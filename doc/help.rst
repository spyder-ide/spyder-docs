####
Help
####

You can use the **Help** pane to find, render and display rich documentation for any object with a docstring, including modules, classes, functions and methods.
Help can be retrieved both by static analysis of open files in the :doc:`editor`, or by dynamically inspecting an object in an :doc:`ipythonconsole`.

You can trigger help by manually entering the object's name into the :guilabel:`Object` box, pressing the configurable help shortcut (:kbd:`Ctrl-I` by default), or even automatically if desired when on typing a left parenthesis (``(``) after a function or method name.
Automatic help can be individually enabled for both the :guilabel:`Editor` and the :guilabel:`Console` under :menuselection:`Preferences --> Help --> Automatic Connections`, and turned on and off dynamically via the :guilabel:`lock` icon in the top right corner of the :guilabel:`Help` pane.


========================
Understanding help modes
========================

You can use the options menu (:guilabel:`Gear` icon) in the top right of the :guilabel:`Help` pane to toggle the help display mode.

:guilabel:`Rich Text` mode renders the object's docstrings with ``Sphinx``:

.. image:: images/help/help_standard.png
   :alt: Spyder Help panel, displaying rich text docs for the DataFrame class

|

:guilabel:`Plain Text` mode displays the docstring without formatting:

.. image:: images/help/help_plain.png
   :alt: Spyder Help panel, displaying plain text docs for the DataFrame class

|

:guilabel:`Show Source` displays the docstring inline with the code for the selected object, or any Python portion of it (if the object is not pure Python).
This can be useful when docstrings are not available or insufficient to document the object:

.. image:: images/help/help_source_code.png
   :alt: Help panel showing part of the docstring and source code for DataFrame

|


Related components
~~~~~~~~~~~~~~~~~~

* :doc:`editor`
* :doc:`ipythonconsole`
* :doc:`onlinehelp`
