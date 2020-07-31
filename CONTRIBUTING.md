# Contributing to the Spyder Documentation

First off, thanks for your interest in helping out with the documentation
for Spyder, the Scientific Python Development Environment!

**Important Note:** This is the repository for Spyder's documentation sources
used to build the [Spyder docs site](https://docs.Spyder-IDE.org/)
—not the IDE itself. For more information about Spyder, please see the
[website](https://www.spyder-ide.org/), and for the core Spyder codebase,
visit the [main repo](https://github.com/spyder-ide/spyder) . Thanks!

For more guidance on the basics of using ``git`` and Github to contribute
to Spyder and its documentation, please see the contributing guidelines in
the main Spyder repository mentioned above, and check out the
[Spyder Development Documentation]
(https://github.com/spyder-ide/spyder/wiki/Contributing-to-Spyder)
for detailed instructions.

To view the rendered and deployed documentation itself, please visit:

* Develop (4.x): https://docs.spyder-ide.org/develop

* Stable (3.x): https://docs.spyder-ide.org/


## Reporting Issues

If you find a typo in the text, a passage that could be clarified,
or would like a section or document added or expanded upon, please submit
an issue report documenting the bug, enhancement or new content
following the guidance in our issue template.

If referring to a particular word, line or section, please be sure to provide
a snippet of context and/or the file and line number to allow us to find
and fix it, and if pointing out a problem, please be as specific as you can
in suggesting a revised wording that would solve it. Issue reports that
don't contain enough information to allow us to do something about them
will be closed.



## Documentation Branches

* Submit PRs against ``3.x`` for changes to documentation relevant to the
  current stable Spyder 3 release
* Base against ``master`` for fixes or additions that only apply to the
  future Spyder 4 feature release.



## Submitting Pull Requests

We welcome contributions from the community, and will do our best to
review all of them in a timely fashion. To do so, please submit a
pull request (PR) to this repo against the appropriate branch with your
changes, and create a corresponding issue as well if your change is
substantive, so that we can keep track of everything and give you
credit for closing it.

Please make sure your PR titles are brief but descriptive, and include ``PR: ``
as a prefix (if a work in progress, also prefix ``[WiP]``); most importantly,
make sure you follow and fill out the template provided, which should guide
you through the process and make sure everything runs smoothly.



## Building the Docs Locally

To build the docs locally with Sphinx, you can easily do so with our makefile
from the Terminal/command line (or the Anaconda prompt on Windows).

Make sure you have ``sphinx`` installed in your active Python environment
for the script to work; if you have Anaconda you should have it already,
at least in your base env or any one with Spyder installed. If you need it,
you can install it into your present environemnt with

```bash
conda install sphinx
pip install sphinx-panels
pip install git+https://github.com/spyder-ide/spyder-docs-sphinx-theme.git@develop_spyder
```

Or, if using ``pip``, you can grab it with

```bash
pip install sphinx sphinx-panels
pip install git+https://github.com/spyder-ide/spyder-docs-sphinx-theme.git@develop_spyder
```

Now, run the following if on macOS/Linux:

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

to run the build. You should be able to view the html output inside the
resulting ``_build`` directory it produces; ``index.html`` is the main page.

**NOTE:** You can try to use the `make` commands on Windows if you have `make` installed and something like `Cygwin`, `MSYS2` or `MYSYS`, or by using Windows Subsystem for Linux (`WSL`).


## Standards and Conventions

Make sure you follow these to ensure clarity, consistency and correctness
throughout our documentation and its repo.

* **reStructuredText** (rst) for documentation format
* **PEP8** style for any Python code
* **79 characters** for line length on initial creation
* **UTF-8** for character encoding
* **LF** for newlines
* **ISO 8601** (YYYY-MM-DD HH:MM:SS) for dates/times
* **SI/metric** for units
