######
Editor
######

Spyder's multi-language **Editor** pane is the key element of the IDE, where you can create, open, and modify source files.
The Editor offers a variety of core features, such as autocompletion, real-time analysis, syntax highlighting, horizontal and vertical splitting, and much more.
In addition, it integrates a number of powerful tools for an easy to use, efficient editing experience.

.. image:: /images/editor/editor-standard.png
   :alt: Spyder's Editor pane, split horizontally and with style analysis



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



=========
Interface
=========

Tabs
~~~~

You can browse and navigate between open files in the Editor with tabs.
Click the :guilabel:`Browse tabs` button on the left of the tab bar to display a list of open files, with the active tab checked.

.. image:: /images/editor/editor-tabs-browser.png
   :alt: Spyder's Editor pane, showing the tabs browser

Reorder files by dragging and dropping, or with :guilabel:`Sort tabs alphabetically` in the options menu, which also allows closing all tabs to the right of, or all tabs but the active one.

.. image:: /images/editor/editor-tabs-sorting.gif
   :alt: Spyder's Editor pane, showing how to browse and sort open tabs alphabetically


File switcher
~~~~~~~~~~~~~

The Editor features a file switcher, which enables you to navigate and switch between multiple open files.
The file switcher is helpful for locating any file when there are several files opened.

.. image:: /images/editor/editor-file-switcher.png
   :alt: Spyder's Editor pane, showing the file switcher

It can be accessed from the :menuselection:`File --> File Switcher` menu or :kbd:`Ctrl-P`, and includes a search function.
You can type in any part of an open file's name and—if exists—it can be switched to by pressing :kbd:`Enter`.

.. image:: /images/editor/editor-file-switcher.gif
   :alt: Spyder's Editor pane, showing searching and switching to an existing file


Split panels
~~~~~~~~~~~~

The Editor can be split horizontally and vertically into as many distinct panels as desired.
This allows viewing and editing the contents of several files (or different parts of the same file) at the same time.

.. image:: /images/editor/editor-split-panels.gif
   :alt: Spyder's Editor pane, showing how to split panels

Split the Editor with the :guilabel:`Split vertically` (:kbd:`Ctrl-Shift-{`) and :guilabel:`Split horizontally` (:kbd:`Ctrl-Shift--`) commands in the options menu, and use :guilabel:`Close this panel` (:kbd:`Alt-Shift-W`) to close the selected split panel.

.. note:: :menuselection:`Close this panel` closes a split panel, while :menuselection:`Close` hides the entire Editor *pane* (including all splits, which are restored when the Editor is re-opened).



================
Editing features
================

Syntax highlighting
~~~~~~~~~~~~~~~~~~~

To improve the readability of your code, Spyder has a syntax highlighting feature that determines the color and style of text in the Editor, as well as in the :doc:`ipythonconsole`.

You can configure and preview syntax highlighting themes and fonts under :menuselection:`Preferences --> Appearance`.
The :guilabel:`Syntax highlighting theme` section allows you to change the color and style of the syntax elements and background to match your preferences.
You can switch between available themes in the drop-down menu, modify the selected theme, create a new theme, and more.
The :guilabel:`Fonts` section lets you change the text font and size.

.. image:: /images/editor/editor-syntax-highlighting.gif
   :alt: Spyder's Editor pane, showing how to switch between syntax highlighting themes

.. note:: Changes made to the syntax highlighting theme and font settings are common to all source files, regardless of their language.


Code cells
~~~~~~~~~~

A "code cell" in Spyder is a block of lines, typically in a script, that can be easily executed all at once in the current :doc:`ipythonconsole`.
This is similar to "cell" behavior in Jupyter Notebook and MATLAB.
You can divide your scripts into as many cells as needed, or none at all—the choice is yours.

.. image:: /images/editor/editor-cells.png
   :alt: Spyder's Editor pane, showing an example of a code cell

You can separate cells by lines starting with either:

* ``# %%`` (standard cell separator), or
* ``# <codecell>`` (IPython notebook cell separator)

Providing a description to the right of the separator will give that cell its own name in the :doc:`outline`.
You can also create "subsections" by adding more ``%`` signs to the cell separator, e.g. ``# %%%`` to create a level 2 subsection, ``# %%%%`` for level 3, etc.
This displays multiple levels in the :doc:`outline` pane.

.. image:: /images/editor/editor-subsections.png
   :alt: Spyder outline pane, showing an example of sub sections

.. note:: This only affects how the cell is displayed in the :doc:`outline`, and doesn't affect running it in the Editor.

