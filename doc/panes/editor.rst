######
Editor
######

Spyder's multi-language **Editor** pane is the key element of the IDE where users can create, open, and modify code files.
The Editor offers a variety of core features like autocompletion, real-time analysis, syntax highlighting, horizontal and vertical splitting, and much more.
In addition, it uniquely integrates a number of powerful tools for an easy to use, efficient editing experience.

.. image:: /images/editor/editor-standard.png
   :alt: Spyder's Editor panel, split horizontally and with style analysis

===========================
The Editor's key components
===========================

The editor pane consists of the following areas:

.. image:: /images/editor/editor-pane.png
   :alt: Spyder's Editor panel, showing the different areas of the editor


1. The left sidebar shows line numbers and displays any code analysis errors/warnings that exist in the current file.
   Clicking a line number highlights the code in that line.

.. image:: /images/editor/editor-pane-code-error.png
   :alt: Spyder outline panel, showing an example of a code error

2. The right and bottom scrollbars help navigate the code in the current file vertically and horizontally.
3. The Context menu displays actions relevant to the editor pane. To display the editor's context menu, right-click anywhere over it and a list of possible options will appear under the cursor.
4. Another menu called the Options menu appears when clicking the "Hamburger" icon at the top right, which includes useful settings and actions relevant to the editor.

.. image:: /images/editor/editor-pane-options-menu.png
   :alt: Spyder outline panel with the options menu expanded

5. The location-based breadcrumbs on the top left of the editor pane show the exact location of the current file in your system.
6. The tabs bar displays the names of all opened files.
   It also offers a "Browse tabs" ability to effortlessly switch between current tabs and see which file is currently under selection.
   This feature comes handy when there is a large number of opened files.
   By default, the active/in-use tab is usually underlined in blue and shows with a check mark on its left when you click "Brows tabs".


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
