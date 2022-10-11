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

=========
Interface
=========

----
Tabs
----

You can browse and navigate between open files in the Editor with tabs.
Click the :guilabel:`Browse tabs` button on the left of the Tabs bar to display a list of open files, with the active tab checked.
Reorder files by dragging and dropping, or with :guilabel:`Sort tabs alphabetically` in the options menu, which also allows closing all tabs to the right of, or all tabs but the active one.

.. image:: /images/editor/editor-tabs-browser.png
   :alt: Spyder's Editor pane, showing the tabs browser

-------------
File switcher
-------------

The Editor features a file switcher, which enables you to navigate and switch between multiple open files.
The file switcher is helpful for locating any file when there are several files opened.
It can be accessed from the :menuselection:`File --> File Switcher` menu or :kbd:`Ctrl-P` and includes a search function.
You can type in any part of an open file's name and -if exists- it can be switched to by pressing Enter.

.. image:: /images/editor/editor-file-switcher.png
   :alt: Spyder's Editor pane, showing the file switcher

------------
Split panels
------------

The Editor can be split horizontally and vertically into as many distinct panels as desired.
This allows viewing and editing the contents of several files (or different parts of the same file) at the same time.

GIF needed

Split the Editor with the :guilabel:`Split vertically` (:kbd:`Ctrl-Shift-{`) and :guilabel:`Split horizontally` (:kbd:`Ctrl-Shift–`) commands in the options menu, and use :guilabel:`Close this panel` (:kbd:`Alt-Shift-W`) to close the selected split panel.
.. note: :menuselection:`Close this panel` closes a split panel, while :menuselection:`Close` hides the entire Editor *pane* (including all splits, which are restored when the Editor is re-opened).


================
Editing features
================

-------------------
Syntax highlighting
-------------------

To improve the readability of your code, Spyder has a syntax highlighting feature that determines the colour and style of text in the Editor, as well as in the :doc:`ipythonconsole`..
You can configure and preview syntax highlighting themes and fonts under :menuselection:`Preferences --> Appearance`.
The :guilabel:`Syntax highlighting theme` section allows you to change the colour theme of the syntax elements and background to match your preferences.
You can switch between available themes in the drop-down menu, modify the selected theme, create a new theme, and more.
The :guilabel:`Fonts` section lets you change the plain text font and size.

GIF new

.. note:: Changes made to the syntax highlighting theme and font settings are common to all source files, regardless of their language

----------
Code cells
----------

A "code cell" in Spyder is a block of lines, typically in a script, that can be easily executed all at once in the current :doc:`ipythonconsole`.

This is similar to "cell" behaviour in Jupyter Notebook and MATLAB.
You can divide your scripts into as many cells as needed, or none at all—the choice is yours.

.. image:: /images/editor/editor-cells.png
   :alt: Spyder's Editor panel, showing an example of a code cell

You can separate cells by lines starting with either:

* ``# %%`` (standard cell separator), or
* ``# <codecell>`` (IPython notebook cell separator)

Providing a description to the right of the separator will give that cell its own name in the :guilabel:`Outline Explorer`.
You can also create "subsections" by adding more ``%`` signs to the cell separator, e.g. ``# %%%`` to create a level 2 subsection, ``# %%%%`` for level 3, etc.
This displays multiple levels in the :guilabel:`Outline Explorer`.

.. image:: /images/editor/editor-subsections.png
   :alt: Spyder outline panel, showing an example of sub sections

.. note::  This only affects how the cell is displayed in the :guilabel:`Outline Explorer`, and doesn’t affect running it in the Editor.

To run the code in a cell, use :menuselection:`Run --> Run cell`, the :guilabel:`Run cell` button in the toolbar or the keyboard shortcut (:kbd:`Ctrl-Enter`/:kbd:`Cmd-Return` by default).
You can also run a cell and then jump to the next one, letting you quickly step through multiple cells, using  :menuselection:`Run --> Run cell and advance` (:kbd:`Shift-Enter` by default).

--------------------
Automatic formatting
--------------------

The Editor has built-in support for automatically formatting your code using several popular tools, including Autopep8, Yapf, and Black.
The :guilabel:`Format file or selection with {tool}` command in the :guilabel:`Source` or context menu will format either the selected fragment (if text is selected) or the entire active file.

GIF new

You can have the Editor automatically autoformat a file every time you save your work.
To set this up, go to :menuselection:`Preferences --> Completion and linting --> Code style and formatting --> Code formatting` and check the :guilabel:`Autoformat files on save` option.