To run the code in a cell, use :menuselection:`Run --> Run cell`, the :guilabel:`Run cell` button in the toolbar or the keyboard shortcut (:kbd:`Ctrl-Enter`/:kbd:`Cmd-Return` by default).
You can also run a cell and then jump to the next one, letting you quickly step through multiple cells, using :menuselection:`Run --> Run cell and advance` (:kbd:`Shift-Enter` by default).


Automatic formatting
~~~~~~~~~~~~~~~~~~~~

The Editor has built-in support for automatically formatting your code using several popular tools, including `Autopep8 <https://github.com/hhatto/autopep8>`_ and `Black <https://black.readthedocs.io/en/stable/>`_.
The :guilabel:`Format file or selection with {tool}` command in the :guilabel:`Source` or context menu will format either the selected fragment (if text is selected) or the entire active file.

.. image:: /images/editor/editor-automatic-formatting.gif
   :alt: Spyder Editor pane, showing an example of code selection formatting

You can have the Editor automatically autoformat a file every time you save your work.
To set this up, go to :menuselection:`Preferences --> Completion and linting --> Code style and formatting --> Code formatting` and check the :guilabel:`Autoformat files on save` option.

.. image:: /images/editor/editor-autoformat-setting.png
   :alt: Spyder's preferences dialog, showing checking the autoformat files on save setting



============
Running code
============

The Editor lets you run an entire file as well as specific lines, selections or cells.

As your code is running,

* The :doc:`ipythonconsole` will display output and errors.
* The :doc:`variableexplorer` allows you to browse and interact with the objects generated.
* The :doc:`plots` pane renders the figures and images created.


Run file
~~~~~~~~

Run an entire Editor file using the :menuselection:`Run --> Run` menu item, the :guilabel:`Run file` toolbar button or the :kbd:`F5` key.
Use :menuselection:`Run --> Re-Run last script` to re-run the most recent file executed with the above.


Run line/selection
~~~~~~~~~~~~~~~~~~

You can execute the current line—or multiple selected lines—using the :guilabel:`Run selection or current line` option from the toolbar or the :menuselection:`Run` menu, as well as with the :kbd:`F9` key.
After running the current line, the cursor automatically advances to the next one, so you can step through your code line by line.
Unlike :guilabel:`Run file`, the executed lines are shown in the :doc:`ipythonconsole`.


Run cell
~~~~~~~~

To run a cell, place your cursor inside it and use the :menuselection:`Run --> Run cell` menu item, the :guilabel:`Run current cell` toolbar button or the :kbd:`Ctrl-Enter` / :kbd:`Cmd-Return` keyboard shortcut.
Use :guilabel:`Run cell and advance` in the :guilabel:`Run` menu/toolbar or :kbd:`Shift-Enter` to jump to the next cell after running, useful for stepping through cells quickly.


Run configuration
~~~~~~~~~~~~~~~~~

You can use the :guilabel:`Run configuration per file` dialog to set each file's working directory, console mode (current, dedicated or external), command line arguments, execution options (clear all variables, run in an existing/empty namespace, debug on error), and more.

.. image:: /images/editor/editor-run-configuration.png
   :alt: Spyder's Editor pane, showing the Run Configuration dialog

To access it, click :menuselection:`Run --> Configuration per file...` or press :kbd:`Ctrl-F6` / :kbd:`Cmd-F6`.



===============
Code navigation
===============

Find and replace
~~~~~~~~~~~~~~~~

To search for text in the current file, use :menuselection:`Search --> Find text` or :kbd:`Ctrl-F` / :kbd:`Cmd-F`, and to replace it, use :menuselection:`Search --> Replace text` or :kbd:`Ctrl-R` / :kbd:`Cmd-R`.
Typing your search string in the resulting panel below the Editor highlights each result and counts the total.
Navigate between matches with the :guilabel:`Find Previous` and :guilabel:`Find Next` buttons in the find/replace panel, their corresponding entries in the :guilabel:`Search` menu, or use the :kbd:`F2` and :kbd:`F3` keys.
Use the :guilabel:`.*` button to process search text as a `regular expression <https://docs.python.org/3/library/re.html>`_, :guilabel:`Aa` to treat it as case-sensitive and :guilabel:`[–]` to only match whole words (e.g. for ``data``, match ``data()`` but not ``dataframe``).

.. image:: /images/editor/editor-find-replace-panel.png
   :alt: Spyder's Editor pane, showing the find and replace panel


Go to line
~~~~~~~~~~

The :guilabel:`Go to line` dialog allows jumping to a specific line in the active file.
Open it with :menuselection:`Search --> Go to line` or :kbd:`Ctrl-L` / :kbd:`Cmd-L`, type the line number you want to scroll to and press :kbd:`Enter` (or click :guilabel:`OK`).

.. image:: /images/editor/editor-go-to-line.gif
   :alt: Spyder's Editor pane, showing the go to line feature

It also shows the current line number and total line count in the file.


