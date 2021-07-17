###############
Spyder Terminal
###############

**Spyder-terminal** is a plugin that allows you to have an integrated Terminal inside Spyder.

.. image:: /images/terminal/terminal-standard.png
   :alt: Spyder Terminal in Spyder

Using the terminal inside Spyder allows you to use the system shell rather than just the IPython console. You can use it to issue commands, interact
with version control or to run programs.

=======================
Installing the Terminal
=======================

If you installed Spyder using conda, the best way to install Spyder-terminal is to run the following command in your terminal or Anaconda prompt on Windows:

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

You will see it then as a tab in the bottom of the console area. When switching to it, a new terminal tab will be created. You can also create a new terminal tab by clicking in the :guilabel:`+` button at the upper right corner of the console area.

.. image:: /images/terminal/terminal-new-terminal-option.gif
   :alt: Spyder showing the new terminal button

You can also click the :guilabel:`Options` button next to the :guilabel:`+` button. You can rename terminals, undock the terminal, and open a terminal in the directory of the current Editor file.

.. image:: /images/terminal/terminal-options-menu.gif
   :alt: Spyder showing the terminal Options menu

If you right click the terminal area, it's possible to issue commands such as :guilabel:`Clear Terminal`, :guilabel:`Zoom In/Out` and :guilabel:`Copy/Paste Text`.

.. image:: /images/terminal/terminal-right-click.gif
   :alt: Spyder showing the terminal context menu
