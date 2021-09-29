######
Editor
######

Spyder's multi-language **Editor** integrates a number of powerful tools right out of the box for an easy to use, efficient editing experience.
The Editor's key features include syntax highlighting (``pygments``); real-time code and style analysis (``pyflakes`` and ``pycodestyle``); on-demand completion, calltips and go-to-definition features (``rope`` and ``jedi``); a function/class browser, horizontal and vertical splitting, and much more.

.. image:: /images/editor/editor-standard.png
   :alt: Spyder's Editor panel, split horizontally and with style analysis

:guilabel:`Outline Explorer` (function/class/method browser) and horizontal/vertical splitting capabilities:

.. image:: /images/editor/editor-outline-standard.png
   :alt: Spyder outline panel, showing the functions/classes/methods in a file

Real-time code and style analysis with ``pyflakes`` and ``pycodestyle``:

.. image:: /images/editor/editor-inset-code-analysis.png
   :alt: A snippit of code in the Spyder Editor, showing code style warnings



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
