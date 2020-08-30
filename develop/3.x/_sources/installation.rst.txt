############
Installation
############

Spyder is relatively easy to install on Windows, Linux and macOS.
Just make sure to read and follow these instructions with care.

This section explains how to install the latest stable release of Spyder.
If you prefer testing the development version, please use the :ref:`boostrap script<install-from-source>` instead.

If you run into problems, before posting a report, *please* consult our comprehensive `Troubleshooting Guide`_ and search the `issue tracker`_ for your error message and problem description, as these methods generally fix or isolate the great majority of install-related complaints.
Thanks!

.. _Troubleshooting Guide: https://github.com/spyder-ide/spyder/wiki/Troubleshooting-Guide-and-FAQ
.. _issue tracker: https://github.com/spyder-ide/spyder/issues


======================================
Installing with Anaconda (recommended)
======================================

Spyder is included by default in the `Anaconda`_
Python distribution, which comes with everything you need to get started in an all-in-one package.

.. _Anaconda: https://www.anaconda.com/download/

This is the easiest way to install Spyder for any of our supported platforms, and the way we recommend to avoid unexpected issues we aren't able to help you with.
If in doubt, you should install via this method; it generally has the least likelihood of potential pitfalls for non-experts, and we may be able to provide limited assistance if you do run into trouble.


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

.. _several versions: https://www.macports.org/ports.php?by=name&substr=spyder

.. attention::

   The MacPorts version of Spyder may currently be raising ``ValueError: unknown locale: UTF-8``, which doesn't let it start correctly.
   To fix it you will have to set these environment variables in your :file:`~/.profile` (or :file:`~/.bashrc`) file manually:

   .. code-block:: bash

      export LANG=en_US.UTF-8
      export LC_ALL=en_US.UTF-8


Install on GNU/Linux
~~~~~~~~~~~~~~~~~~~~

Please refer to the `Requirements`_ to see what other packages you might need.


Ubuntu
------

Using the official package manager:

.. code-block:: bash

   sudo apt-get install spyder3

.. note::

   The `Ubuntu package`_ could be slightly outdated. If you find that is the case, please use the Debian package mentioned below.

.. _Ubuntu package: https://packages.ubuntu.com/search?keywords=spyder3


Debian Unstable
---------------

Using the package manager:

.. code-block:: bash

   sudo apt-get install spyder3

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

Please refer to your distribution's documentation to learn how to install Spyder.


==================================
Installing with pip (experts only)
==================================

.. warning::

   While this installation method is a viable option for experienced users, installing Spyder (and other SciPy stack packages) with ``pip`` can lead to a number of tricky issues.
   While you are welcome to try this on your own, we unfortunately do not have the resources to help you if you do run into problems, except to recommend you use Anaconda instead.


Requirements
~~~~~~~~~~~~

The requirements to run Spyder are:

* `Python <https://www.python.org/>`_ 2.7 or >=3.3

* `PyQt5 <https://www.riverbankcomputing.com/software/pyqt/download5>`_ >=5.5

* `Qtconsole <https://github.com/jupyter/qtconsole>`_ >=4.2.0 -- for an enhanced Python interpreter.

* `Rope <https://github.com/python-rope/rope>`_ >=0.9.4 and `Jedi <https://github.com/davidhalter/jedi>`_ >=0.9.0 -- for code completion, go-to-definition and calltips in the Editor.

* `Pyflakes <https://github.com/PyCQA/pyflakes>`_  -- for real-time code analysis.

* `Sphinx <http://www.sphinx-doc.org/en/master/>`_ -- for the Help pane rich text mode and to get our documentation.

* `Pygments <http://pygments.org/>`_ >=2.0 -- for syntax highlighting and code completion in the Editor of all file types it supports.

* `Pylint <https://www.pylint.org/>`_  -- for static code analysis.

* `Pycodestyle <https://github.com/PyCQA/pycodestyle>`_ -- for style analysis.

* `Psutil <https://github.com/giampaolo/psutil>`_  -- for memory/CPU usage in the status bar.

* `Nbconvert <https://github.com/jupyter/nbconvert>`_ -- to manipulate Jupyter notebooks on the Editor.

* `Qtawesome <https://github.com/spyder-ide/qtawesome>`_ >=0.4.1 -- for an icon theme based on FontAwesome.

* `Pickleshare <https://github.com/pickleshare/pickleshare>`_ -- To show import completions in the Editor and Consoles.

* `PyZMQ <https://github.com/zeromq/pyzmq>`_ -- To run introspection services in the Editor asynchronously.

* `QtPy <https://github.com/spyder-ide/qtpy>`_ >=1.2.0 -- To run Spyder with different Qt bindings seamlessly.

* `Chardet <https://github.com/chardet/chardet>`_ >=2.0.0-- Character encoding auto-detection in the Editor.

* `Numpydoc <https://github.com/numpy/numpydoc>`_ Used by Jedi to get return types for functions with Numpydoc docstrings.

* `Cloudpickle <https://github.com/cloudpipe/cloudpickle>`_ Serialize variables in the IPython kernel to send them to Spyder.


Optional modules
~~~~~~~~~~~~~~~~

* `Matplotlib <https://matplotlib.org/>`_ >=1.0 -- for 2D and 3D plotting in the consoles.

