#########################
Debugging and Breakpoints
#########################

**Debugging** in Spyder is supported through integration with the enhanced ``ipdb`` debugger in the :doc:`ipythonconsole`.
This allows breakpoints and the execution flow to be viewed and controlled right from the Spyder GUI, as well as with all the familiar IPython console commands.

.. image:: images/debugging/debugging-console.png
   :alt: A Spyder IPython console window, showing the ipdb debugger in action



===================
Debugging with ipdb
===================

You can have full GUI control over debugger execution from the :guilabel:`Debug` menu, :guilabel:`Debug toolbar` and via configurable keyboard shortcuts, along with the standard ``ipdb`` `console commands`_.

.. _console commands: https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/

Gif Inset of Spyder's Editor, with a breakpoint set and the condition dialog open (commands from the toolbar)

Spyder's debugger has features like syntax highlighting, completion, and history which work exactly like the IPython console. To trigger autocomplete suggestions, press `Tab`, and use the up and down arrows to recall previous commands.

Gif browsing autocomplete suggestions

You can also take advantage of IPython's `magic functions`_ in debugging mode which will allow you to use `%matplotlib` to switch between the `qt5` and `inline` plotting backends, and `%timeit` to check how fast a given snippet of code is.

.. _magic functions: https://ipython.readthedocs.io/en/stable/interactive/magics.html

Screenshot (timeit)

Additionally the debugger allows highlighting of the current frame (debugging step) in the :doc:`editor`. 

Screenshot of highlighting step (close up) 

Finally, you can write multiline statements while debugging which will allow you execute code while debugging easily.

Gif of multiline debugging

===========
Breakpoints
===========

Spyder's debugger is integrated with a :guilabel:`Breakpoints` pane, listing the file, line, and condition (if any) of every breakpoint defined (:menuselection:`&Debug --> List breakpoints`, or :kbd:`Ctrl-Shift-B` by default).

.. image:: images/debugging/breakpoints-standard.png
   :alt: Spyder's Breakpoints panel, with a number of examples showing file, line number and an optional condition

There are Multiple means of setting and clearing normal and conditional breakpoints for any line in a file opened in the :doc:`editor`.

  * By selecting the respective option from the Debug menu.
  * Through pressing a configurable keyboard shortcut (:kbd:`F12` for normal, or :kbd:`Shift-F12` for conditional breakpoints by default).
  * By clicking to the left of the line number in an open file in the Editor and shift-clicking for conditional breakpoints.
  * With the ``breakpoint()`` function in your code.
  * Interactively, using the ``!b`` command in an ``ipdb`` session.

Gif setting conditional breakpoint shift-clicking 

You can access and edit local and global variables at each breakpoint through the :doc:`variableexplorer`.

Screenshot with console and variable explorer showing local and global variables


=================
Advanced features
=================

You can avoid stepping through other Python packages while debugging by enabling the new `Ignore Python libraries while debugging` option in Spyder's preferences under `IPython Console > Debugger > Debug`.
This will skip all the built-in and third-party Python modules.

Screenshot with option in preferences

When debugging, if your code has variables with the name of Pdb commands, your debugging workflow might be interrumpted. To avoid the mix of Pdb commands and Python statements when using the interactive prompt add an exclamation mark in front of the Pdb commands to separate them from Python expressions.

Screenshot with "b" variable 

You can execute a snippet of code before any Pdb command to make sure you have the modeules and variables in your context when debugging. 
To set this up, go to `Preferences` > `IPython Console` > `Debugger` > `Run code while debugging` and write there the code that you want to be executed before the Pdb commands.

Screenshot with Run code while debugging in preferences.


==================
Matplotlib support
==================

Plotting Matplotlib figures is fully supportd while debugging with the :guilabel:`inline` backend and the :guilabel:`interactive` backends which you can use by typing the matplotlib magic. 

Gif of plots in interactive backend (zooming in and out)

To avoid showing plots while debugging, deactivate the :guilabel:`Process execute events while debugging` option in :guilabel:`Preferences > IPython console > Debugger`.





==================
Related components
==================

* :doc:`editor`
* :doc:`ipythonconsole`
* :doc:`variableexplorer`
