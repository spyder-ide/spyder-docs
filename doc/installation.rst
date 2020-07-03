##################
Installation Guide
##################

Spyder is relatively easy to install on Windows, Linux and macOS.
Just make sure to read and follow these instructions with care.

If you run into problems, before posting a report, *please* consult our comprehensive `Troubleshooting Guide`_ and search the `issue tracker`_ for your error message and problem description, as these methods generally fix or isolate the great majority of install-related complaints.
Thanks!

.. _Troubleshooting Guide: https://github.com/spyder-ide/spyder/wiki/Troubleshooting-Guide-and-FAQ
.. _issue tracker: https://github.com/spyder-ide/spyder/issues



======================================
Installing with Anaconda (recommended)
======================================

Spyder is included by default in the `Anaconda`_
Python distribution, which comes with everything you need to get started in an all-in-one package.

.. _Anaconda: https://www.anaconda.com/products/individual

This is the easiest way to install Spyder for any of our supported platforms, and the way we recommend to avoid unexpected issues we aren't able to help you with.
If in doubt, you should install via this method; it generally has the least likelihood of potential pitfalls for non-experts, and we may be able to provide limited assistance if you do run into trouble.

To run Spyder after installing it with Anaconda, the recommended method on Windows is to launch it via the Start menu shortcut.
On other platforms, open Anaconda Navigator, scroll to Spyder under ``Home``, and click ``Launch``.
If Spyder does not launch via this method or you prefer to use the command line, open Anaconda Prompt (Windows) or your terminal (other platforms), type ``conda activate base`` then ``spyder``.



===========================================
Installing with an alternative distribution
===========================================

.. caution::

   While we offer alternative Spyder installation options for users who desire them, we currently lack the resources to offer individual assistance for problems specific to installing via these alternative distributions.
   Therefore, we recommend you switch to Anaconda if you encounter installation issues you are unable to solve on your own.


Install on Windows
~~~~~~~~~~~~~~~~~~

Spyder is also included in the `WinPython`_ scientific Python distribution, although it doesn't include Anaconda's convenient ``conda`` package and environment manager like Anaconda.
You can use it immediately after installing, just like with Anaconda.

.. _WinPython: https://winpython.github.io/


Install on macOS
~~~~~~~~~~~~~~~~

Thanks to the `MacPorts project`_, Spyder can be installed using its ``port`` package manager; however, the included Spyder version may be out of date or have MacPorts-specific issues outside of Spyder's control.

.. _MacPorts project: https://www.macports.org/

There are `several versions`_ available from which you can choose.

.. _several versions: https://ports.macports.org/?search=spyder&search_by=name

.. attention::

   The MacPorts version of Spyder may currently be raising ``ValueError: unknown locale: UTF-8``, which doesn't let it start correctly.
   To fix it you will have to set these environment variables in your :file:`~/.profile` (or :file:`~/.bashrc`) file manually:

   .. code-block:: bash

      export LANG=en_US.UTF-8
      export LC_ALL=en_US.UTF-8


Install on GNU/Linux
~~~~~~~~~~~~~~~~~~~~

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


Other Distributions
-------------------

Spyder is also available in other GNU/Linux distributions, like

* `Arch Linux`_
* `Fedora`_
* `Gentoo`_
* `openSUSE`_

.. _Arch Linux: https://aur.archlinux.org/packages/spyder3-git/
.. _Fedora: https://fedoraproject.org/wiki/Spyder
.. _Gentoo: https://packages.gentoo.org/packages/dev-python/spyder
.. _openSUSE: https://software.opensuse.org/package/spyder3

Please refer to your distribution's documentation for how to install Spyder.


Running Spyder
--------------

How to launch Spyder after installation varies depending on your OS and install method, but with those featured here, it will generally be the same as for any other installed application.
Alternately, you should be able to launch it from the terminal/command line with `spyder`.



==================================
Installing with pip (experts only)
==================================

.. warning::

   While this installation method is a viable option for experienced users, installing Spyder (and other PyData-stack packages) with ``pip`` can lead to a number of tricky issues.
   While you are welcome to try this on your own, we unfortunately do not have the resources to help you if you do run into problems, except to recommend you use Anaconda instead.

You can install Spyder with the ``pip`` package manager, which comes by default with most Python installations.
Before installing Spyder itself by this method, you need to acquire the `Python`_ programming language.

.. _Python: https://www.python.org/

You'll want to create a virtual environment in which to install Spyder with `mkvirtualenv spyder-env` or `python3 -m venv spyder-env` then activate it with `workon spyder-env` or `source spyder-env/bin/activate`.
To install Spyder and its other dependencies, run ``pip install spyder``.
You may need to install a Qt binding (PyQt5) separately with ``pip`` if running under Python 2.

To launch Spyder after installing, ensure your environment is activated and run the `spyder` command.



===============
Updating Spyder
===============

If you installed Spyder through Anaconda (recommended), WinPython, MacPorts, or your system package manager, update using those same methods.
With Anaconda, just run (in Anaconda Prompt if on Windows) ``conda update anaconda`` to update the distribution as a whole and ``conda update spyder`` to update Spyder specifically.

If you installed Spyder via the advanced/cross-platform method, ``pip``, run ``pip install --upgrade spyder``.
This command will also update all Spyder dependencies, so we recommend you use an isolated ``venv`` environment to avoid any potential unintended effects on other installed packages.



==============================
Installing a development build
==============================

If you want to try the next Spyder version before it is released, you can!
You may want to do this for fixing bugs in Spyder, adding new features, learning how Spyder works or just getting a taste of what the IDE can do.
For more information, please see the `CONTRIBUTING.md document`_ included with the Spyder source or on Github, and for further detail consult the `Spyder development wiki`_.

.. _CONTRIBUTING.md document: https://github.com/spyder-ide/spyder/blob/master/CONTRIBUTING.md
.. _Spyder development wiki: https://github.com/spyder-ide/spyder/wiki



===============
Additional help
===============

* For a comprehensive guide to Spyder troubleshooting, including installation issues, read our `Troubleshooting Guide and FAQ`_.
* For general information about Spyder and its ecosystem, see our `main website`_.
* For bug reports and feature requests, check out our `Github repository`_.
* For development-oriented help and information, consult our `Github wiki`_.
* For discussions and help requests, you can subscribe to our `Google Group`_.
* For quick questions and to chat with the dev team, stop by our `Gitter chatroom`_.

.. _Troubleshooting Guide and FAQ: https://github.com/spyder-ide/spyder/wiki/Troubleshooting-Guide-and-FAQ
.. _main website: https://www.spyder-ide.org/
.. _Github repository: https://github.com/spyder-ide/spyder/
.. _Github wiki: https://github.com/spyder-ide/spyder/wiki
.. _Google Group: https://groups.google.com/group/spyderlib
.. _Gitter chatroom: https://gitter.im/spyder-ide/public