* `Pandas <https://pandas.pydata.org/>`_ >=0.13.1 -- for viewing and editing Series and DataFrames in the Variable Explorer.

* `Numpy <https://www.numpy.org/>`_ -- for viewing and editing two or three dimensional arrays in the Variable Explorer.

* `Sympy <https://www.sympy.org/en/index.html>`_ >=0.7.3 -- for working with symbolic mathematics in the IPython console.

* `Scipy <https://www.scipy.org/>`_ -- for importing Matlab workspace files in the Variable Explorer.

* `Cython <http://cython.org/>`_ >=0.21 -- to run Cython files or Python files that depend on Cython libraries in the IPython console.


Installation procedure
~~~~~~~~~~~~~~~~~~~~~~

You can install Spyder with the ``pip`` package manager, which comes by default with most Python installations.
Before installing Spyder itself by this method, you need to acquire the `Python`_ programming language.

.. _Python: https://www.python.org/

Then, to install Spyder and its other dependencies, run ``pip install spyder``.
You may need to install a Qt binding (PyQt5) separately with ``pip`` if running under Python 2.


Run without installing
~~~~~~~~~~~~~~~~~~~~~~

You can execute Spyder from source without installing it first by the following procedure:

#. Unzip the source package available for download on the `Spyder Github repository`_ (or :ref:`clone it from Github<install-from-source>`)
#. Change current directory to the unzipped directory
#. Install Spyder's requirements with:

   .. code-block:: bash

      pip install -r requirements/requirements.txt

#. Run Spyder with the command:

   .. code-block:: bash

      python bootstrap.py

.. _Spyder Github repository: https://github.com/spyder-ide/spyder

This is especially useful for beta-testing, troubleshooting and helping develop Spyder itself.


===============
Updating Spyder
===============

If you installed Spyder through Anaconda (recommended), WinPython, MacPorts, or your system package manager, update using those same methods.
With Anaconda, just run (in Anaconda Prompt if on Windows) ``conda update anaconda`` to update the distribution as a whole and ``conda update spyder`` to update Spyder specifically.

If you installed Spyder via the advanced/cross-platform method, ``pip``, run ``pip install --upgrade spyder``.
This command will also update all Spyder dependencies, so we recommend you use an isolated ``virtualenv`` or ``venv`` environment to avoid any potential unintended effects on other installed packages.


.. _install-from-source:


==============================
Installing a development build
==============================

If you want to try the next Spyder version before it is released, you can!
You may want to do this for fixing bugs in Spyder, adding new features, learning how Spyder works or just getting a taste of what the IDE can do.
For more information, please see the `CONTRIBUTING.md document`_ included with the Spyder source or on Github, and for further detail consult the `Spyder development wiki`_.

.. _CONTRIBUTING.md document: https://github.com/spyder-ide/spyder/blob/master/CONTRIBUTING.md
.. _Spyder development wiki: https://github.com/spyder-ide/spyder/wiki

In summary:

#. Install the Spyder `requirements`_.

   The recommended and easiest way to do this is with ``conda`` (although experts may prefer ``pip``). In a fresh environment (``conda create -n your-name-here -c conda-forge python=3``, then ``activate`` it), run the following:

   .. code-block:: bash

      conda install -c conda-forge/label/beta spyder=4.0.0b1
      conda install -c conda-forge python-language-server
      conda remove spyder

   This installs all of Spyder's dependencies into the environment along with the stable/packaged version of Spyder, and then removes Spyder itself.

   .. note::

      Following the separation in v3.3 of Spyder's console code into its own package, ``spyder-kernels``, you'll need to have the corresponding version of it available—``0.x`` for Spyder 3 (``3.x`` branch), and ``1.x`` for Spyder 4 (``master`` branch).
      The above procedure will install the ``0.x`` version; to test the ``master`` branch (Spyder 4), you'll need to install the corresponding ``1.x`` version of ``spyder-kernels``.
      This can be done via two methods: installing the ``1.x`` version via ``conda``:

      .. code-block:: bash

         conda install -c spyder-ide spyder-kernels=1.*

      or ``pip``:

      .. code-block:: bash

         pip install spyder-kernels==1.*

      (and using the same respective command, replacing ``1`` with ``0``, to switch back to the Spyder 3 version), or by ``clone``-ing the `spyder-kernels git repository`_ to somewhere on your path and checking out the appropriate branch (``0.x`` or ``master``) corresponding to the version of Spyder (3 or 4) you would like to run, and running the commend ``pip install -e`` at the root.
      For any non-trivial development work, keeping two separate virtual environments (with ``conda-env`` or ``venv``) for Spyder 3 and 4 makes this process much quicker and less tedious.

#. Install `Git`_, a powerful source control management tool.

#. Clone the Spyder source code repository with the command:

   .. code-block:: bash

      git clone https://github.com/spyder-ide/spyder.git

#. Run Spyder with the :file:`bootstrap.py` script from within the cloned :file:`spyder/` directory:

   .. code-block:: bash

      python bootstrap.py

#. To keep your repository up-to-date, run ``git pull`` inside the cloned directory.

.. _spyder-kernels git repository: https://github.com/spyder-ide/spyder-kernels
.. _Git: https://git-scm.com/downloads


===============
Additional help
===============

* For a comprehensive guide to spyder troubleshooting, including installation issues, read our `Troubleshooting Guide and FAQ`_.
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
