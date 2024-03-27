.. _install-guide:

##################
Installation Guide
##################

Spyder is relatively easy to install on Windows, Linux and macOS.
Just make sure to read and follow these instructions with care.

If you run into problems, before posting a report, *please* consult our comprehensive :doc:`troubleshooting guide</troubleshooting/first-steps>` and search the `issue tracker`_ for your error message and problem description.
These methods generally fix or isolate the great majority of install-related difficulties.
Thanks!

.. _issue tracker: https://github.com/spyder-ide/spyder/issues

.. note::

   For most users on Windows and macOS, we recommend our :ref:`install-standalone` as the most straightforward and robust option to obtain Spyder.
   For users needing Linux support, third-party Spyder plugins or Variable Explorer compatibility with custom-installed packages—all capabilities which the standalone installers currently do not yet provide—we advise using a :ref:`install-conda`.
   Linux, plugin and package/environment management support in the standalone installers are currently under active development for future Spyder versions.


.. _install-binder:

=================
Try Spyder online
=================

Want to try out Spyder without installing it?
With `Binder`_ you can work with a fully functional copy of Spyder online that runs right in your web browser, no installation needed.
Visit the `Spyder Binder`_ to get started using Spyder.

.. _Binder: https://mybinder.org/
.. _Spyder Binder: https://mybinder.org/v2/gh/spyder-ide/binder-environments/spyder-stable?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fspyder-ide%252FSpyder-Workshop%26urlpath%3Ddesktop%252F%26branch%3Dmaster

.. image:: /images/installation/installation-spyder-binder.png
   :alt: Spyder running on Binder



.. _install-standalone:

=====================
Standalone installers
=====================

The standalone installers are our recommended method for most users on Windows and macOS, with experimental Linux support under active development.
They work like any other IDE, where Spyder can be installed and updated independently of the Python environments you use to run your code.
This avoids the problems with incompatible packages and broken installations users often face when mixing Spyder with the (Conda, etc) environments they use to run their code.

The installers include a built-in Python environment with the most common scientific libraries (e.g. NumPy, Pandas, Matpotlib, etc), which can be used out of the box for basic data analysis tasks.
However, to manage your own packages and environments, you'll currently need to connect an external Python distribution (such as `Anaconda`_, `Miniconda`_, `Miniforge/Mambaforge`_, `WinPython`_ or `Python.org <Python_>`__) to your standalone copy of Spyder.
For more information on this, see our :ref:`FAQ entry on the subject <using-packages-installer>`.

.. note::

   The standalone installers do not yet support installing third-party Spyder plugins not already bundled with them, though this feature is currently under development.
   For now, if you need this capability, we recommend a :ref:`install-conda`.


.. _install-standalone-installing:

Downloading and installing
~~~~~~~~~~~~~~~~~~~~~~~~~~

To download the supported Spyder installer for your platform, simply click the appropriate link below (for Linux, see the :ref:`install-conda` section).
Then, double-click the downloaded file to open the installer.
If a security warning pops up, you may need to click :guilabel:`Yes`, :guilabel:`OK`, :guilabel:`Open`, :guilabel:`Allow` or similar.

On Windows, if a "SmartScreen" dialog appears, click :guilabel:`More info` followed by :guilabel:`Run anyway`, and then proceed through the steps in the installer.

On macOS, open the disk image and drag Spyder to your :guilabel:`Applications` folder.

.. rst-class:: installer-table

.. table::

   ================ ================ ================
   `Windows`_       `macOS M1`_      `macOS Intel`_
   ================ ================ ================

.. _Windows: https://github.com/spyder-ide/spyder/releases/latest/download/Spyder_64bit_full.exe
.. _macOS M1: https://github.com/spyder-ide/spyder/releases/latest/download/Spyder_arm64.dmg
.. _macOS Intel: https://github.com/spyder-ide/spyder/releases/latest/download/Spyder.dmg

.. note::

   "Lite" versions of both installers are also available from the `releases page`_, which are somewhat smaller than the full installers.
   These lack a number of optional but recommended dependencies, such as NumPy, SciPy and Pandas, meaning that a few :doc:`/panes/variableexplorer` features, including graphical data import wizards and support for rich display and editing of NumPy arrays and Pandas DataFrames, will not be available.
   Given this only saves a modest amount of space while missing out on significant features, we recommend using the full installers unless minimizing download/install size and memory usage is a priority.

