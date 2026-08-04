.. _panes-debugger:

########
Debugger
########

The new **Debugger** pane added in Spyder 6 allows you to control the debugging process, browse and navigate the current execution stack, and view and manage active breakpoints throughout your files.
This uses the enhanced IPdb debugger, which can be controlled via the buttons in Spyder's main toolbar and the :ref:`panes-console`.

.. image:: /images/debugging/debugging-console.webp
   :alt: The Spyder interface, showing an Editor file with breakpoints and debug status, the Debugger pane with the execution stack and breakpoints, and the IPython Console with debug commands



.. _panes-debugger-ipdb:
.. _panes-debugger-using:

=====================
Debugging with Spyder
=====================

You can control debugger execution via the buttons in the main toolbar and :guilabel:`Debugger` pane, as well as from the :guilabel:`Debug` menu and via configurable keyboard shortcuts, along with the standard ``ipdb`` `console commands`_.

.. _console commands: https://wangchuan.github.io/coding/2017/07/12/ipdb-cheat-sheet.html

.. video:: /images/debugging/debugging-commands.webm
   :loop:
   :nocontrols:
   :alt: The Spyder interface, showing debugging from toolbar

The :ref:`panes-editor` shows the line of code the debugger is currently stopped on with an arrow, as well as red togglable circles for breakpoints.

.. image:: /images/debugging/debugging-arrow.webp
   :alt: Spyder Editor showing the debugging panel, including a breakpoint and the locator arrow

Spyder's debugger offers syntax highlighting, code completion and command history, which work just like they do in the normal interactive interpreter.
Use the up and down arrows to recall previous commands, and press :kbd:`Tab` to trigger autocomplete suggestions.

.. video:: /images/debugging/debugging-autocompletion.webm
   :loop:
   :nocontrols:
   :alt: A Spyder IPython console window, showing autocompletion when debugging

Furthermore, IPython's `magic functions`_ are available in debugging mode.
You can, for example, run ``%ls`` to list the contents of your current working directory or ``%timeit`` to check how fast a given snippet of code is.

.. _magic functions: https://ipython.readthedocs.io/en/stable/interactive/magics.html

.. image:: /images/debugging/debugging-timeit.webp
   :alt: The Spyder IPython Console, showing use of the timeit IPython magic

Finally, you can enter and execute multiline statements in Spyder's debugger just like with the regular IPython prompt, to easily run complex code.

.. video:: /images/debugging/debugging-multiline.webm
   :loop:
   :nocontrols:
   :alt: Demonstration of multiline execution in the IPython Console when debugging



.. _panes-debugger-breakpoints:
.. _debugging-breakpoints:

===========
Breakpoints
===========

The right section of Spyder's :guilabel:`Debugger` pane lists the file, line, and condition (if any) of every breakpoint defined in any open file.
To open it, select :menuselection:`Debug --> List breakpoints`, or press the file icon to the right of the :guilabel:`Debugger` pane toolbar.

.. image:: /images/debugging/breakpoints-standard.webp
   :alt: Spyder's Debugger pane, showing the breakpoints list with a variety of breakpoints set showing file, line number and an optional condition

There are several different ways to set and clear breakpoints:

* With the :guilabel:`Toggle breakpoint` item in the :guilabel:`Debug` menu (:guilabel:`Set/edit conditional breakpoint` to edit the condition of a breakpoint).
* Through pressing the configurable keyboard shortcut (by default, :kbd:`F12` to toggle a breakpoint, and :kbd:`Shift-F12` to set a condition).
* By clicking to the left of the line number in an open file in the Editor (holding :kbd:`Shift` for a conditional breakpoint).
* With the ``breakpoint()`` builtin function in your code.
* Interactively, using the ``b`` command in a debugging session.

.. video:: /images/debugging/debugging-breakpoints.webm
   :loop:
   :nocontrols:
   :alt: Spyder showing setting conditional breakpoint

You can access and edit local and global variables at each breakpoint through the :ref:`panes-variables`.

.. image:: /images/debugging/debugging-variables.webp
   :alt: Spyder's Console and Variable Explorer showing local and global variables when debugging



.. _panes-debugger-stack:

