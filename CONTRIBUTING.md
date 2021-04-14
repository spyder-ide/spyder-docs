# Contributing to the Spyder Documentation

First off, thanks for your interest in helping out with the documentation for Spyder, the Scientific Python Development Environment!

**Important Note:** This is the repository for the documentation sources used to build the [Spyder docs site](https://docs.Spyder-IDE.org/)—not the IDE itself.
For more information about Spyder, please see the [website](https://www.spyder-ide.org/), and for the core Spyder codebase, visit the [main repo](https://github.com/spyder-ide/spyder).
You can view the live documentation for current and past Spyder versions at [docs.Spyder-IDE.org](https://docs.spyder-ide.org).
For more guidance on the basics of using ``git`` and Github to contribute to Spyder and its documentation, please see the [contributing guide](https://github.com/spyder-ide/spyder/blob/master/CONTRIBUTING.md) in the main Spyder repository mentioned above, and check out the [Spyder Development Documentation](https://github.com/spyder-ide/spyder/wiki/Contributing-to-Spyder) for detailed information.
For an introduction to the basics of reST syntax, the source format in which Spyder's documentation is written, see the [Sphinx reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).



## Reporting Issues

If you find a typo in the text, a passage that could be clarified, or would like a section or document added or expanded upon, please submit an issue report documenting the bug, enhancement or new content following the guidance in our issue template.

If referring to a particular word, line or section, please be sure to provide a snippet of context and/or the file and line number to allow us to find and fix it, and if pointing out a problem, please be as specific as you can in suggesting a revised wording that would solve it.
Issue reports that don't contain enough information to allow us to do something about them will be closed.



## Documentation Branches

* Currently, all PRs should be based against ``master``, which contains the in-development documentation for the current Spyder 4 release.
* The ``3.x`` branch is frozen, containing the docs for the legacy Spyder 3 version

In the near future, the ``4.x`` branch will be contain the docs for the stable version, while ``master`` will be dedicated to the changes necessary for Spyder 5.



## Submitting Pull Requests

We welcome contributions from the community, and will do our best to review all of them in a timely fashion.
To do so, please submit a pull request (PR) to this repo against the appropriate branch with your changes, and create a corresponding issue as well if your change is substantive, so that we can keep track of everything and give you credit for closing it.

Please make sure your PR titles are brief but descriptive, and include ``PR: `` as a prefix; most importantly, make sure you follow and fill out the template provided, which should guide you through the process and make sure everything runs smoothly.



## Building and Testing Locally

For non-trivial changes, its easy to work with Spyder-Docs locally by following a few simple steps.


### Install dependencies

Make sure you have the appropriate dependencies installed in your active Python environment for the script to work.
You can install them into your current conda environment with:

```bash
conda install -c conda-forge --file requirements-conda.txt
pip install -r requirements-dev.txt
```

Or, if using ``pip`` (``pip3`` on Linux), you can grab them with just:

```bash
pip install -r requirements-dev.txt
```


### Build the docs

To build the docs locally with Sphinx, you can easily do so with our makefile from the Terminal/command line (or the Anaconda prompt on Windows).

To build just the docs for the current version, run the following if on macOS/Linux:

```bash
make docs
make serve
```

or, if on Windows:

```cmd
cd doc
make.bat html
cd ..
```

**NOTE:** You can try to use the `make` commands on Windows if you have `make` installed and something like `Cygwin`, `MSYS2` or `MYSYS`, or by using Windows Subsystem for Linux (`WSL`).

To build the full site with the documentation for all Spyder versions, run:

```bash
make multidocs
```

Either way, you should be able to view the HTML output inside the resulting ``_build`` directory the build commands produce; ``index.html`` is the main page.



## Netlify Notes

* The `runtime.txt` file in the root of the repo is needed by Netlify to declare the Python version required to build the docs.
* By default, Netlify adds a lot of checks to pull requests, besides the one that actually builds the live preview.
  To remove those extra checks, you need to go to the `Build and deploy` configuration entry, then to the `Outgoing notifications` section, and remove all commit notifications that don't start with `Add Deploy Preview`.



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

* **Admonitions**: ``important::`` for key points, ``warnings`` for things to avoid, and ``note::`` for everything else.
* **Blank lines**: One after all headings and before and after paragraphs, directives and ``|``s
* **Filenames**: Lowercase, hyphen-separated
* **Headings**: *Level 1*—Page titles, title case, ``###`` top and bottom; *Level 2*—3 blank lines before, Sentence case, ``===`` top and bottom; *Level 3*—2 blank lines before, Sentence case, ``~~~`` bottom; *Level 4*—1 blank line before, Sentence case, ``---`` bottom
* **Images/GIFS**: Full width, 690 px or 500 px; manual break (``|``) after before a new section; PNGs or GIFs 5-10 s at 5 frames/s
* **Indentation**: Spaces, no tabs; 3 spaces after directives, 4 inside code blocks
* **Line breaks**: Break by sentence for text, 70 characters for code
* **Lists**: ``#. `` for lists that have inherent order, ``* `` otherwise
* **reST directives**: ``:file:`` for file paths; ``:kbd:`` for keyboard shortcuts; ``:guilabel:`` buttons, labels, options and other UI items; ``:menuselection`` for menu items and preference panes; ``code-block::`` for code