Class/function selector
~~~~~~~~~~~~~~~~~~~~~~~

This panel, activated under :menuselection:`Source --> Show selector for classes and functions`, displays (as applicable) the name of the cell, function/method and class the Editor cursor is located inside.
Use its dropdowns to view and jump to the functions, methods and classes in the current file.

.. image:: /images/editor/editor-class-function-selector.gif
   :alt: Spyder's Editor pane, showing the class and function selector panel



=============================
Code analysis and completions
=============================

Spyder uses the `Language Server Protocol <https://microsoft.github.io/language-server-protocol/>`_ (LSP) to provide code completion and linting for the Editor, similar to VSCode, Neovim, and other popular editors/IDEs.

.. note::

   Many issues with completion and linting are outside of Spyder's control, and are either limitations with the LSP or the code that is being introspected, but some can be worked around.
   See :ref:`code-completion-problems-ref` for troubleshooting steps.

Python is supported out of the box, and advanced users can add completion and linting support for other languages by setting up LSP servers for them under :menuselection:`Preferences --> Completion and Linting --> Other languages`.


Code completion
~~~~~~~~~~~~~~~

Automatic code completion as you type is enabled by default in the Editor, and can also be triggered manually with :kbd:`Ctrl-Space`/:kbd:`Cmd-Space`, showing you possible completions (with pop-up help for each) and available code snippets.
For example, typing ``cla`` will display the keyword ``class``, the decorator ``classmethod`` and two built-in snippets with class templates.
Select the desired completion with the arrow keys and :kbd:`Enter`, or by double clicking.

.. image:: /images/editor/editor-code-completion.png
   :alt: Spyder's Editor pane, showing a code completion example

You can enable or disable on-the-fly code completion, as well as modify when it is triggered and what results are shown, under :menuselection:`Preferences --> Completion and Linting --> General --> Completions`.
Spyder also allows you to define custom completion snippets to use, in addition to the ones offered by the LSP, under :menuselection:`Preferences --> Completion and Linting --> Advanced`.


Linting and code style
~~~~~~~~~~~~~~~~~~~~~~

Spyder can optionally highlight syntax errors, style issues, and other potential problems with your code in the Editor, which can help you spot bugs quickly and make your code easier to read and understand.

.. image:: /images/editor/editor-pane-code-error.png
   :alt: Spyder's Editor pane, showing an example of a highlighted code error

The Editor's basic linting, powered by `Pyflakes <https://github.com/PyCQA/pyflakes>`_, warns of syntax errors and likely bugs in your code.
It is on by default, and can be disabled or customized under :menuselection:`Preferences --> Completion and Linting --> Linting`.

.. image:: /images/editor/editor-linting-setting.png
   :alt: Spyder's preferences dialog, showing linting settings

Code style analysis, powered by `Pycodestyle <https://pycodestyle.pycqa.org/en/stable/>`_, flags deviations from the style conventions in :pep:`8`.
It is not active by default, but you can enable it and customize the `Pycodestyle error codes <https://pycodestyle.pycqa.org/en/stable/intro.html#error-codes>`_ shown with the options under :menuselection:`Preferences --> Completion and Linting --> Code style and formatting --> Code Style`.

.. image:: /images/editor/editor-code-style-setting.png
   :alt: Spyder's preferences dialog, showing code style and formatting settings


Introspection features
~~~~~~~~~~~~~~~~~~~~~~

If there's a function, class or variable for which you would like to check its definition, you need to :kbd:`Ctrl`/:kbd:`Cmd`-click its name in the Editor (or click its name and press :kbd:`Ctrl-G` / :kbd:`Cmd-G` to jump to the file and line where it is declared.

.. image:: /images/editor/editor-go-to-definition.gif
   :alt: Spyder's Editor pane, showing the go to definition feature

You can hover over the name of an object for pop-up help, as :ref:`described in the Help pane docs <help-hover-hints>`.

.. image:: /images/editor/editor-hoverhint.png
   :alt: Spyder's Editor pane, showing an example of a hover hint

Finally, if you type the name of a function, method or class constructor and then an open parenthesis, a calltip will pop up which shows the function's parameters as you type them, as well as a summary of its documentation.
These features can be enabled and customized under :menuselection:`Preferences --> Completion and Linting --> Introspection`.



==================
Keyboard shortcuts
==================

To view the Editor's primary keyboard shortcuts, consult its section under :menuselection:`Help --> Shortcuts Summary`.
The full list can be browsed, searched and customized (on double-click) in :menuselection:`Preferences --> Keyboard shortcuts`.



=============
Related panes
=============

* :doc:`fileexplorer`
* :doc:`findinfiles`
* :doc:`ipythonconsole`
* :doc:`projects`
* :doc:`pylint`
