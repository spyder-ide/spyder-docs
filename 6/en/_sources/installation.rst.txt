.. _install:
.. _install-guide:

#############
Install Guide
#############

Spyder is relatively easy to install on any Windows, Linux or macOS system meeting our basic :ref:`system requirements <run-system-reqs>`.
Just make sure to read and follow these instructions with care.

If you have questions or run into problems, *please* check our :ref:`FAQ <faq-installing>`, consult our :ref:`troubleshooting guide <troubleshooting-guide>` and search the `issue tracker`_ for your error message and problem description.
These methods generally fix or isolate the great majority of install-related difficulties.
Thanks!

.. _issue tracker: https://github.com/spyder-ide/spyder/issues

.. important::

   For most users, our :ref:`install-standalone` are the most straightforward and robust option to obtain Spyder, and support extended functionality over other installation methods.
   Easy installation of third-party Spyder plugins and full Variable Explorer support for custom-installed packages are both currently under active development; if you require these capabilities now, using a :ref:`install-conda` is the currently recommended alternative.


.. _install-binder:

=================
Try Spyder online
=================

Want to try out Spyder before installing it?
With `Binder`_, you can open a functional copy of Spyder online that runs right in your web browser, with no installation needed.
Visit the `Spyder Binder`_ page to get started using Spyder.

.. _Binder: https://mybinder.org/
.. _Spyder Binder: https://mybinder.org/v2/gh/spyder-ide/binder-environments/spyder-stable?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fspyder-ide%252FSpyder-Workshop%26urlpath%3Ddesktop%252F%26branch%3Dmaster

.. image:: /images/installation/installation-spyder-binder.png
   :alt: Spyder running on Binder



.. _install-standalone:

=====================
Standalone installers
=====================

The standalone installers are recommended for most users on Windows, macOS and Linux.
They work like any other IDE, where Spyder can be installed and updated independently of the Python environments you use to run your code.
This avoids the problems with incompatible packages and broken installations users can face when managing Spyder's installation themselves, mixed with their own working environments.

The installers include a built-in Python environment with the most common scientific libraries (e.g. NumPy, SciPy, Pandas, Matpotlib, etc), which can be used out of the box for basic data analysis tasks.
To use additional packages, we currently recommend connecting an external Python distribution (such as `Miniforge`_ (recommended), `Anaconda`_, `Miniconda`_, or `Python.org <Python_>`__) to your standalone copy of Spyder.
For more information on this, see our :ref:`FAQ entry on the subject <using-packages-installer>`.

.. note::

   A built-in plugin manager allowing you to easily install Spyder plugins not already bundled with the installers is being developed for Spyder 6.2.
   For now, if you require third-party plugins, we recommend installing Spyder via a :ref:`install-conda`.


.. _install-standalone-installing:

Downloading and installing
~~~~~~~~~~~~~~~~~~~~~~~~~~

To download the supported Spyder installer for your platform, simply click the appropriate link below; you can also browse all installer versions from the `downloads page`_.
Then, double-click the downloaded file to open the installer on Windows and macOS, or run it with ``bash`` in a terminal on Linux (``bash path/to/downloaded/Spyder-Linux-x86_64.sh``).
If a security warning pops up, you may need to click :guilabel:`Yes`, :guilabel:`OK`, :guilabel:`Open`, :guilabel:`Allow` or similar; or on Windows, :guilabel:`More info` followed by :guilabel:`Run anyway`.

.. rst-class:: installer-table

.. table::

   ================ ================ ================ ================
   `Windows`_       `macOS M1`_      `macOS Intel`_   `Linux`_
   ================ ================ ================ ================

.. _downloads page: https://www.spyder-ide.org/download
.. _Windows: https://github.com/spyder-ide/spyder/releases/latest/download/Spyder-Windows-x86_64.exe
.. _macOS M1: https://github.com/spyder-ide/spyder/releases/latest/download/Spyder-macOS-arm64.pkg
.. _macOS Intel: https://github.com/spyder-ide/spyder/releases/latest/download/Spyder-macOS-x86_64.pkg
.. _Linux: https://github.com/spyder-ide/spyder/releases/latest/download/Spyder-Linux-x86_64.sh


