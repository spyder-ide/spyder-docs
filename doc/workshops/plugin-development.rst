##############################
Plugin Development with Spyder
##############################



============
Introduction
============

This workshop consists of a review of the features and possibilities of the API
offered by Spyder 5, the recently released version of our favorite IDE for
scientific python, to develop plugins to extend its functionality. As a
practical exercise, we will develop a pair of simple plugins that incorporate a
configurable pomodoro timer in the status bar and a task manager as a dockable
widget.


Spyder for developers
~~~~~~~~~~~~~~~~~~~~~

The best place to understand the process and technologies that make up spyder is
its Github repository, in particular the `contribution guide`_.

The core of **Spyder** is *spyder-ide*, a desktop application developed in *Qt*,
which requires for its operation two packages with it is closely related (and
without which it cannot work): *spyder-kernels* and *spyder-lsp-server*.

**Qt** is a multiplatform widget toolkit for creating native graphical user
interfaces. Qt is a very complete development framework that offers utilities
for building applications, and libraries of extensions for Networking,
Bluetooth, Charts, 3D rendering, Navigation (as GPS), among others.

Spyder uses **qtpy** which is an abstraction layer that allows you to work with
Qt from Python regardless of whether you use either of the two reference
libraries: PyQt or PySide.

**spyder-kernels** provide Jupyter kernels to Spyder for use within its
consoles.

**spyder-lsp-server** is a python implementation of Microsoft's Language Server
Protocol that connects with an Editor to provide features as auto complete, go
to definition, find all references, etc.

These three packages have been developed entirely by the Spyder team,
consolidating a huge effort over the years, and a way to secure Spyder's future
by making it a robust and versatile tool.

In turn, spyder-ide is currently developed in such a way that most of its
features are implemented as extensions or plugins to allow third-party
developers to extend its functionality. In this workshop we will focus on the
development of spyder-ide plugins.

.. _contribution guide: https://github.com/spyder-ide/spyder/blob/master/CONTRIBUTING.md



================================
Set up a development environment
================================

TODO It is included here so that those taking the workshop do not have to wait
so long to start the actual hands-on work. The following concepts can be
reviewed while the packages are being installed.


===================
Basic Qt Components
===================

To develop an application we’ll add widgets, arrange them using layouts and
connect these widgets to functions, allowing to trigger behavior from user
interaction. We now define these concepts as follows.

Each type of Qt component is a class starting with the letter ``Q`` followed by
a name related to its functionality.

The core component of Qt is the ``QApplication`` class. Every Qt application
needs a single instance of this class as the base, from where the Qt *event
loop* is controlled. Spyder itself is an instance of ``QApplication``, its
starting point is in the following two lines of code:

.. code:: python

   QMainWindow.__init__(self)
   qapp = QApplication.instance()

``QMainWindow`` is a pre-built widget that provides many standard window
features as toolbars, menus, a status bar, dockable widgets and more, which
serves as the basis for the application.


Signals & Slots
~~~~~~~~~~~~~~~

**Signals** are notifications emitted by widgets when something happens. That
something can be any number of things, from pressing a button, to changing text
in an input box, to changing text in the window. Many signals are initiated by
user action, but this is not a rule.

**Slots** are signal receivers. Functions or methods could be used as slots, by
connecting a signal to them. If a signal sends data, the receiver callable will
also receive it. Many Qt widgets also have their own built-in slots, so the
corresponding widgets are notified automatically.


Widgets
~~~~~~~

In computer science a *Widget* is a shortened form of “window gadget”. A widget
is an element of interaction, such as a button, or a container for other
widgets, as panels or tabs. The ``QWidget class`` is the base class of all user
interface elements, it receives events from the window system, and paints its
representation on the screen.


Layouts
~~~~~~~

Interfaces are built by embedding widgets inside widgets, and since they are
visual components they are visually organized by means of *layouts*.

There are 4 basic layouts available in Qt: ``QHBoxLayout``, ``QVBoxLayout``,
``QGridLayout``, and ``QStackedLayout``. They are used depending on whether you
need to organize widgets in a horizontal, vertical, grid or stacked manner
respectively.


