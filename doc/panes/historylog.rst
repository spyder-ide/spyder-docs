#######
History
#######

With the **History** pane, you can view all the commands you've entered into any :doc:`ipythonconsole`, along with their timestamp.

.. image:: /images/history/history-standard.png
   :alt: Spyder History Log, displaying a list of previously executed commands



======================
Using the History pane
======================

Navigating the :guilabel:`History` pane is very straightforward.
Each Spyder session is marked by a date and timestamp, making it easy to remember when you executed a certain command.
Statements can be selected and copied from the context menu or with the normal system shortcuts.
Just like in the Editor, selecting a word or phrase displays all other occurrences, and full syntax highlighting is also supported.



============
Options Menu
============

The top-right options menu (:guilabel:`Hamburger` icon) allows you to toggle wrapping of long lines (:guilabel:`Wrap lines`), and whether the line number is displayed to the left of the text (:guilabel:`Show line numbers`).

.. image:: /images/history/history-wrap.gif
   :alt: Spyder History Log, displaying wrapping lines and showing line number



==============
Advanced usage
==============

The list of commands shown in the :guilabel:`History` pane are stored in :file:`history.py` in the :file:`.spyder-py3` directory in your user home folder (by default, :file:`C:/Users/{username}` on Windows, :file:`/Users/{username}` for macOS, and typically :file:`/home/{username}` on GNU/Linux).
You might need to show invisible files in order to see it on a non-Windows operating system.

.. image:: /images/history/history-log-file.png
   :alt: Spyder History Log file



==================
Related components
==================

* :doc:`ipythonconsole`
