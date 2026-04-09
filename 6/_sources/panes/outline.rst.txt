.. _panes-outline:

#######
Outline
#######

The **Outline** pane allows you to view and navigate the functions, classes, methods, cells and comments in open Python files.
To show or hide the Outline pane, use :menuselection:`View --> Panes --> Outline` or :kbd:`Ctrl-Shift-O` / :kbd:`Cmd-Shift-O`.
Click an entry in the outline to jump to its source file location, and use the :guilabel:`Go to cursor position` toolbar button to highlight the item corresponding to the current :ref:`panes-editor` position.

.. image:: /images/outline/outline-standard.png
   :alt: Outline pane



.. _panes-outline-options:

============
Options menu
============

The options menu in the top-right of the pane allows customizing how the outline is displayed.

.. image:: /images/outline/outline-options-menu.png
   :alt: Outline options menu

These customization settings include:

* :guilabel:`Show absolute path`: Display the full path to each file instead of just the name.
* :guilabel:`Show all files`: List every open file rather than just the current one.
  This allows using the Outline as a file switcher.
* :guilabel:`Group code cells`: Group code cells in multiple nested levels in the outline rather than showing all cells in one level.
  You can create subsections by adding more ``%`` signs to the cell separator.
* :guilabel:`Display variables and attributes`: Display top-level variable/constant definitions and class attributes in the outline.
* :guilabel:`Follow cursor position`: Automatically highlight and expand the entry corresponding to the current cursor position in the :ref:`panes-editor`.
* :guilabel:`Show special comments`: List special comments in the outline, which start with ``# ----``.
* :guilabel:`Sort files alphabetically`: Sort the file list in alphabetical order.
  When disabled, all tabs will be sorted by the tab order of the currently selected Editor panel.



.. _panes-outline-icons:

=====
Icons
=====

The following icons are used for outline elements:

* :guilabel:`m` for methods
* :guilabel:`f` for functions
* :guilabel:`c` for classes
* :guilabel:`%` for code cells
* :guilabel:`#` for comments



.. _panes-outline-related:

=============
Related panes
=============

* :ref:`panes-editor`
* :ref:`panes-files`
* :ref:`panes-projects`