.. _releases page: https://github.com/spyder-ide/spyder/releases/latest


.. _install-standalone-running:

Running from a standalone install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run Spyder when installed standalone, you can simply use your operating system's typical method of launching applications, such as opening it from the :guilabel:`Start` menu on Windows (or the Taskbar, if you've pinned it there), or from Launchpad, Spotlight or the :guilabel:`Applications` folder on macOS (or the Dock, if you've added it there).


.. _install-standalone-update:

Updating a standalone install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, Spyder checks for updates automatically on startup, and you can also check manually with :menuselection:`Help --> Check for updates`.
The standalone installers for Spyder 5.4.0+ include update functionality built right into Spyder, which after checking for updates will display a prompt to automatically download and install the current version.
On earlier versions, you'll need to manually download and install the latest release (if on Windows, make sure to remove the old version first from Control Panel/System Settings).



.. _install-conda:

=========================
Conda-based distributions
=========================

Spyder is included by default in the `Anaconda`_ Python distribution, which comes with everything you need to get started in an all-in-one package.
It can also be easily installed in the much lighter-weight `Miniconda`_ and `Miniforge/Mambaforge`_, which include just Python and the Conda/Mamba package and environment manager by default (with Miniforge defaulting to the Conda-Forge channel, and Mambaforge using Mamba, a much faster alternative to Conda).
This is our recommended installation method on Linux and for users with third-party Spyder plugins, as support for both of these in our standalone installers is still under active development.

.. _Anaconda: https://www.anaconda.com/products/distribution
.. _Miniconda: https://conda.io/miniconda.html
.. _Miniforge/Mambaforge: https://github.com/conda-forge/miniforge


.. _install-conda-environment:

Conda environment
~~~~~~~~~~~~~~~~~

With Miniconda/Miniforge/Mambaforge, or to get a more reliable and up-to-date Spyder version with Anaconda, we strongly recommend installing Spyder into its own dedicated Conda environment.

.. note::

   If using Mamba/Mambaforge, substitute ``mamba`` for ``conda`` in the following commands.


.. _install-conda-installing:

Installing with Conda
---------------------

For a full install of Spyder and all optional dependencies, run the following command in your Anaconda Prompt (Windows) or terminal:

.. code-block:: shell

   conda create -c conda-forge -n spyder-env spyder numpy scipy pandas matplotlib sympy cython

For a minimal install without the optional functionality and integration with the above packages, you can instead run:

.. code-block:: shell

   conda create -c conda-forge -n spyder-env spyder

This installs Spyder into a new environment called ``spyder-env``, using the more up-to-date, community-run Conda-Forge channel.
To make sure future installs/updates in this environment also use Conda-Forge and are faster and more reliable, make sure to set it as your environment's default channel with strict channel priority enabled, if this isn't the case already (as it is with Miniforge/Mambaforge or if you've manually configured it):

.. code-block:: shell

   conda activate spyder-env
   conda config --env --add channels conda-forge
   conda config --env --set channel_priority strict

Here's a summary of the main steps.

.. image:: /images/installation/installation-conda-install.gif
   :alt: Running Spyder installation with conda


.. _install-conda-running:

Running with Conda
------------------

You can then run Spyder by the same methods :ref:`as with Anaconda <install-anaconda-running>`, except that you need to make sure to launch the Start menu shortcut with ``(spyder-env)`` in the name, select the ``spyder-env`` environment on the left before launching it with Navigator, or type ``conda activate spyder-env`` before launching it on the command line.

See :ref:`our FAQ question <using-existing-environment>` for more information about how to use Spyder with your existing Conda environments.


.. _install-conda-update:

Updating with Conda
-------------------

With any Conda-based distribution and Spyder installed in its own environment (recommended), update Conda itself, active the environment, and finally update Spyder.
In your system terminal (or Anaconda Prompt if on Windows), run:

.. code-block:: shell

   conda update -n base conda
   conda activate spyder-env
   conda update spyder

In case you get an error trying to update, just remove the existing environment (if using one other than ``base``):

.. code-block:: shell

   conda remove -n spyder-env --all

And then :ref:`recreate a fresh one <install-conda-installing>`.


.. _install-anaconda-base:

Anaconda base
~~~~~~~~~~~~~

While we recommend always using a dedicated environment, with Anaconda you can also run the bundled copy of Spyder from the built-in ``base`` environment.

.. caution::

   The bundled Spyder version can often be quite out of date, missing new features and bug fixes from the latest version, and if you install, change or remove other packages, there is a significant chance of dependency conflicts or a broken Spyder installation.
   Therefore, we recommend :ref:`installing Spyder into a new Conda environment <install-conda-installing>` to avoid all these issues.


.. _install-anaconda-running:

Running with Anaconda
---------------------

To run the bundled version of Spyder after installing it with Anaconda, the recommended method on Windows is to launch it via the Start menu shortcut.
On other platforms, open Anaconda Navigator, scroll to Spyder under :guilabel:`Home` and click :guilabel:`Launch`.

.. image:: /images/installation/installation-anaconda-navigator.png
   :alt: Anaconda Navigator showing Spyder

If Spyder does not start via this method or you prefer to use the command line, open Anaconda Prompt (Windows) or your terminal (other platforms), type ``conda activate base`` then ``spyder``.


.. _install-anaconda-update:

Updating with Anaconda
----------------------

With Spyder installed in Anaconda's ``base`` environment, first update the ``anaconda`` meta-package, and then Spyder itself (in case there is a newer version than that pinned to the ``anaconda`` metapackage).
In your system terminal (or Anaconda Prompt if on Windows), run:

.. code-block:: shell

   conda update anaconda
   conda install spyder=5.4.3

.. note::

   These commands also update all your other packages, which is one reason we strongly recommend you use an isolated conda environment to avoid any potential unintended effects on other installed packages.

In case you get an error resolving dependencies, try uninstalling Spyder and re-installing it:

.. code-block:: shell

   conda remove spyder
   conda install spyder



.. _install-pip:

=========
Using pip
=========

.. caution::

   While this installation method is a viable option for experienced users, installing Spyder (and other PyData-stack packages) with pip can sometimes lead to tricky issues, particularly on Windows and macOS.
   While you are welcome to try it on your own, we are typically not able to provide individual support for installation problems with pip, except to recommend our :ref:`install-standalone` (Windows and macOS) or a :ref:`install-conda`.

You can install Spyder with the pip package manager, which is included by default with most Python installations.
Before installing Spyder itself by this method, you need to download the `Python`_ programming language.

.. _Python: https://www.python.org/

.. note::

   Due to a known issue with some DEB-based Linux distributions (Debian, Ubuntu, Mint), you might also need to install the ``pyqt5-dev-tools`` package first, with ``sudo apt install pyqt5-dev-tools``.

You'll first want to create and activate a virtual environment in which to install Spyder, via one of the following methods.

With ``virtualenvwrapper``:

.. code-block:: shell

   mkvirtualenv spyder-env
   workon spyder-env

Otherwise, on macOS/Linux/Unix:

.. code-block:: shell

   python3 -m venv spyder-env
   source spyder-env/bin/activate

or on Windows:

.. code-block:: batch

   python -m venv spyder-env
   spyder-env\Scripts\activate.bat

After activating your environment, to install Spyder and its optional dependencies, run:

.. code-block:: shell

   pip install spyder numpy scipy pandas matplotlib sympy cython

Or for a minimal installation, run:

.. code-block:: shell

   pip install spyder

.. image:: /images/installation/installation-pip-install.gif
   :alt: Running Spyder installation with pip

To launch Spyder after installing it, ensure your environment is activated and run the ``spyder`` or ``spyder3`` command.

And to update Spyder, with your Spyder environment activated, run:

.. code-block:: shell

   pip install --upgrade spyder



.. _install-alternatives:

===================
Alternative methods
===================

.. caution::

   While we describe alternative Spyder installation options for users who prefer them, as these are third-party distributions that we have no direct involvement in, we are usually not able to offer useful individual assistance for problems specific to installing via these alternative methods.

   Also, the Spyder versions they install may be out of date relative to the current release, and thus be missing the latest features and bug fixes.

   Therefore, we recommend you switch to our :ref:`install-standalone` (Windows and macOS) or a :ref:`install-conda` if you encounter installation issues you are unable to solve on your own.


.. _install-windows:

Windows
~~~~~~~

Spyder is included in the `WinPython`_ scientific Python distribution, along with many other common numerical computing and data analysis packages.
You can use Spyder immediately after installing, similar to Anaconda.

.. _WinPython: https://winpython.github.io/


.. _install-macos:

macOS
~~~~~

Spyder is available as `a cask`_ through `Homebrew`_.

.. _a cask: https://formulae.brew.sh/cask/spyder
.. _Homebrew: https://brew.sh/

To install it using the ``brew`` package manager, run:

.. code-block:: shell

   brew install --cask spyder

It is also available as a `a port`_ through `MacPorts`_.

.. _a port: https://ports.macports.org/port/py-spyder/
.. _MacPorts: https://www.macports.org/

To install it using the ``port`` package manager, run:

.. code-block:: shell

   sudo port install py39-spyder


.. _install-linux:

Linux
~~~~~

Spyder can be installed via third-party distro packages on most common Linux distributions.

Running Spyder installed this way will generally be the same as any other distro-installed application.
Alternatively, it can be launched from the terminal with ``spyder`` (or ``spyder3``, on older versions of some distros).


.. _install-debian:

Ubuntu/Debian
-------------

Spyder is available as `a Ubuntu package`_ and `a Debian package`_.

.. _a Ubuntu package: https://packages.ubuntu.com/search?keywords=spyder
.. _a Debian package: https://packages.debian.org/search?searchon=names&keywords=spyder

To install it using the ``apt`` package manager, run:

.. code-block:: shell

   sudo apt install spyder


.. _install-linux-other:

Other distributions
-------------------

Spyder is also available in other GNU/Linux distributions, including:

* `Arch Linux`_
* `Fedora`_
* `Gentoo`_
* `openSUSE`_

.. _Arch Linux: https://aur.archlinux.org/packages/spyder-git/
.. _Fedora: https://fedoraproject.org/wiki/Spyder
.. _Gentoo: https://packages.gentoo.org/packages/dev-python/spyder
.. _openSUSE: https://software.opensuse.org/package/spyder

Please refer to the links or your distribution's documentation for how to install Spyder.



.. _install-dev:

==================
Development builds
==================

If you want to try the next Spyder version before it is released, you can!
You may want to do this for fixing bugs in Spyder, adding new features, learning how Spyder works or just getting a taste of what the IDE can do.
For more information, please see the `Contributing Guide`_ included with the Spyder source or on Github, and for further detail consult the `Spyder development wiki`_.

.. _Contributing Guide: https://github.com/spyder-ide/spyder/blob/master/CONTRIBUTING.md
.. _Spyder development wiki: https://github.com/spyder-ide/spyder/wiki



.. rst-class:: blue-32px

.. _install-help:

===============
Additional help
===============

.. rst-class:: fasb fa-first-aid

*Run in to a problem installing or running Spyder?* Read our :ref:`Troubleshooting Guide <troubleshooting-first-steps>`.

.. rst-class:: fasb fa-globe

*Looking for general information about Spyder and its ecosystem?* See our `main website`_.

.. rst-class:: fasb fa-bug

*Need to submit a bug report or feature request?* Check out our `Github repository`_.

.. rst-class:: fasb fa-code

*Want development-oriented help and information?* Consult our `Github wiki`_.

.. rst-class:: fasb fa-mail-bulk

*Have a help request or discussion topic?* Subscribe to our `Google Group`_.

.. rst-class:: fasb fa-comments

*Asking a quick question or want to chat with the dev team?* Stop by our `Gitter chatroom`_.

.. rst-class:: fabb openteams-icon

*Seeking personalized help from expert Spyder consultants?* Visit `OpenTeams`_.

.. _main website: https://www.spyder-ide.org/
.. _Github repository: https://github.com/spyder-ide/spyder/
.. _Github wiki: https://github.com/spyder-ide/spyder/wiki
.. _Google Group: https://groups.google.com/g/spyderlib
.. _Gitter chatroom: https://gitter.im/spyder-ide/public
.. _OpenTeams: https://www.openteams.com/oss-spyder/
