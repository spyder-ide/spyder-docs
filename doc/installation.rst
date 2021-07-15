##################
Installation Guide
##################

Spyder is relatively easy to install on Windows, Linux and macOS.
Just make sure to read and follow these instructions with care.

If you run into problems, before posting a report, *please* consult our comprehensive :doc:`troubleshooting guide</troubleshooting/first-steps>` and search the `issue tracker`_ for your error message and problem description.
These methods generally fix or isolate the great majority of install-related difficulties.
Thanks!

.. _issue tracker: https://github.com/spyder-ide/spyder/issues

.. important::

   Spyder now offers :ref:`standalone_installers_ref` for Windows and macOS, making it easier to get up and running with the application without having to download Anaconda or manually install it in your existing environment.
   While we still support Anaconda, we recommend this install method on those platforms to avoid most problems with package conflicts and other issues.



=================
Try Spyder online
=================

Want to try out Spyder without installing it?
With `Binder`_ you can work with a fully functional copy of Spyder online that runs right in your web browser, no installation needed.
Just visit the `Spyder page on Binder`_ to get started using Spyder now.

.. _Binder: https://mybinder.org/
.. _Spyder page on Binder: https://mybinder.org/v2/gh/spyder-ide/spyder/5.x?urlpath=/desktop

.. image:: /images/installation/installation-spyder-binder.png
   :alt: Spyder running on Binder



.. _standalone_installers_ref:

=====================
Standalone installers
=====================

Our standalone installers for Windows and macOS are available from Spyder 4.2 onwards.
We recommend using this installation method on those platforms, but we offer several other options for Linux, advanced users and specific needs, so keep reading if that's the case for you.

.. rst-class:: installer-table

.. table::

   ========================================== ==========================================
   `Windows Installer`_                       `macOS Installer`_
   ========================================== ==========================================

.. _Windows Installer: https://github.com/spyder-ide/spyder/releases/latest/download/Spyder_64bit_full.exe
.. _macOS Installer: https://github.com/spyder-ide/spyder/releases/latest/download/Spyder.dmg



==============
Using Anaconda
==============

Spyder is included by default in the `Anaconda`_ Python distribution, which comes with everything you need to get started in an all-in-one package, and is our recommended installation method on Linux (and supported on the other platforms too).

.. _Anaconda: https://www.anaconda.com/products/individual


Running with Anaconda
~~~~~~~~~~~~~~~~~~~~~

To run Spyder after installing it with Anaconda, the recommended method on Windows is to launch it via the Start menu shortcut.
On other platforms, open Anaconda Navigator, scroll to Spyder under ``Home``, and click ``Launch``.

.. image:: /images/installation/installation-anaconda-navigator.png
   :alt: Anaconda Navigator showing Spyder

If Spyder does not launch via this method or you prefer to use the command line, open Anaconda Prompt (Windows) or your terminal (other platforms), type ``conda activate base`` then ``spyder``.


New Conda environment
~~~~~~~~~~~~~~~~~~~~~

If you would like to have Spyder in a dedicated environment to update it separately from your other packages and avoid any conflicts, you can.
Just run the following command in your Anaconda Prompt (Windows) or terminal (other platforms), for a minimal install of Spyder into a new environment called ``spyder-env``:

.. code-block:: bash

   conda create -n spyder-env spyder=4

To install Spyder's optional dependencies as well for full functionality, use the following command instead:

.. code-block:: bash

   conda create -n spyder-env spyder=4 numpy scipy pandas matplotlib sympy cython

To install Spyder from Conda-Forge instead of the default Anaconda channel, add ``-c conda-forge`` at the end of either of the previous commands.

You can then run Spyder by the same methods as above, except make sure to select the start menu shortcut with ``(spyder-env)`` in the name, select the ``spyder-env`` environment on the left before launching it with Navigator, or type ``conda activate spyder-env`` before launching it on the command line.

.. image:: /images/installation/installation-conda-install.gif
   :alt: Running Spyder installation with conda

For more information on this approach, and using Spyder with your existing Python environments and packages, please see our `Guide to working with packages and environments in Spyder`_.

.. _Guide to working with packages and environments in Spyder: https://github.com/spyder-ide/spyder/wiki/Working-with-packages-and-environments-in-Spyder



===================
Alternative methods
===================

.. caution::

   While we offer alternative Spyder installation options for users who desire them, we currently lack the resources to offer individual assistance for problems specific to installing via these alternative distributions.
   Therefore, we recommend you switch to Anaconda if you encounter installation issues you are unable to solve on your own.


Windows
~~~~~~~

Spyder is also included in the `WinPython`_ scientific Python distribution, although it doesn't include Anaconda's convenient ``conda`` package and environment manager like Anaconda.
You can use it immediately after installing, just like with Anaconda.

.. _WinPython: https://winpython.github.io/


macOS
~~~~~

