#######
History
#######

With the **History** pane, you can view all the commands entered into any :doc:`ipythonconsole` along with their time-stamp.

.. image:: images/history/history-menu.png
   :alt: Spyder History Log, displaying a list of previously executed commands

(Replace screenshot for screenshot without the options menu)



=================
Using the History
=================

Navigating the :guilabel:`History` pane is very straightforward.
Each Spyder session is marked by a date and time-stamp, making it easy to remember when you executed a certain command.
Statements can be selected and copied from the context menu or with the normal system shortcuts.
Just like in the editor, highlighting a word or phrase displays all other occurrences, and full syntax highlighting is also supported.



============
Options Menu
============
The top-right options menu (:guilabel:`Gear` icon) allows you to set the number of commands the :guilabel:`History` pane should remember.

(Gif with dialog for changing the maximum entries)

You can also toggle wrapping of long lines (:guilabel:`Wrap lines`), and decide whether to display the line number at the left of the pane.

(Gif to display deactivating wrapping and displaying line number)



==============
Advanced usage
==============

The commands from the :guilabel:`History` are stored in the :file:`.spyder-py3` directory in your user home folder (by default, :file:`C:/Users/{username}` on Windows, :file:`/Users/{username}` for macOS, and typically :file:`/home/{username}` on GNU/Linux).
You might need to show invisible files in order to see it on a non-Windows operating system.

(Screenshot of the history log file)



==================
Related components
==================

* :doc:`ipythonconsole`
