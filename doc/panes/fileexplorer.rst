.. _panes-files:

#####
Files
#####

The **Files** pane is a filesystem and directory browser built right into Spyder.
You can view and filter files according to their type and extension, open them with the :ref:`panes-editor` or an external tool, and perform many common operations.

.. image:: /images/files/files-standard.webp
   :alt: Spyder Files pane, showing a tree view of files and metadata

.. note::

   The Files pane is especially useful when connected to a remote machine via the :ref:`panes-remote`, as in addition to opening and managing files in a graphical interface, it allows you to upload and download files between your computer and the remote host.
   Most, although not all quite features work similarly on a remote machine as they do locally.


.. _file-operations:
.. _panes-files-operations:

===============
File operations
===============

You can expand/collapse the folders in the pane to display the files and subdirectories hierarchically.
Double-clicking a folder will open it, showing the files inside and making it your working directory.
To go back to the previous working directory, or forward if you've already gone back, click the forward and back arrows on the pane's toolbar.
The up arrow navigates up a level to the parent directory, while the right-pointing finger goes to the directory of the current file in the :ref:`panes-editor`.

.. video:: /images/files/files-browse.webm
   :loop:
   :alt: Spyder Files pane showing browsing directories

To open a file in the :ref:`panes-editor` from the Files pane, double-click its name.
Files can also be opened in an external editor, configured via Spyder's :ref:`panes-files-associations` preferences.
The context menu when right-clicking a file allows you to access a number of functions, including running scripts; creating, renaming, moving, deleting files; and opening them in your computer's file manager (:guilabel:`Show in folder`); along with basic :ref:`Git operations <panes-files-vcs>`.

.. image:: /images/files/files-context-menu.webp
   :alt: Spyder Files pane showing context menu

You can also copy and paste one or several files to and from the pane, and copy their absolute or relative paths to the clipboard as text.
If copying the paths for multiple files, they will be automatically formatted so you can paste them directly into a Python list.

.. video:: /images/files/files-copy-path.webm
   :loop:
   :alt: Spyder Files pane showing copying absolute path to Editor



.. _files-vcs-support:
.. _panes-files-vcs:

=======================
Version control support
=======================

The :guilabel:`Files` pane allows you to perform basic operations with the `Git`_ distributed version control system via the context-menu on right-clicking a file, like committing your changes and browsing the repository a given file or folder belongs to.
This is :ref:`particularly useful <panes-projects-vcs>` when you're working in Spyder :ref:`panes-projects`.

.. _Git: https://git-scm.com/

.. video:: /images/files/files-commit.webm
   :loop:
   :alt: Spyder Files pane showing committing changes with Git



.. _panes-files-options:

============
Options menu
============

The options ("hamburger") menu in the top right of the :guilabel:`Files` pane offers several ways to customize how your files are displayed.

By default, the pane displays the contents of your working directory without filtering.
However, it can filter the list to show only files matching the patterns set under :guilabel:`Edit filter settings`, if you toggle them on via the :guilabel:`Filter filenames` button to the right of the pane toolbar.

.. video:: /images/files/files-filters.webm
   :loop:
   :alt: Spyder Files pane showing filtering files

You can also activate or deactivate the :guilabel:`Show hidden files` option, which will display files that are invisible by default in your operating system.

Additionally, you can show or hide the :guilabel:`Type`, :guilabel:`Size` and :guilabel:`Date Modified` columns using the corresponding menu options.

.. image:: /images/files/files-columns-display.webp
   :alt: Spyder Files pane showing columns checked and shown

Finally, the menu also gives you the option to open files and directories with a single- instead of a double-click, to suit your preference.



.. _panes-files-associations:

=================
File associations
=================

:guilabel:`Files` allows you to associate different external applications with specific file extensions they can open.
Under the :guilabel:`File associations` tab of the :guilabel:`Files` pane in Spyder's :guilabel:`Preferences`, you can add file types and set the external program used to open each of them by default.

.. video:: /images/files/files-associations.webm
   :loop:
   :alt: Spyder Files pane showing files associations

Once you've set this up, files will automatically launch in the associated application when opened from Spyder's :guilabel:`Files` pane.
Additionally, when you right-click a file, you will find an :guilabel:`Open with...` option that will allow you to select from the applications associated with this extension.

.. video:: /images/files/files-associations-open.webm
   :loop:
   :alt: Spyder Files pane showing opening file with associated program



.. _panes-files-related:

=============
Related panes
=============

* :ref:`panes-editor`
* :ref:`panes-find`
* :ref:`panes-projects`
