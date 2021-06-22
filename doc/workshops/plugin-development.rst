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

**Qt** is a multiplatform widget toolkit for creating graphical user interfaces,
a native application with native capabilities and speed. Qt is a very complete
development framework that offers utilities for building applications, and
libraries of extensions for Networking, Bluetooth, Charts, 3D rendering,
Navigation (as GPS), among others.

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



================================
Set up a development environment
================================



===================
Create a repository
===================



======================
Publishing your plugin
======================
