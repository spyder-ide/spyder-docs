"""Common tasks to build, check and publish Spyder-Docs."""

# Standard library imports
import contextlib
import logging
import os
import tempfile
import shutil
import sys
import webbrowser
from pathlib import Path

# Third party imports
import nox  # pylint: disable=import-error
import nox.logger  # pylint: disable=import-error


# --- Global constants --- #

nox.options.error_on_external_run = True
nox.options.sessions = ["build"]
nox.options.default_venv_backend = "none"


CI = "CI" in os.environ
CANARY_COMMAND = ("sphinx-build", "--version")

BUILD_INVOCATION = ("python", "-m", "sphinx", "--color")
SOURCE_DIR = Path("doc").resolve()
BUILD_DIR = Path("doc/_build").resolve()
BUILD_OPTIONS = ("-n", "-W", "--keep-going")

HTML_BUILDER = "html"
HTML_BUILD_DIR = BUILD_DIR / "html"
HTML_INDEX_PATH = HTML_BUILD_DIR / "index.html"

SCRIPT_DIR = Path("scripts").resolve()

LATEST_VERSION = 5
BASE_URL = "https://docs.spyder-ide.org"


# ---- Helpers ---- #

@contextlib.contextmanager
def set_log_level(logger=nox.logger.logger, level=logging.CRITICAL):
    """Context manager to set a logger log level and reset it after."""
    prev_level = logger.level
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(prev_level)


def split_sequence(seq, sep="--"):
    """Split a sequence by a single separator."""
    if sep not in seq:
        seq.append(sep)
    idx = seq.index(sep)
    return seq[:idx], seq[idx + 1:]


def process_filenames(filenames, source_dir=SOURCE_DIR):
    """If filepaths are missing the source directory, add it automatically."""
    source_dir = Path(source_dir)
    filenames = [
        str(source_dir / filename)
        if source_dir not in Path(filename).resolve().parents
        else filename
        for filename in filenames
    ]
    return filenames


def construct_sphinx_invocation(
    posargs=(),
    builder=HTML_BUILDER,
    source_dir=SOURCE_DIR,
    build_dir=BUILD_DIR,
    build_options=BUILD_OPTIONS,
    build_invocation=BUILD_INVOCATION,
):
    """Reusably build a Sphinx invocation string from the given arguments."""
    extra_options, filenames = split_sequence(posargs)
    filenames = process_filenames(filenames, source_dir=source_dir)
    sphinx_invocation = [
        *build_invocation,
        "-b",
        builder,
        *build_options,
        *extra_options,
        str(source_dir),
        str(Path(build_dir) / builder),
        *filenames,
    ]
    return sphinx_invocation


# ---- Dispatch ---- #

# Workaround for Nox not (yet) supporting shared venvs
# See: https://github.com/wntrblm/nox/issues/167
@nox.session(venv_backend="virtualenv", reuse_venv=True)
def _execute(session):
    """Dispatch tasks to run in a common environment. Do not run directly."""
    if not session.posargs or isinstance(session.posargs[0], str):
        raise ValueError(
            "Must pass a list of functions to execute as first posarg")

    if not session.posargs or session.posargs[0] is not _install:
        # pylint: disable=too-many-try-statements
        try:
            with set_log_level():
                session.run(
                    *CANARY_COMMAND, include_outer_env=False, silent=True)
        except nox.command.CommandFailed:
            print("Installing dependencies in isolated environment...")
            _install(session)

    if session.posargs:
        for task in session.posargs[0]:
            task(session)


# ---- Install ---- #

def _install(session):
    """Execute the dependency installation."""
    session.install("-r", "requirements.txt")


@nox.session
def install(session):
    """Install the project's dependencies in a virtual environment."""
    session.notify("_execute", posargs=([_install],))


# ---- Utility ---- #

def _build_help(session):
    """Print Sphinx --help."""
    session.run(*BUILD_INVOCATION, "--help")


@nox.session(name="help")
def build_help(session):
    """Get help with the project build."""
    session.notify("_execute", posargs=([_build_help],))


def _run(session):
    """Run an arbitrary command in the project's venv."""
    session.run(*session.posargs[1:])