Thanks to the `MacPorts project`_, Spyder can be installed using its ``port`` package manager; however, the included Spyder version may be out of date or have MacPorts-specific issues outside of Spyder's control.

.. _MacPorts project: https://www.macports.org/

There are `several versions`_ available from which you can choose.

.. _several versions: https://ports.macports.org/?search=spyder&search_by=name


Linux
~~~~~

Ubuntu
------

Using the official package manager:

.. code-block:: bash

   sudo apt install spyder3

.. note::

   The `Ubuntu package`_ is often outdated.
   If you find that is the case, please use the Debian package mentioned below, although it may also be out of date.

.. _Ubuntu package: https://packages.ubuntu.com/search?keywords=spyder3


Debian Unstable
---------------

Using the package manager:

.. code-block:: bash

   sudo apt install spyder3

Spyder's official Debian package is available on the `Debian package repository`_.

.. _Debian package repository: https://packages.debian.org/unstable/spyder3


Other distributions
-------------------

Spyder is also available in other GNU/Linux distributions, like

* `Arch Linux`_
* `Fedora`_
* `Gentoo`_
* `openSUSE`_

.. _Arch Linux: https://aur.archlinux.org/packages/spyder-git/
.. _Fedora: https://fedoraproject.org/wiki/Spyder
.. _Gentoo: https://packages.gentoo.org/packages/dev-python/spyder
.. _openSUSE: https://software.opensuse.org/package/spyder

Please refer to your distribution's documentation for how to install Spyder.


Running on Linux
~~~~~~~~~~~~~~~~

How to launch Spyder after installation varies depending on your OS and install method, but with those featured here, it will generally be the same as for any other installed application.
Alternately, you should be able to launch it from the terminal/command line with ``spyder`` or ``spyder3``.



=========
Using pip
=========

.. warning::

   While this installation method is a viable option for experienced users, installing Spyder (and other PyData-stack packages) with ``pip`` can lead to a number of tricky issues.
   While you are welcome to try this on your own, we unfortunately do not have the resources to help you if you do run into problems, except to recommend you use Anaconda instead.

You can install Spyder with the ``pip`` package manager, which comes by default with most Python installations.
Before installing Spyder itself by this method, you need to acquire the `Python`_ programming language.

.. _Python: https://www.python.org/

You'll first want to create and activate a virtual environment in which to install Spyder, via one of the following methods.

With ``virtualenvwrapper``:

.. code-block:: bash

   mkvirtualenv spyder-env
   workon spyder-env

Otherwise, on macOS/Linux/Unix:

.. code-block:: bash

   python3 -m venv spyder-env
   source spyder-env/bin/activate

or on Windows:

.. code-block:: bash

   python -m venv spyder-env
   spyder-env/Scripts/activate.bat

After activating your environment, to install Spyder and its other dependencies, run ``pip install spyder``.

.. image:: /images/installation/installation-pip-install.gif
   :alt: Running Spyder installation with pip

You may need to install a Qt binding (PyQt5) separately with ``pip`` if running under Python 2.

To launch Spyder after installing, ensure your environment is activated and run the ``spyder3`` command.



===============
Updating Spyder
===============

If you installed Spyder through Anaconda (recommended), WinPython, MacPorts, or your system package manager, update using those same methods.
With Anaconda, just run (in Anaconda Prompt if on Windows, otherwise in your system terminal):

.. code-block:: bash

   conda update anaconda
   conda update spyder

If you installed Spyder via the advanced/cross-platform method, ``pip``, run ``pip install --upgrade spyder``.
This command will also update all Spyder dependencies, so we recommend you use an isolated virtual environment to avoid any potential unintended effects on other installed packages.



==================
Development builds
==================

If you want to try the next Spyder version before it is released, you can!
You may want to do this for fixing bugs in Spyder, adding new features, learning how Spyder works or just getting a taste of what the IDE can do.
For more information, please see the `Contributing Guide`_ included with the Spyder source or on Github, and for further detail consult the `Spyder development wiki`_.

.. _Contributing Guide: https://github.com/spyder-ide/spyder/blob/master/CONTRIBUTING.md
.. _Spyder development wiki: https://github.com/spyder-ide/spyder/wiki



.. rst-class:: blue-32px

===============
Additional help
===============

.. rst-class:: fasb fa-first-aid

*Run in to a problem installing or running Spyder?* Read our `Troubleshooting Guide and FAQ`_.

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

.. _Troubleshooting Guide and FAQ: https://github.com/spyder-ide/spyder/wiki/Troubleshooting-Guide-and-FAQ
.. _main website: https://www.spyder-ide.org/
.. _Github repository: https://github.com/spyder-ide/spyder/
.. _Github wiki: https://github.com/spyder-ide/spyder/wiki
.. _Google Group: https://groups.google.com/group/spyderlib
.. _Gitter chatroom: https://gitter.im/spyder-ide/public
