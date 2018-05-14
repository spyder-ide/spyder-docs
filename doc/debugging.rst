#########
Debugging
#########

**Debugging** in Spyder is supported through integration with the enhanced ``ipdb`` debugger in the :doc:`ipythonconsole`.
This allows breakpoints and the execution flow to be viewed and controlled right from the Spyder GUI, as well as with all the familiar IPython console commands.

.. image:: images/debugging/debugging_console.png
   :align: center
   :alt: A Spyder IPython console window, showing the ipdb debugger in action

|


Debugging with ipdb
===================

Spyder offers the following debugging features integrated into the native GUI:

.. image:: images/debugging/debugging_condbreakpoint.png
   :align: right
   :width: 50%
   :alt: Inset of Spyder Editor, with breakpoint set and condition dialog open

* Multiple means of setting and clearing normal and conditional breakpoints for any line in a file opened in the :doc:`editor`.

  * By selecting the respective option from the Debug menu.
  * Through pressing a configurable keyboard shortcut (F12 for normal, or Shift-F12 for conditional breakpoints by default).
  * By double-clicking to the left of the line number in an open file.
  * With a ``ipdb.set_trace()`` statement in your code.
  * Interactively, using the ``b`` magic command in an ``ipdb`` session.

* A breakpoints pane, listing the file, line, and condition (if any) of every breakpoint defined (Debug > List Breakpoints, or Ctrl-Shift-B by default).
* Full GUI control over debugger execution from the Debug menu, Debug toolbar and via configurable keyboard shortcuts, along with the standard ``ipdb`` console commands.
* Highlighting of the current frame (debugging step) in the :doc:`editor`.
* The ability to accessed and edit local and global variables at each breakpoint through the :doc:`variableexplorer`, and run many commands in the :doc:`ipythonconsole`.

For a comprehensive but accessible introduction to ``pdb``/``ipdb``, consult Steve Ferg's excellent online guide, `Debugging in Python`_.

.. _Debugging in Python: https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/


Related components
~~~~~~~~~~~~~~~~~~

* :doc:`editor`
* :doc:`ipythonconsole`
* :doc:`variableexplorer`
