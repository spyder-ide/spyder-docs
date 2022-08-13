######
Editor
######

Spyder's multi-language **Editor** pane is the key element of the IDE, where you can create, open, and modify source files.
The Editor offers a variety of core features, such as autocompletion, real-time analysis, syntax highlighting, horizontal and vertical splitting, and much more.
In addition, it integrates a number of powerful tools for an easy to use, efficient editing experience.

.. image:: /images/editor/editor-standard.png
   :alt: Spyder's Editor panel, split horizontally and with style analysis

==============
Key components
==============

The Editor pane consists of the following areas:

.. image:: /images/editor/editor-components.png
   :alt: Spyder's Editor pane, showing its different areas (described below)

1. The left sidebar shows line numbers and displays any code analysis warnings that exist in the current file.
   Clicking a line number selects the text on that line, and clicking to the right of it sets a :ref:`breakpoint <debugging-breakpoints>`.
2. The scrollbars allow vertical and horizontal navigation in a file.
3. The context (right-click) menu displays actions relevant to whatever was clicked.
4. The options menu ("Hamburger" icon at top right) includes useful settings and actions relevant to the Editor.
5. The location bar at the top of the Editor pane shows the full path of the current file.
6. The tab bar displays the names of all opened files.
   It also has a :guilabel:`Browse tabs` button (at left) to show every open tab and switch between them—which comes in handy if many are open.



===================
Defining code cells
===================

A "code cell" in Spyder is a block of lines, typically in a script, that can be easily executed all at once in the current :doc:`ipythonconsole`.
This is much like a "cell" in MATLAB (except without any need to enable a "cell mode", since in Spyder, cells are detected automatically).
You can divide your scripts into as many cells as needed, or none at all—the choice is yours.

.. image:: /images/editor/editor-cells.png
   :alt: Spyder's Editor panel, showing an example of a code cell

You can separate cells by lines starting with either:

* ``#%%`` (standard cell separator)
* ``# %%`` (standard cell separator, when file has been edited with Eclipse)
* ``# <codecell>`` (IPython notebook cell separator)

Providing a description to the right of the separator will give that cell its own name in the :guilabel:`Outline Explorer`.
You can also create "subsections" by adding more ``%`` signs to the cell separator, e.g. ``# %%%`` to create a level 2 subsection, ``# %%%%`` for level 3, etc.
This displays multiple levels in the the :guilabel:`Outline Explorer`.

.. image:: /images/editor/editor-subsections.png
   :alt: Spyder outline panel, showing an example of sub sections

Note that this only affects how the outline is displayed; it has no impact on the functioning of the code cells.




==================
Related components
==================

* :doc:`fileexplorer`
* :doc:`findinfiles`
* :doc:`ipythonconsole`
* :doc:`projects`
* :doc:`pylint`