.. image:: /images/editor/editor-autoformat-setting.png
   :alt: Spyder's preferences dialog, showing checking the autoformat files on save setting

============
Running code
============

As previously mentioned, the Editor is the place where you easily manage your work.
It allows you to create a new file or open an existing one.
It also lets you run an entire file as well as certain lines or selections.
As your code is running,

* The :doc:`ipythonconsole` will display the results and errors when applicable
* The :doc:`variableexplorer` allows you to browse and interact with the objects generated when running your code.
* The :doc:`plots` pane shows the figures and images created during your code execution.
* The :doc:`profiler` helps you optimize your code by determining the run time and number of calls for every function and method used in a file. It also allows you to save and compare your results between runs.

--------
Run file
--------

You can run any source file in the Editor by simply using the Run file button in Spyder’s toolbar or by pressing the F5 key.
You can also run your code by selecting  :menuselection:`Run --> Run` menu item.

--------
Run line
--------

You can execute just a single line of your source code where the cursor currently resides by selecting the :guilabel:`Run selection or current line` option from the  :menuselection:`Run` menu or Spyder’s toolbar.
Alternatively, you can use the F9 key to run any line.
After executing your selected line of code, the cursor automatically advances to the next line.
This helps you run your code in sequential order with a single line step.

-----------------
Other run options
-----------------

In addition to executing your entire source file at once or just a single line, the Editor allows you to run your code in other options.

^^^^^^^^^^^^^^
Multiple lines
^^^^^^^^^^^^^^

You can execute multiple lines from within the editor by highlighting these lines and using the :guilabel:`Run selection or current line` option from the  :menuselection:`Run` menu or Spyder’s toolbar.
Alternatively, you can use the F9 key to run any line.
After executing a selection of code, use the :guilabel:`Re-Run last script` command from the :menuselection:`Run` menu to execute the same selection again.
The main difference between running a selection of lines and an entire file is that in the former all lines are inserted directly into the :doc:`ipythonconsole` whereas in the latter only the results are shown in the console.

^^^^^^^^^^
Code cells
^^^^^^^^^^

To run a cell, press :kbd:`Ctrl-Return` (while your cursor is focused on it) or use the :guilabel:`Run current cell` button in Spyder’s toolbar.

^^^^^^^^^^^^^^^^^
Run configuration
^^^^^^^^^^^^^^^^^

You can configure the :guilabel:`Run per file` settings to control where and how this file runs in the :guilabel:`Configuration per file…` dialog under the :menuselection:`Run` menu or pressing :kbd:`Ctrl+F6`.
For example, you could execute the current file in a dedicated console, remove all variable before executing, or even change the working directory settings.

===============
Code navigation
===============

----------
Find panel
----------

The Editor features a find and replace functionality to find and replace a given text in the current file.
You can find a string in the current file by selecting :menuselection:`Search --> Find text` from the Spyder IDE main menu or simply using :kbd:`Ctrl+F`.
Similarly, you can to find and replace a string by selecting :menuselection:`Search --> Replace text` from the Spyder IDE main menu or using the :kbd:`Ctrl+R` shortcut.
The :guilabel:`Find and Replace` panel appears in the Editor’s bottom left corner highlighting each occurrence of the desired text in the current file and showing the total number of occurrences.
The panel allows you to navigate from one occurrence to another by choosing the :guilabel:`Find Next` or the :guilabel:`Find Previous` buttons.
It also lets you run a case-sensitive regex search using the Case Sensitive and Regular expressions controls.

.. image:: /images/editor/editor-find-replace-panel.png
   :alt: Spyder's Editor pane, showing the find and replace panel

----------
Go to line
----------

The :guilabel:`Go to line` dialog box allows you to navigate your source code and move to a specific line in the active file.
You can view and use this box under the :menuselection:`search --> Go to line` menu item or alternatively press :kbd:`Ctrl+L`.

Image/GIF placeholder

You can enter your desired line number in the :guilabel:`Go to line` input field, which should fall between 1 and the line count shown in the dialog box.

-----------------------
Class/function selector
-----------------------

When you activate the class and function selector under :menuselection:`Source --> Show` selector for classes and functions, the name of the selected class will be shown at the top of the Editor while you are exploring any object inside this class such as methods.

Image/GIF placeholder

=============================
Code analysis and completions
=============================