Actions, Toolbars & Menus
~~~~~~~~~~~~~~~~~~~~~~~~~

User interfaces of desktop applications usually use *toolbars* and *menus*.
Since these are alternative ways to access the same functionality, Qt provides
*actions* as a way to avoid duplication of functions. Thus, each time a menu
option or a toolbar button gives access to the same function, they point to the
same action.


Dialogs
~~~~~~~

A *Dialog* is a GUI component that communicates with the user. Dialogs are
commonly used for functions that do not fit into the main interface. In Qt, by
design they are modal (or blocking) windows that show in front of the main
Window until they are dismissed.

Qt provides some *special* dialogs for the most common use-cases as file
Open/Save, font selection, error messages, color choosing, printing, among
others.


Windows
~~~~~~~

If an application requires additional windows that do not block the main window,
these are generated as non-parent ``QWidget`` instances. These are used for
tasks that happen in parallel over long-running processes such as displaying
graphs or document editing.


Events
~~~~~~

An *Event* denote every interaction the user has with a Qt application. There
are several types of events designed to address different types of interactions.
In Qt they are represented by objects that contain information about what
prompted them, and are passed to specific handlers that are responsible for
triggering further actions.



===================
Create a repository
===================

TODO Check what can be reused from previous workshops.


=========================================
Types of plugins we can develop in Spyder
=========================================


Dockable plugin
~~~~~~~~~~~~~~~

TODO

Spyder V2 plugin, (non dockable)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO

Some Spyder-IDE plugins
~~~~~~~~~~~~~~~~~~~~~~~

TODO Examples of current Spyder plugins are listed here, specifying which ones are of
each type.

================
A Pomodoro Timer
================

The Pomodoro Technique designed by Francesco Cirillo is a time management
practice used to increase your focus and productivity when trying to complete
assignments or meet deadlines. Choosing to use a Pomodoro Timer can help to give
a task your full, undivided attention.

The typical process of the Pomodoro Technique consists of the following six
steps:

1. Choose a task to be done.
2. Set the Pomodoro Timer (default is 25 minutes).
3. Work only on that task until the timer ends.
4. When the timer rings, put a checkmark on a piece of paper, this is called "a
   pomodoro".
5. If you have less than 3 checkmarks take a short break (by default, 5
   minutes), and return to step 2.
6. When you have completed four Pomodoro cycles, you deserve a longer break (our
   default is 15 minutes). Checkmarks are reset to zero, go back to step 1.

Implementation
~~~~~~~~~~~~~~

* How to use PyQt, Spyder modules and widget classes for creating graphical
  components inside Spyder.
* The layout management classes, including QHBoxLayout and QVBoxLayout
* The use of container classes for organizing groups of widgets
* PyQt’s signal and slot mechanism for event handling
* The QTimer class and event loops
* Using other Qt classes such as Qt and QIcon

Features
~~~~~~~~

* Pomodoro Timer

  - State: Pomodoro, short-break, long-break -> change color or other properties.
  - Interactions: Start, Stop, reset -> QPushButtons

* Tasks Logger

  - Input: Text with the current task -> QLabel and  QLineEdit
  - Counter: Number of pomodoros completed.

* Message or sound

  - Dialog: If four pomodoros are completed, a message will be displayed urging
    the user to take a break.



=================
Let's get started
=================

We already have a repository an a virtual environment where Spyder 5 is installed.


Create an initial structure of our plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ cookiecutter https://github.com/spyder-ide/spyder5-plugin-cookiecutter
   You\'ve downloaded /home/mapologo/.cookiecutters/spyder5-plugin-cookiecutter before. Is it okay to delete and re-download it? [yes]:
   full_name [Spyder Bot]: Francisco Palm # It's your name, better John Doe
   email [spyder.python@gmail.com]: fpalm@qu4nt.com
   github_username [spyder-bot]: map0logo
   github_org [spyder-ide]:
   project_name [Spyder Boilerplate]: Spyder Pomodoro Timer
   project_short_description [Boilerplate needed to create a Spyder Plugin.]: A very simple pomodoro timer that shows in the status bar.
   project_pypi_name [spyder-pomodoro-timer]:
   project_package_name [spyder_pomodoro_timer]:
   pypi_username [map0logo]:
   Select plugin_type:
   1 - Spyder Dockable Plugin
   2 - Spyder Plugin
   Choose from 1, 2 [1]: 2
   Select open_source_license:
   1 - MIT license
   2 - BSD license
   3 - ISC license
   4 - Apache Software License 2.0
   5 - GNU General Public License v3
   6 - Not open source
   Choose from 1, 2, 3, 4, 5, 6 [1]: 1


