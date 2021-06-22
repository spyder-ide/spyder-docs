.. _qt-fundamentals:

###############
Qt Fundamentals
###############



**Qt** is a multiplatform widget toolkit for creating native graphical user interfaces. Qt is also a very complete development framework that offers utilities for building applications, and libraries of extensions for Networking, Bluetooth, Charts, 3D rendering, Navigation (as GPS), among others.


===================
Basic Qt Components
===================

As mentioned before, Spyder's plugin development consists of extending the functionality of its Qt-based graphical interface.

To develop a GUI we will add graphical elements of interaction known as widgets, arrange them using layouts. Then, we interconnect those widgets using customized procedures implemented as functions or methods, allowing to trigger behavior from user interaction. In the following, we will develop these ideas in more detail.

Each type of Qt component is a class starting with the letter ``Q`` followed by a name related to its functionality.

The core component of Qt is the ``QApplication`` class. Every Qt application needs a single instance of this class as the base, from where the Qt *event loop* is controlled.
Spyder itself is an instance of ``QApplication``, its starting point is in the following two lines of code (spyder/spyder/app/mainwindow.py):

.. code:: python

   QMainWindow.__init__(self)
   qapp = QApplication.instance()

``QMainWindow`` is a pre-built widget that provides many standard window features as toolbars, menus, a status bar, dockable widgets and more, which serves as the basis for the application.


Signals & Slots
~~~~~~~~~~~~~~~

**Signals** are notifications emitted by widgets when something happens. That something could be different things, from pressing a button, to changing text in an input box, to changing text in the window.
Many signals are initiated by user action, but this is not a rule.

**Slots** are signal receivers. Functions or methods could be used as slots, by connecting a signal to them.
If a signal sends data, the receiver callable will also receive it.
Many Qt widgets also have their own built-in slots, so the corresponding widgets are notified automatically.


Widgets
~~~~~~~

In computer science a *Widget* is a shortened form of “window gadget”. A widget is an element of interaction, such as a button, or a container for other widgets, as panels or tabs.
The ``QWidget`` class is the fundamental class for creating interfaces in Qt, it receives events from the window system, and renders its representation on the screen. A widget can provide a container for grouping other widgets, and if it is not embedded in a parent widget, it becomes a window.


Layouts
~~~~~~~

Interfaces are built by embedding widgets inside widgets, and since they are visual components they are visually organized by means of *layouts*.
A layout indicates how the widgets fill their container, either as columns, rows, cells in a matrix or stacked so that only one is visible at a time.
Those are the 4 basic layouts available in Qt: ``QHBoxLayout``, ``QVBoxLayout``, ``QGridLayout``, and ``QStackedLayout``.



Actions, Toolbars & Menus
~~~~~~~~~~~~~~~~~~~~~~~~~

User interfaces of desktop applications usually use ``QToolbar`` and ``QMenu``. Since these are alternative ways to access the same functionality, Qt provides ``QAction`` as a way to avoid duplication of functions.
Thus, each time a menu option or a toolbar button gives access to the same function, they point to the same action.

Dialogs
~~~~~~~

A *Dialog* is a GUI component that communicates with the user. Dialogs are commonly used for functions that do not fit into the main interface.
In Qt, by design ``QDialog`` is a modal (or blocking) window that show in front of the main Window until it is dismissed.

Qt provides some *special dialogs* for the most common use-cases as *file Open/Save*, *font selection*, *error messages*, *color choosing*, *printing*, among others.


Windows
~~~~~~~

If an application requires additional windows that do not block the main window, these are generated as non-parent ``QWidget`` instances.
These are used for tasks that happen in parallel over long-running processes such as displaying graphs or document editing.


Events
~~~~~~

An *Event* denote every interaction the user has with a Qt application. There are several types of events designed to address different types of interactions.
In Qt they are represented by ``QEvent`` instances that contain information about what prompted them, and are passed to specific handlers that are responsible for triggering further actions.