Spyder uses the `Language Server Protocol <https://microsoft.github.io/language-server-protocol/>`_ (LSP) to provide code completion and linting for the Editor, similar to VSCode, Atom, and other popular editors/IDEs.

.. note:: Many issues with completion and linting are outside of Spyder’s control, and are either limitation with LSP or the code that is being introspected, but some can be worked around. See :ref:`troubleshooting-completion <code-completion-problems-ref>` for troubleshooting steps.

Python is supported out of the box, and advanced users can add completion and linting support for other languages by setting up LSP servers for them under  :menuselection:`Preferences --> Completion and Linting --> Other languages`.

---------------
Code completion
---------------

Automatic code completion as you type is enabled by default in the Editor, and can also be triggered manually with :kbd:`Ctrl-Space`/:kbd:`Cmd-Space`, showing you help, possible completions, and available code snippets.
For example, typing ``cla`` will display the keyword ``class``, the decorator ``classmethod`` and two built-in snippets with class templates.
Select the desired completion with the arrow keys and :kbd:`Enter`, or by double clicking.

.. image:: /images/editor/editor-code-completion.png
   :alt: Spyder's Editor pane, showing a code completion example

You can enable or disable on-the-fly code completion as you type, as well as modify when it is triggered and what results are shown, under :menuselection:`Preferences --> Completion and Linting --> General --> Completions`.
Spyder also allows you to define custom completion snippets to use, in addition to the ones offered by LSP, under :menuselection:`Preferences --> Completion and Linting --> Advanced`.

----------------------
Linting and code style
----------------------

Spyder can optionally highlight syntax errors, style issues, and other potential problems with your code in the Editor, which can help you spot bugs quickly and make your code easier to read and understand.

.. image:: /images/editor/editor-pane-code-error.png
   :alt: Spyder's Editor pane, showing an example of a highlighted code error

The Editor’s basic linting, powered by `Pyflakes <https://github.com/PyCQA/pyflakes>`_, warns of syntax errors and likely bugs in your code.
It is on by default, and can be disabled or customized under :menuselection:`Preferences --> Completion and Linting --> Linting`.

.. image:: /images/editor/editor-linting-setting.png
   :alt: Spyder's preferences dialog, showing linting settings

Code style analysis, powered by `Pycodestyle <https://pycodestyle.pycqa.org/en/latest/>`_, flags deviations from the style conventions in :pep:`8`.
It is not active by default; you can enable it and customize the `pycodestyle error codes <https://pycodestyle.pycqa.org/en/stable/intro.html#error-codes>`_ shown with the options under :menuselection:`Preferences --> Completion and Linting --> Code style and formatting --> Code Style`.

.. image:: /images/editor/editor-code-style-setting.png
   :alt: Spyder's preferences dialog, showing code style and formatting settings

----------------------
Introspection features
----------------------

If there’s a function, class or variable that you want to jump to the definition of, :kbd:`Ctrl`/:kbd:`Cmd`-click its name in the Editor (or click its name and press :kbd:`Ctrl-G` / :kbd:`Cmd-G` to jump to the file and line where it is defined.

.. image:: /images/editor/editor-go-to-definition.gif
   :alt: Spyder's Editor pane, showing the go to definition feature

If you type the name of a function, method or class constructor and then an open parenthesis, a calltip will pop up which shows the function’s parameters as you type them, as well as a summary of its documentation.

.. image:: /images/editor/editor-calltip.png
   :alt: Spyder's Editor pane, showing an example of a calltip

Finally, you can also hover over the name of an object for pop-up help, as :ref:`described in the Help pane docs <help-hover-hints>`.
These features can be enabled and customized under :menuselection:`Preferences --> Completion and Linting --> Introspection`.

==================
Keyboard shortcuts
==================

The Editor offers a useful set of default keyboard shortcuts that can help you perform your tasks faster, increase your productivity, and stay focused by keeping your hands on the keyboard.
For an exhaustive list of keyboard shortcuts, navigate to :menuselection:`Help --> Shortcuts Summary --> Editor` menu option.
You can also navigate to :menuselection:`Preferences --> Keyboard shortcuts` for the full list of Spyder shortcuts.
All default shortcuts in the list are customizable when double clicked.


=============
Related panes
=============

* :doc:`fileexplorer`
* :doc:`findinfiles`
* :doc:`ipythonconsole`
* :doc:`projects`
* :doc:`pylint`
