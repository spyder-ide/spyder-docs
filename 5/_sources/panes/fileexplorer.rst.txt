#####
Files
#####

The **Files** pane is a filesystem and directory browser built right into Spyder.
You can view and filter files according to their type and extension, open them with the :doc:`editor` or an external tool, and perform many common operations.

.. image:: /images/files/files-standard.png
   :alt: Spyder Files pane, showing a tree view of files and metadata



.. _file-operations:

===============
File operations
===============

To browse the files on your system, use the arrows at the top of the pane.
You can expand/collapse the folders in the pane to display the files and subdirectories hierarchically.
Double-clicking a folder will open it, showing the files inside and making it your working directory.

.. image:: /images/files/files-browse.gif
   :alt: Spyder Files pane showing browsing directories

To open a file in the :guilabel:`Editor` from the :guilabel:`Files` pane, double-click its name.
If you right-click over it, you will see a context menu that allows you to access a number of functions, including running scripts; creating, renaming, moving, deleting files; and opening them in your computer's file manager.

.. image:: /images/files/files-context-menu.png
   :alt: Spyder Files pane showing context menu

You can copy and paste one or several files to and from the pane, and copy their absolute or relative paths to the clipboard as text.
If copying the paths for multiple files, they will be automatically formatted so you can paste them directly into a Python list.

.. image:: /images/files/files-copy-path.gif
   :alt: Spyder Files pane showing copying absolute path to Editor



.. _files-vcs-support:

=======================
Version control support
=======================

The :guilabel:`Files` pane allows you to perform basic operations with the `Git`_ distributed version control system, like committing your changes and browsing the repository a given file or folder is part of.
This is :ref:`particularly useful<vcs-section>` when you're working in Spyder :doc:`projects`.

.. _Git: https://git-scm.com/

.. image:: /images/files/files-commit.gif
   :alt: Spyder Files pane showing committing change of file



============
Options menu
============

The options menu in the top right of the :guilabel:`Files` pane offers several ways to customize how your files are displayed.

By default, the pane displays the contents of your working directory without filtering.
However, it can filter the list to show only files matching the patterns set under :guilabel:`Show filenames with these extensions...`, if you toggle the :guilabel:`Filter filenames` button in the pane toolbar.

.. image:: /images/files/files-filters.gif
   :alt: Spyder Files pane showing filtering files

You can also activate the :guilabel:`Show hidden files` option, which will display files that are invisible by default in your operating system.

Additionally, you can change which file attributes you want to see by hiding or displaying the :guilabel:`Type`, :guilabel:`Size` and :guilabel:`Date Modified` columns using the corresponding menu options.

.. image:: /images/files/files-columns-display.png
   :alt: Spyder Files pane showing columns checked and shown

The menu also gives you the option to open files and directories with a single instead of a double click, to suit your preferences.



=================
File associations
=================

:guilabel:`Files` allows you to associate different external applications with specific file extensions they can open.
Under the :guilabel:`File associations` tab of the :guilabel:`Files` preferences pane, you can add file types and set the external program used to open each of them by default.

.. image:: /images/files/files-associations.gif
   :alt: Spyder Files pane showing files associations

Once you've set this up, files will automatically launch in the associated application when opened from Spyder's :guilabel:`Files` pane.
Additionally, when you right-click a file, you will find an :guilabel:`Open with...` option that will allow you to select from the applications associated with this extension.

.. image:: /images/files/files-associations-open.gif
   :alt: Spyder Files pane showing opening file with associated program



=============
Related panes
=============

* :doc:`editor`
* :doc:`findinfiles`
* :doc:`projects`