@nox.session()
def run(session):
    """Run any command."""
    session.notify("_execute", posargs=([_run], *session.posargs))


def _clean():
    """Remove the Sphinx build directory."""
    try:
        BUILD_DIR.unlink()
    except FileNotFoundError:
        pass


@nox.session
def clean(_session):
    """Clean build artifacts."""
    _clean()


# ---- Build ---- #

def _build(session):
    """Execute the docs build."""
    sphinx_invocation = construct_sphinx_invocation(
        posargs=session.posargs[1:])
    session.run(*sphinx_invocation)


@nox.session
def build(session):
    """Build the project."""
    session.notify("_execute", posargs=([_build], *session.posargs))


def _serve():
    """Open the docs in a web browser."""
    webbrowser.open(HTML_INDEX_PATH.as_uri())


@nox.session
def serve(_session):
    """Display the project."""
    _serve()


def _autobuild(session):
    """Use Sphinx-Autobuild to rebuild the project and open in browser."""
    session.install("sphinx-autobuild")

    with tempfile.TemporaryDirectory() as destination:
        sphinx_invocation = construct_sphinx_invocation(
            posargs=session.posargs[1:],
            build_dir=destination,
            build_options=list(BUILD_OPTIONS) + ["-a"],
            build_invocation=[
                "sphinx-autobuild",
                "--port=0",
                f"--watch={SOURCE_DIR}",
                "--open-browser",
            ]
        )
        session.run(*sphinx_invocation)


@nox.session
def autobuild(session):
    """Rebuild the project continuously as source files are changed."""
    session.notify("_execute", posargs=([_autobuild], *session.posargs))


# ---- Deploy ---- #

def _deploy():
    """Execute the pre-deployment steps for multi-version support."""
    # pylint: disable=import-outside-toplevel

    sys.path.append(str(SCRIPT_DIR))
    import generateredirects
    import safecopy

    latest_version_dir = HTML_BUILD_DIR / str(LATEST_VERSION)
    shutil.copytree(
        HTML_BUILD_DIR, latest_version_dir, copy_function=shutil.move)
    safecopy.copy_dir_if_not_existing(
        source_dir=str(LATEST_VERSION),
        target_dir="current",
        base_path=HTML_BUILD_DIR,
        verbose=True,
    )
    generateredirects.generate_redirects(
        canonical_dir="current",
        base_path=HTML_BUILD_DIR,
        verbose=True,
        base_url=BASE_URL,
    )


@nox.session
def deploy(_session):
    """Prepare the project for deployment."""
    _deploy()


# ---- Check ---- #

def _install_hooks(session):
    """Run pre-commit install to install the project's hooks."""
    session.run(
        "pre-commit",
        "install",
        "--hook-type",
        "pre-commit",
        "--hook-type",
        "commit-msg",
    )


@nox.session(name="install-hooks")
def install_hooks(session):
    """Install the project's pre-commit hooks."""
    session.notify("_execute", posargs=([_install_hooks],))


def _uninstall_hooks(session):
    """Run pre-commit uninstall to uninstall the project's hooks."""
    session.run(
        "pre-commit",
        "uninstall",
        "--hook-type",
        "pre-commit",
        "--hook-type",
        "commit-msg",
    )


@nox.session(name="uninstall-hooks")
def uninstall_hooks(session):
    """Uninstall the project's pre-commit hooks."""
    session.notify("_execute", posargs=([_uninstall_hooks],))


def _lint(session):
    """Run linting on the project via pre-commit."""
    extra_options = ["--show-diff-on-failure"] if CI else []
    session.run(
        "pre-commit", "run", "--all", *extra_options, *session.posargs[1:])


@nox.session
def lint(session):
    """Lint the project."""
    session.notify("_execute", posargs=([_lint], *session.posargs))


def _linkcheck(session):
    """Run Sphinx linkcheck on the docs."""
    sphinx_invocation = construct_sphinx_invocation(
        posargs=session.posargs[1:], builder="linkcheck")
    session.run(*sphinx_invocation)


@nox.session
def linkcheck(session):
    """Check that links in the project are valid."""
    session.notify("_execute", posargs=([_linkcheck], *session.posargs))
