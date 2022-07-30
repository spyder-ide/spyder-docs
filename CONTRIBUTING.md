# Contributing to the Spyder Documentation

First off, thanks for your interest in helping out with the documentation for Spyder, the Scientific Python Development Environment!

**Important Note:** This is the repository for the documentation sources used to build the [Spyder docs site](https://docs.Spyder-IDE.org/)—not the IDE itself.
For more information about Spyder, please see the [website](https://www.spyder-ide.org/), and for the core Spyder codebase, visit the [main repo](https://github.com/spyder-ide/spyder).
You can view the live documentation for current and past Spyder versions at [docs.Spyder-IDE.org](https://docs.spyder-ide.org).

Spyder-Docs is part of the Spyder IDE Github org, and is developed with standard Github flow.
If you're not comfortable with at least the basics of ``git`` and GitHub, we recommend reading beginner tutorials such as [GitHub's Git Guide](https://github.com/git-guides/), its [introduction to basic Git commands](https://guides.github.com/introduction/git-handbook/#basic-git) and its [guide to the fork workflow](https://guides.github.com/activities/forking/), or (if you prefer) their [video equivalents](https://www.youtube.com/githubguides).
However, this contributing guide should fill you in on most of the basics you need to know.

For an introduction to the basics of reST syntax, the source format in which Spyder's documentation is written, see the [Sphinx reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).

Let us know if you have any further questions, and we look forward to your contributions!


<!-- markdownlint-disable -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Reporting Issues](#reporting-issues)
- [Setting Up a Development Environment](#setting-up-a-development-environment)
  - [Fork and clone the repo](#fork-and-clone-the-repo)
  - [Create and activate a fresh environment](#create-and-activate-a-fresh-environment)
  - [Install dependencies](#install-dependencies)
  - [Install the required Pre-Commit hooks](#install-the-required-pre-commit-hooks)
- [Building the docs](#building-the-docs)
- [Deciding Which Branch to Use](#deciding-which-branch-to-use)
- [Making Your Changes](#making-your-changes)
- [Pushing your Branch](#pushing-your-branch)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Standards and Conventions](#standards-and-conventions)
  - [Key standards](#key-standards)
  - [Style conventions](#style-conventions)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- markdownlint-restore -->



## Reporting Issues

Find a typo in the text, a passage that could be clarified, or would like a section or document added or expanded upon?
Please [open](https://github.com/spyder-ide/spyder-docs/issues/new/choose) an [issue](https://github.com/spyder-ide/spyder-docs/issues) documenting the bug, enhancement or new content following the guidance in our issue template.

If referring to a particular word, line or section, please be sure to provide a snippet of context and/or the file and line number to allow us to find and fix it, and if pointing out a problem, please be as specific as you can in suggesting a revised wording that would solve it.



## Setting Up a Development Environment

For non-trivial changes, its easy to work with Spyder-Docs locally by following a few simple steps.

**Note**: You may need to substitute ``python3`` for ``python`` in the commands below on some Linux distros where ``python`` isn't mapped to ``python3`` (yet).


### Fork and clone the repo

First, navigate to the [project repository](https://github.com/spyder-ide/spyder-docs) in your web browser and press the ``Fork`` button to make a personal copy of the repository on your own Github account.
Then, click the ``Clone or Download`` button on your repository, copy the link and run the following on the command line to clone the repo:

```shell
git clone <LINK-TO-YOUR-REPO>
```

Finally, set the upstream remote to the official Spyder-Docs repo with:

```shell
git remote add upstream https://github.com/spyder-ide/spyder-docs.git
```


### Create and activate a fresh environment

We highly recommend you create and activate a virtual environment to avoid any conflicts with other packages on your system or causing any other issues.
Of course, you're free to use any environment management tool of your choice (conda, virtualenvwrapper, pyenv, etc).
Regardless of the tool you use, make sure to remember to always activate your environment before using it.


#### Conda

To create an environment with Conda (recommended), simply execute the following:

```shell
conda create -c conda-forge -n spyder-docs-env python=3.9
```

Then, activate it with

```shell
conda activate spyder-docs-env
```


#### Pip/Venv

With pip/venv, you can create a virtual environment with

```shell
python -m venv spyder-docs-env
```

And activate it with the following on Linux and macOS,

```bash
source spyder-docs-env/bin/activate
```

or on Windows (``cmd.exe``),

```cmd
.\spyder-docs-env\Scripts\activate.bat
```



### Install dependencies

Then, you need to install the appropriate dependencies in your active Python environment to develop and build the documentation.
You can install them into your current Conda environment with:

```shell
conda install -c conda-forge --file requirements-conda.txt
python -m pip install -r requirements-dev.txt
```

Or, if using ``pip``, you can grab them with just:

```shell
python -m pip install -r requirements-dev.txt
```


### Install the required Pre-Commit hooks

This repository uses [Pre-Commit](https://pre-commit.com/) to install, configure and update a suite of pre-commit hooks that check for common problems and issues, and fix many of them automatically.
You'll need to install the pre-commit hooks before committing any changes, as they both auto-generate/update specific files and run a comprehensive series of checks to help you find likely errors and enforce the project's code quality guidelines and style guide.
They are also run on all pull requests, and will need to pass before your changes can be merged.
Pre-commit itself is installed with the [above commands](#install-dependencies), and its hooks should be enabled by running the following from the root of this repo:

```shell
pre-commit install --hook-type pre-commit --hook-type commit-msg
```

The hooks will be automatically run against any new/changed files every time you commit.
It may take a few minutes to install the needed packages the first time you commit, but subsequent runs should only take a few seconds.
If you made one or more commits before installing the hooks (not recommended), you can run them manually on all the files in the repo with:

```shell
pre-commit run --all-files
```

**Note**: Many of the hooks fix the problems they detect automatically (the hook output will say ``Files were modified by this hook``, and no errors/warnings will be listed), but they will still abort the commit so you can double-check everything first.
Once you're satisfied, ``git add .`` and commit again.



## Building the docs

To build the docs locally with Sphinx, you can easily do so with our makefile from the Terminal/command line, or via running the appropriate Sphinx command.

To build just the docs for the current version, run the following on a system terminal with ``make`` (macOS/Linux):

```bash
make docs
make serve
```

To build the full site with the documentation for all Spyder versions, run:

```bash
make multidocs
```

On a system without ``make`` (like Windows, by default), or to build the docs manually, run:

```shell
python -m sphinx -n -W --keep-going -b html doc doc/_build/html
```

If you've run ``make serve``, the rendered documentation should open automatically in your default web browser.
Otherwise, navigate to the ``_build/html`` directory inside the ``spyder-docs`` repository and open ``index.html`` (the main page of the docs) in your browser.



## Deciding Which Branch to Use

When you start to work on a new pull request (PR), you need to be sure that your work is done on top of the correct branch, and that you base your PR on Github against it.

To guide you, issues on Github are marked with a milestone that indicates the correct branch to use.
If not, follow these guidelines:

* The ``master`` branch contains the in-development documentation for Spyder 5; most general changes and those specific to that version should be made against this branch.
* The ``4.x`` branch contains the docs for Spyder 4 and is in bugfix-only mode; no substantial new content should be added here at this point.
* The ``3.x`` branch is frozen, containing the docs for the legacy Spyder 3 version; no further PRs will be accepted

Of course, if an issue is only present in a specific branch, please base your PR on that branch.
If you are at all unsure which branch to use, we'll be happy to guide you.



## Making Your Changes

To start working on a new PR, you need to execute these commands, filling in the branch names where appropriate (``<BASE-BRANCH>`` is the branch you're basing your work against, e.g. ``master``, while ``<FEATURE-BRANCH>`` is the branch you'll be creating to store your changes, e.g. ``fix-doc-typo`` or ``add-plugin-guide``:

```shell
git checkout <BASE-BRANCH>
git pull upstream <BASE-BRANCH>
git checkout -b <FEATURE-BRANCH>
```

Once you've made and tested your changes, commit them with a descriptive, unique message of 74 characters or less written in the imperative tense, with a capitalized first letter and no period at the end.
Try to make your commit message understandable on its own, giving the reader a high-level idea of what your changes accomplished without having to dig into the full diff output.
For example:

```shell
git commit -am "Add new guide on developing plugins for Spyder"
```

If your changes are complex (more than a few dozen lines) and can be broken into discrete steps/parts, its often a good idea to make multiple commits as you work.
On the other hand, if your changes are fairly small (less than a dozen lines), its usually better to make them as a single commit, and then use the ``git -a --amend`` (followed by ``git push -f``, if you've already pushed your work) if you spot a bug or a reviewer requests a small change.

These aren't hard and fast rules, so just use your best judgment, and if there does happen to be a significant issue we'll be happy to help.



## Pushing your Branch

Now that your changes are ready to go, you'll need to push them to the appropriate remote repository.
All contributors, including core developers, should push to their personal fork and submit a PR from there, to avoid cluttering the upstream repo with feature branches.
To do so, run:

```shell
git push -u origin <FEATURE-BRANCH>
```

Where ``<FEATURE-BRANCH>`` is the name of your feature branch, e.g. ``fix-docs-typo``.



## Submitting a Pull Request

Finally, create a pull request to the [spyder-ide/spyder-docs repository](https://github.com/spyder-ide/spyder-docs/) on Github.
Make sure to set the target branch to the one you based your PR off of (``master`` or ``X.x``).

We'll then review your changes, and after they're ready to go, your work will become an official part of Spyder-Docs.

Thanks for taking the time to read and follow this guide, and we look forward to your contributions!



## Standards and Conventions

### Key standards

Make sure you follow these to ensure clarity, consistency and correctness throughout our documentation and its repo.

* **[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)** (reST/rst) for documentation format
* **[PEP 8](https://www.python.org/dev/peps/pep-0008/)** style for any Python code
* **[UTF-8](https://en.wikipedia.org/wiki/UTF-8)** (no BOM) for character encoding
* **[LF](https://en.wikipedia.org/wiki/Newline)** for newlines
* **[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)** (YYYY-MM-DD HH:MM:SS) for dates/times
* **[SI/metric](https://en.wikipedia.org/wiki/International_System_of_Units)** for units


### Style conventions

This section summarizes the important points for doc authors to actively keep in mind while writing the documentation.
See the [Style Guide](https://github.com/spyder-ide/spyder-docs/blob/master/STYLEGUIDE.md) for a comprehensive reference on a wide variety of topics that may be pertinent to specific situations encountered when working on the docs.
If you're not sure about something, don't worry about it!
Feel free to ask, or request a maintainer take care of the style details for you.

* **Admonitions**: ``important::`` for key points, ``warnings`` for things to avoid, and ``note::`` for everything else.
* **Blank lines**: One after all headings and before and after paragraphs, directives and ``|``s
* **Filenames**: Lowercase, hyphen-separated
* **Headings**: *Level 1*—Page titles, title case, ``###`` top and bottom; *Level 2*—3 blank lines before, Sentence case, ``===`` top and bottom; *Level 3*—2 blank lines before, Sentence case, ``~~~`` bottom; *Level 4*—1 blank line before, Sentence case, ``---`` bottom
* **Images/GIFS**: Full width, 690 px or 500 px; manual break (``|``) after before a new section; PNGs or GIFs 5-10 s at 5 frames/s
* **Indentation**: Spaces, no tabs; 3 spaces after directives, 4 inside code blocks
* **Line breaks**: Break by sentence for text, 70 characters for code
* **Lists**: ``#.`` for lists that have inherent order, ``*`` otherwise
* **reST directives**: ``:file:`` for file paths; ``:kbd:`` for keyboard shortcuts; ``:guilabel:`` buttons, labels, options and other UI items; ``:menuselection`` for menu items and preference panes; ``code-block::`` for code
