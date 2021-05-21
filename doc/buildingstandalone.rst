#################################
Building a Standalone Application
#################################

Each new release of Spyder provides :ref:`standalone_installers_ref` for macOS 10.15+ and Windows.
However, we are unable to provide support for older versions of these operating systems.
If you would like to use the standalone application on your older operating system, you may be able to build it locally; however, we do not have the resources to support any issues that you may encounter.

=====
macOS
=====

To build Spyder's standalone application for macOS you need:

* Python 3.x installed, not from Anaconda and not your native Python installation (2.7).
* A local clone of the `Spyder Project`_ repository.
* A virtual environment in which to install the necessary packages

.. _Spyder Project:  https://github.com/spyder-ide/spyder

Once you have the above requirements, you will build the application from within your virtual environment.
The following sections will take you through the entire process

Python 3.x installation
~~~~~~~~~~~~~~~~~~~~~~~

In principle, it doesn't which Python installation you use except it cannot be your native system Python (because it is 2.7) or Anaconda.
The Anaconda installation does not work because its Python libraries are not structured in a way that allows them to be packaged in a macOS application.

We recommend using `Homebrew`_ to install pyenv and pyenv-virtualenv, which will allow you to install whichever Python version you wish.
These instructions assume that you are using ``pyenv`` and ``pyenv-virtualenv``.

.. _Homebrew: http://brew.sh/

Install Homebrew with the following in a Terminal

.. code-block:: bash

   $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

After installing Homebrew, run:

.. code-block:: bash

   $ brew install pyenv, pyenv-virtualenv, xz

``xz`` is a package that provides compression algorithms that Python should be built with to satisfy some packages, namely ``pandas``.

Clone the Spyder Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone Spyder's repository to a local directory. For this example we use ``/Users/rclary/Documents/Python``

.. code-block:: bash

   $ git clone https://github.com/spyder-ide/spyder.git /Users/rclary/Documents/Python

Having a git repository is useful in that it will allow you to pull updates to the code easily, or allow you to checkout certain versions.

Create a Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Python frameworks must be copied to the stand-alone application, so when setting up a virtual environment you must set certain flags.

.. code-block:: bash

   $ export TKPREFIX=$(brew --prefix tcl-tk)
   $ export PYTHON_CONFIGURE_OPTS="--enable-framework --with-tcltk-includes=-I${TKPREFIX}/include --with-tcltk-libs='-L${TKPREFIX}/lib -ltcl8.6 -ltk8.6'"

Now you can install Python. The following installs Python 3.9.4 but you may use whichever version you like (>3.7)

.. code-block:: bash

   $ pyenv install 3.9.4

Next you will create the virtual environment ``spy-build`` (but you can call it whatever you like) and activate it.

.. code-block:: bash

   $ pyenv virtualenv 3.9.4 spy-build
   $ pyenv activate spy-build

Build the Application
~~~~~~~~~~~~~~~~~~~~~

First you must checkout the Spyder version you wish to build.
For this example, we will build Spyder version 5.0.3.
Change your working directory to the Spyder repository and checkout the appropriate version.

.. code-block:: bash

   $ cd /Users/rclary/Documents/Python/spyder
   $ git checkout v5.0.3

Now you will install the build, extras, and scientific packages from requirements files located in the repository.
Spyder's dependencies will be installed by installing Spyder from the source code.
However, Spyder itself will be uninstalled so as not to interfere with the build process.
You should still be in your ``spy-build`` pyenv environment.

.. code-block:: bash

   $ pip install -U pip setuptools
   $ pip install -r installers/macOS/req-build.txt -r installers/macOS/req-extras.txt -r installers/macOS/req-scientific.txt -e .
   $ pip uninstall -q -y spyder

.. note::

   For development purposes, you may wish to build Spyder from an arbitrary commit.
   In this case, you will need to also install the developer versions of ``spyder-kernels``, ``python-language-server``, and ``qdarkstyle`` provided as subrepos to Spyder's repository

   .. code-block:: bash

      $ pip install -e external-deps/spyder-kernels -e external-deps/python-language-server -e external-deps/qdarkstyle

You are now ready to build the standalone application.

.. code-block:: bash

   $ cd installers/macOS
   $ python setup.py

After a whole lot of screen dump, and if everything went well, you should now have the standalone application ``<repo>/installers/macOS/dist/Spyder.app``:


=======
Windows
=======