.. _install-standalone-running:

Running from a standalone install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run Spyder when installed standalone, you can simply use your operating system's typical method of launching applications, such as opening it from the :guilabel:`Start` menu on Windows (or the Taskbar, if you've pinned it there), from Launchpad, Spotlight or the :guilabel:`Applications` folder on macOS (or the Dock, if you've added it there), or your preferred application launcher on Linux.


.. _install-standalone-update:

Updating a standalone install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, Spyder checks for updates automatically on startup, and you can also check manually with :menuselection:`Help --> Check for updates`.
Standalone installers for Spyder 6+ include update functionality built right into the application, which after checking for updates will display a prompt to automatically download and install the latest version.
On earlier versions, you'll need to manually download and install the latest release (if on Windows, make sure to remove the old version first from Control Panel/System Settings).



.. _install-conda:

========================
Conda-based distribution
========================

Spyder is included by default in the `Anaconda`_ Python distribution, which comes with everything you need to get started in an all-in-one package.
It can also be easily installed in the much lighter-weight `Miniforge`_ (recommended) or `Miniconda`_, which include just the Conda/Mamba package and environment manager.
They allow you to create your own environments with any packages you need, with Miniforge defaulting to the Conda-Forge channel instead of the commercial Anaconda channel.
This is our recommended installation method if you require third-party Spyder plugins or Variable Explorer compatibility with inspecting objects from specialized libraries (e.g. PyTorch or Scikit-Learn), as support for both of these in our standalone installers is still under active development.

.. _Anaconda: https://www.anaconda.com/products/distribution
.. _Miniconda: https://conda.io/miniconda.html
.. _Miniforge: https://conda-forge.org/download/


.. _install-conda-environment:

Conda environment
~~~~~~~~~~~~~~~~~

To ensure you get the most reliable and up-to-date Spyder version and avoid any conflicts with other packages, we strongly recommend installing Spyder into its own dedicated Conda environment.

.. note::

   If using Mamba, substitute ``mamba`` for ``conda`` in the following commands.


.. _install-conda-installing:

Installing with Conda
---------------------

For a full install of Spyder and all optional dependencies, run the following command in your Anaconda Prompt (Windows) or terminal:

.. code-block:: shell

   conda create -c conda-forge -n spyder-env spyder numpy scipy pandas matplotlib sympy cython

For a minimal install without the optional functionality and integration with the above packages, you can instead run:

.. code-block:: shell

   conda create -c conda-forge -n spyder-env spyder

This installs Spyder into a new environment called ``spyder-env``, using the more up-to-date, non-restricted Conda-Forge channel.
To make sure future installs/updates in this environment also use Conda-Forge and are faster and more reliable, make sure to set it as your environment's default channel with strict channel priority enabled, if this isn't the case already (as it is with Miniforge or if you've manually configured it):

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

After installing, you can run Spyder by the same normal operating system methods :ref:`as with the standalone installers <install-standalone-running>`; just make sure to launch the shortcut with ``(spyder-env)`` in its name.
You can also launch it directly from the Terminal (the Anaconda Prompt, on Windows) by typing ``conda activate spyder-env`` to active its environment and then ``spyder`` to launch it.

See :ref:`our FAQ question <using-existing-environment>` for more information about how to use Spyder with your existing Conda environments.


.. _install-conda-update:

Updating with Conda
-------------------

With any Conda-based distribution and Spyder installed in its own environment (as we strongly recommend), run the following in your system terminal (or Anaconda Prompt if on Windows) to activate the environment and update Spyder:

.. code-block:: shell

   conda activate spyder-env
   conda update -c conda-forge spyder

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

To run the bundled version of Spyder after installing Anaconda, simply launch it like with any other application from your operating system's application launcher (e.g. the Start Menu on Windows, or Spotlight/Launchpad on macOS).

While not recommended, it can also be started from Anaconda Navigator by scrolling to Spyder under :guilabel:`Home` and clicking :guilabel:`Launch`.

.. image:: /images/installation/installation-anaconda-navigator.png
   :alt: Anaconda Navigator showing Spyder

If Spyder does not start via this method or you prefer to use the command line, open your system terminal (Anaconda Prompt on Windows), and type ``conda activate base`` then ``spyder``.


.. _install-anaconda-update:

Updating with Anaconda
----------------------

With Spyder installed in Anaconda's ``base`` environment, first update the ``anaconda`` meta-package, and then Spyder itself.
In your system terminal (or Anaconda Prompt if on Windows), run:

.. code-block:: shell

   conda update anaconda
   conda install spyder=X.Y.Z  # Replace w/latest Spyder version, e.g. 6.1.4

.. note::

   These commands also update all your other packages, which is one reason we strongly recommend you use an isolated conda environment to avoid any potential unintended effects on your environment.

In case you get an error resolving dependencies, try uninstalling Spyder and re-installing it:

.. code-block:: shell

   conda remove spyder
   conda install spyder



.. _install-pip:

=========
Using pip
=========

.. caution::

   While this installation method works fine in most cases, installing Spyder (and other PyData-stack packages) with pip can occasionally lead to tricky issues, particularly if mixed with a Conda install of Python.
   Therefore, we generally recommend our :ref:`install-standalone` or :ref:`installing via Conda <install-conda>` instead.

You can install Spyder with the pip package manager, which is included by default with most Python installations.
Before installing Spyder itself by this method, you need to download a recent version of the `Python`_ programming language if it isn't already installed in your system.

.. _Python: https://www.python.org/

.. note::

   Due to a known issue with some DEB-based Linux distributions (Debian, Ubuntu, Mint), you might also need to install the ``pyqt5-dev-tools`` package first, with ``sudo apt install pyqt5-dev-tools``.

You'll first want to create and activate a virtual environment in which to install Spyder.

.. note::

   There are many environment management tools available; the following examples will use Python's built-in ``venv``.

On macOS/Linux/Unix, run the following in your system terminal:

.. code-block:: shell

   python3 -m venv spyder-env
   source spyder-env/bin/activate

Or on Windows, execute:

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

   While we describe alternative Spyder installation options for users who prefer them, as these are third-party distributions that we have no direct involvement in, we are usually not able to offer useful individual assistance for problems when installing via these alternative methods.

   Furthermore, the Spyder versions they install may be out of date relative to the current release, and thus be missing the latest features and bug fixes.

   Therefore, we recommend you switch to our :ref:`install-standalone` if you encounter installation issues you are unable to solve on your own.


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

   sudo port install py313-spyder


.. _install-linux:

Linux
~~~~~

Spyder can be installed via third-party distro packages on most common Linux distributions.

Launching Spyder installed this way will generally be the same as any other distro-installed application.
Alternatively, it can be launched from the terminal with ``spyder`` (or ``spyder3``, on older versions of some distros).


.. _install-debian:

Ubuntu/Debian
-------------

Spyder is available as `a Ubuntu package`_ and `a Debian package`_.

.. _a Ubuntu package: https://packages.ubuntu.com/search?keywords=spyder
.. _a Debian package: https://packages.debian.org/search?searchon=names&keywords=spyder

It can be installed from your distribution's graphical package manager, or via ``apt`` on the command line:

.. code-block:: shell

   sudo apt update
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
For more information, please see our `Contributing Guide`_, and for further detail consult the `Spyder developer documentation`_.

.. _Contributing Guide: https://github.com/spyder-ide/spyder/blob/master/CONTRIBUTING.md
.. _Spyder developer documentation: https://spyder-ide.github.io/spyder-api-docs/



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

*Need to submit a bug report or feature request?* Check out our `GitHub repository`_.

.. rst-class:: fasb fa-code

*Want development-oriented help and information?* Consult our `developer docs`_.

.. rst-class:: fasb fa-mail-bulk

*Have a help request or discussion topic?* Subscribe to our `Google Group`_.

.. _main website: https://www.spyder-ide.org/
.. _GitHub repository: https://github.com/spyder-ide/spyder/
.. _developer docs: https://spyder-ide.github.io/spyder-api-docs/
.. _Google Group: https://groups.google.com/g/spyderlib
