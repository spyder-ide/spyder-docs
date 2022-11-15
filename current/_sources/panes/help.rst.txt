####
Help
####

You can use the **Help** pane to find, render and display rich documentation for any object with a docstring, including modules, classes, functions and methods.
This allows you to access documentation easily directly from Spyder, without having to interrupt your workflow.

.. image:: /images/help/help-execution.gif
   :alt: Spyder main window showing getting help for numpy arrays from editor

You can also access Spyder's tutorial from here, which will guide you through some basic steps for using its key features.

.. image:: /images/help/help-tutorial.png
   :width: 500
   :alt: Spyder Help pane showing the link for the Spyder's tutorial



============
Getting help
============

Help can be retrieved both by static analysis of open files in the :doc:`editor`, or by dynamically inspecting an object in an :doc:`ipythonconsole`.
You can trigger help manually by pressing the configurable help shortcut (:kbd:`Ctrl-I` by default).

.. image:: /images/help/help-command.png
   :alt: Spyder Editor and Help panes, with the latter displaying documentation for an object selected in the former.

You can also manually enter the object's name into the :guilabel:`Object` textbox at the top of the pane, if :guilabel:`Console` is selected as the :guilabel:`Source`.

.. image:: /images/help/help-console.gif
   :alt: Spyder Help pane, displaying documentation for an object whose name was written in the object text box

Automatic help can be individually enabled for both the :guilabel:`Editor` and the :guilabel:`Console` under :menuselection:`Preferences --> Help --> Automatic Connections`, and turned on and off dynamically via the lock icon in the top right corner of the :guilabel:`Help` pane.
If enabled, simply typing a left parenthesis (``(``) after a function or method name will show its associated help.

.. image:: /images/help/help-automatic-connections.gif
   :alt: Spyder console and help pane showing automatic help with parenthesis



========================
Understanding help modes
========================

You can use the options menu (:guilabel:`Hamburger` icon) in the top right of the :guilabel:`Help` pane to toggle the help display mode.

:guilabel:`Rich Text` mode renders the object's docstrings with ``Sphinx``, :guilabel:`Plain Text` mode displays the docstring without formatting while :guilabel:`Show Source` displays the docstring inline with the code for the selected object, or any Python portion of it (if the object is not pure Python).
The latter can be useful when docstrings are not available or insufficient to document the object.

.. image:: /images/help/help-modes.gif
   :alt: Spyder help pane showing different modes


.. _help-hover-hints:

========================
Getting help by hovering
========================

You can also get summary help for objects by hovering over them in the :guilabel:`Editor`.
Clicking the hover popup will open the full documentation in the :guilabel:`Help` pane.

.. image:: /images/help/help-hover.png
   :alt: Editor pane showing help of an object from hover



========================
Control automatic import
========================

When you get help in the :guilabel:`IPython Console` for an object that has not been previously imported, it is automatically loaded in Spyder's own internal interpreter so that documentation can be shown when available.
This can be disabled in the :guilabel:`Help` pane's top-right options menu so that only documentation from imported objects is displayed.



=============
Related panes
=============

* :doc:`editor`
* :doc:`ipythonconsole`
* :doc:`onlinehelp`
