################
Internal Console
################

You can use the **Internal Console** to control and debug Spyder itself, or as an embedded Python console in your own application.

.. image:: images/internal_console/internal_console_standard.png
   :alt: Spyder Internal Console, with error messages and command output shown

|


==================
Supported features
==================

The :guilabel:`Internal Console` supports code completion and calltips, just like a normal :doc:`ipythonconsole`, along with a number of GUI selection, line-wrapping, buffer, and clear/copy/paste options.
You can toggle and customize these behaviors under :guilabel:`Internal console settings` from the context menu.
Additionally, you can use a number of special commands to open a file in a Spyder or external editor, edit or remove variables, run scripts or system commands, get help, and more.
See the :guilabel:`Help` dialog in the context menu for more details on these.

.. image:: images/internal_console/internal_console_contextmenu_settings.png
   :alt: Spyder Internal Console, showing context menu with settings options

|

By default, all the commands entered in the :guilabel:`Internal Console` are executed in the same process as Spyder's.
However, you can run the :guilabel:`Internal Console` in a separate thread by passing ``--multithread`` as one of Spyder's :doc:`options` on launch.


Related components
~~~~~~~~~~~~~~~~~~

* :doc:`ipythonconsole`