The plugin structure
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   .
   ├── [Some info files]
   ├── Makefile
   ├── setup.py
   ├── spyder_pomodoro_timer
   │   ├── __init__.py
   │   └── spyder
   │       ├── __init__.py
   │       ├── api.py
   │       ├── confpage.py
   │       ├── container.py
   │       ├── locale
   │       │   └── spyder_pomodoro_timer.pot
   │       ├── plugin.py
   │       └── widgets.py
   └── tests


The root folder
~~~~~~~~~~~~~~~

* The Makefile has several useful commands:

.. code-block:: bash

   clean                remove all build, test, coverage and Python artifacts
   clean-build          remove build artifacts
   clean-pyc            remove Python file artifacts
   clean-test           remove test and coverage artifacts
   test                 run tests quickly with the default Python
   docs                 generate Sphinx HTML documentation, including API docs
   servedocs            compile the docs watching for changes
   release              package and upload a release
   dist                 builds source and wheel package
   install              install the package to the active Python's site-packages
   develop              install the package to the active Python's site-packages

.. note::
   ``install`` and ``develop`` commands use ``setup.py install`` and ``setup.py
   develop`` respectively. But, it is better to use ``pip install .`` and ``pip
   install -e .`` to install packages, since ``setup.py`` may give dependency
   problems, or will make the package incompatible with pip.

* ``setup.py`` helps you to package and distribute your plugin with Distutils,
  which is the standard for distributing Python Modules. On this file the
  ``entry_points`` parameter of ``setup`` is quite important, as it is the one
  that allows Spyder to identify this package as a plugin, and to know how to
  access its functionalities.


The spyder folder
~~~~~~~~~~~~~~~~~

The ``spyder-pomodoro-timer` folder has the name you introduced when running
cookie-cutter, and inside this we have a folder denominated ``spyder`` that is
where we must organize the code of our plugin.

So, its files define your plugin as follows:

* ``api.py``: where the functionality of the plugin is exposed to the rest of
  spyder (which would allow additional functionality to be added from other
  plugins).

* ``plugin.py``: is the core of the plugin, depending on the type of plugin
  we create here an instance of ``SpyderDockablePlugin`` or
  ``SpyderPluginV2``.

  * If it is a ``SpyderPluginV2`` you should set a field named
    ``CONTAINER_CLASS`` with an instance of ``PluginMainContainer``.
  * If it is a ``SpyderDockablePlugin`` you should set a field named
    ``WIDGET_CLASS`` with an instance of ``PluginMainWidget`` (that internally
    it is assigned to ``CONTAINER_CLASS``).

* ``container.py``: only used for ``SpyderPluginV2`` plugins, in this file we
  create the instance of ``PluginMainContainer`` that we are going to assign to
  the base class of our plugin.

* ``widgets.py``: in this file is where the graphical components of our plugin
  are written, if it is of type ``SpyderPluginV2`` and it does not have elements
  in the interface it is not necessary. In this file we create the instance of
  ``PluginMainWidget`` that we are going to assign to the base class of our
  ``SpyderDockablePlugin`` plugin, or to our instance of ``PluginMainContainer``
  in case our plugin is of type ``SpyderPluginV2``.

* ``confpage.py``: this is where you specify the forms that will be displayed
  in Tools > Preferences so that the user can adjust the configurable
  parameters of our plugin.



=========================
Building our first plugin
=========================

TODO Initial basic version of the plugin



======================
How to test our plugin
======================

TODO Instructions to install it in development mode



====================
Enhancing our plugin
====================

TODO Enhanced version of the plugin



======================
Publishing your plugin
======================

TODO
