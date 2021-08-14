###############
Spyder Terminal
###############

**Spyder-terminal** is a plugin that allows you to have integrated system terminals inside Spyder.

.. image:: /images/terminal/terminal-standard.png
   :alt: Spyder Terminal in Spyder

Spyder-terminal allows you to use any system shell installed in your system (e.g. Bash, Zsh or Powershell) rather than just the IPython console. You can use it to issue commands, interact
with version control or to run programs.

=======================
Installing the Terminal
=======================

If you installed Spyder using conda, the best way to install Spyder-terminal is to run the following command in your Terminal or Anaconda prompt on Windows:

.. code-block:: bash

   conda install spyder-terminal -c spyder-ide

.. important::

   At the moment it is not possible to use this plugin with the Spyder :ref:`standalone_installers_ref` for Windows and macOS. We're working to make that possible in the future.

Restart Spyder in order to be able to use the plugin.

==================
Using the Terminal
==================

When the Terminal is installed, it will be available under the menu item :menuselection:`View --> Panes --> Terminal`.

.. image:: /images/terminal/terminal-view-panes.png
   :alt: Spyder showing view panes Terminal

You will see it then as a tab at the bottom of the console area. When switching to it, a new terminal tab will be created. You can also create more terminals by clicking in the :guilabel:`+` button at the upper right corner of the terminal area.

.. image:: /images/terminal/terminal-new-terminal-option.gif
   :alt: Spyder showing the new terminal button

Clicking the :guilabel:`Options` button next to the :guilabel:`+` button will allow you to rename terminals, undock the terminal, and open a terminal in the directory of the current Editor file.

.. image:: /images/terminal/terminal-options-menu.gif
   :alt: Spyder showing the terminal Options menu

If you right click the terminal area, it's possible to issue commands such as :guilabel:`Clear Terminal`, :guilabel:`Zoom In/Out` and :guilabel:`Copy/Paste Text`.

.. image:: /images/terminal/terminal-right-click.gif
   :alt: Spyder showing the terminal context menu

====================
Terminal Preferences
====================

It's also possible to customize the Terminal by going to :menuselection:`python --> Preferences...` and then clicking on the Terminal tab on the menu to the left.
You can select the shell interpreter, set the buffer limit and the type of cursor.

.. image:: /images/terminal/terminal-preferences.png
   :alt: Preferences of the Terminal plugin
