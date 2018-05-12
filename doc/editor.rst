Editor
======

Spyder's text **Editor** is a multi-language editor with features such as syntax
coloring, code analysis (real-time code analysis powered by `pyflakes` and
advanced code analysis using `pylint`), introspection capabilities such as
code completion, calltips and go-to-definition features (powered by `rope`),
function/class browser, horizontal/vertical splitting features, etc.

.. image:: images/editor/editor_split_horizontal.png
   :align: center
   :alt: Spyder's Editor panel, split horizontally and with style analysis

|

Function/class/method browser and horizontal/vertical splitting feature:

|outline| |split|

.. |outline| image:: images/editor/outline_standard.png
   :width: 209px
   :alt: Spyder outline panel, showing the functions/classes/methods in a file


.. |split| image:: images/editor/editor_split_vertical.png
   :width: 422px
   :alt: A Spyder editor window, split vertically into two independent panes

|

Code analysis with `pyflakes`:

.. image:: images/editor/editor_inset_code_analysis.png
   :align: center
   :alt: A snippit of code in the Spyder Editor, showing code style warnings



How to define a code cell
--------------------------

A "code cell" is a concept similar to MATLAB's "cell" (except that there is
no "cell mode" in Spyder), i.e. a block of lines to be executed at once in the
current interpreter (Python or IPython). Every script may be divided in as
many cells as needed.

.. image:: images/editor/editor_standard.png
   :align: center
   :alt: Spyder's Editor panel, showing an example of a code cell

|

Cells are separated by lines starting with:

* `#%%` (standard cell separator)
* `# %%` (standard cell separator, when file has been edited with Eclipse)
* `# <codecell>` (IPython notebook cell separator)


Related components
~~~~~~~~~~~~~~~~~~

* :doc:`fileexplorer`
* :doc:`findinfiles`
* :doc:`ipythonconsole`
* :doc:`projects`
* :doc:`pylint`