===================
Stack frame browser
===================

New in Spyder 6, the :guilabel:`Debugger` pane now features a stack frame browser, allowing you to easily view and explore the execution stack while debugging.

.. note::

   Each time your code calls a function, it is added to the stack and execution continues inside that function, with further levels being added if that function itself calls further functions.
   When a function finishes executing and returns, it is popped from the stack and execution continues with the function that called it, on the previous level of the stack.
   Each level of the stack has its own namespace, i.e. its own local variables, and normally cannot directly access those defined within other levels, so that variables in different functions don't conflict.
   You can think of it like a "stack" of papers, which each paper being a function that forms one level of execution, the values of local variables being written only on that one sheet of paper and papers being added or removed only from the top of the stack.

The highest-level code where execution started is shown at the top, while the lowest-level function, the one currently executing, is shown at the bottom, just like in an error traceback.
From left to right, you can see the filename, line number in the file and the line of code that was last executed at that level.
Clicking any line will jump to that level in the execution stack, allowing you to run code in that context in the :guilabel:`IPython Console`.
Furthermore, it will also display that file in the :guilabel:`Editor`, with the arrow icon pointing to the line that was run there, and the :guilabel:`Variable Explorer` will switch to show the values of the local variables visible in that stack frame's namespace.

.. _panes-debugger-postmortem:

The stack frame browser also allows you to explore the levels of an exception traceback when an error occurs in your code.
When an exception is raised, it is automatically displayed in the browser, in the same format as the debugger stack, and you can click each level of the traceback to jump to that file and line.
To jump into the live debugger at the point the error occurred, press the :guilabel:`Start debugging after last error` button in the :guilabel:`Debugger` pane toolbar.
You can then use the stack frame browser as before to view and interact with the code and variables at different levels of the execution stack, by simply clicking them.
The Debugger pane remembers the last error that occurred even if you run further code or make changes to your files, up until you either start a debugging session or another error is raised.



.. _panes-debugger-advanced:

=================
Advanced features
=================

You can avoid stepping through other Python packages while debugging by enabling the :guilabel:`Ignore Python libraries while debugging` option in Spyder's Preferences, under :menuselection:`Debugger --> Interaction`.
This will skip stopping on any line of code inside the built-in and third-party Python modules you have installed, to focus on debugging your own code.

.. image:: /images/debugging/debugging-libraries.webp
   :alt: Spyder's preferences, showing the Ignore Python libraries while debugging option

If your code has variables with the same names as IPdb commands (e.g. ``b`` or ``step``), you can still refer to those variables as normal while debugging.
To call the respective IPdb command, just add an exclamation point before it (e.g. ``!b`` or ``!step``).

.. image:: /images/debugging/debugging-commands.webp
   :alt: Spyder's IPython Console, showing how to type IPdb commands with an exclamation mark

You can have Spyder automatically execute a custom snippet of code every time the debugger stops.
For example, you can use this to set specific variables, or import commonly-used modules so they are always available while debugging.
To set this up, go to :menuselection:`Preferences --> Debugger --> Run code while debugging`, and enter the code that you want to be executed with each step.

.. image:: /images/debugging/debugging-snippet.webp
   :alt: The Debugger pane of Spyder's Preferences, showing how to add a snippet of code to run while debugging



.. _panes-debugger-matplotlib:

==================
Matplotlib support
==================

Generating Matplotlib figures is fully supported while the debugger is active, including all the different graphics backends.
Use the ``%matplotlib`` magic to change to an interactive backend (e.g. ``%matplotlib qt5``) to pan, zoom and adjust your plots in a separate window, or switch back to the default ``inline`` (``%matplotlib inline``) to see them displayed right in the :ref:`panes-plots` pane.

.. video:: /images/debugging/debugging-matplotlib.webm
   :loop:
   :nocontrols:
   :alt: Debugger showing matplotlib interactive backend


To avoid showing plots while debugging, deactivate the :guilabel:`Process execute events while debugging` option in :menuselection:`Preferences --> Debugger --> Interaction`.



.. _panes-debugger-related:

=============
Related panes
=============

* :ref:`panes-editor`
* :ref:`panes-console`
* :ref:`panes-variables`
