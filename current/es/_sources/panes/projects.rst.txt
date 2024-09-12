########
Projects
########

Spyder allows you to associate a given directory with a **Project**, which automatically saves and restores the files you have open in the :doc:`editor` from the last time you opened that project.
With the :ref:`Project <project-explorer>` pane, you can browse all your project's files, regardless of your current working directory or :doc:`fileexplorer` location.

.. image:: /images/projects/projects-main.png
   :alt: Spyder showing Project Explorer and projects menu

In addition, your project's root folder is used to set your working directory, and automatically added to the ``PYTHONPATH``, so you can easily ``import`` and work with any modules and packages you create inside of it.

.. note::

   Projects are completely optional and not imposed on users.
   All of Spyder' functionality (code completion, session saving, File Explorer, working directory, etc) is available without creating a :guilabel:`Project`.



==================
Creating a Project
==================

To create a :guilabel:`Project`, click the :guilabel:`New Project` entry in the :guilabel:`Projects` menu, choose whether you'd like to associate a :guilabel:`Project` with an existing directory or make a new one, and enter the :guilabel:`Project`'s name and path.

.. image:: /images/projects/projects-new.gif
   :alt: Spyder showing opening a new project



.. _project-explorer:

=======================
Using the Projects Pane
=======================

Once a :guilabel:`Project` is opened, the :guilabel:`Project` pane is shown, presenting a tree view of the current :guilabel:`Project`'s files and directories.
It allows you to perform all the same :ref:`operations<file-operations>` as Spyder's :doc:`fileexplorer` pane.

.. image:: /images/projects/projects-standard.png
   :alt: Spyder Project Explorer, displaying a directory tree of project files



.. _vcs-section:

============================
Working with version control
============================

The :guilabel:`Project` pane has basic integration with the `Git`_ distributed version control system, just like :ref:`in the Files pane<files-vcs-support>`.
You can commit or browse a file, directory or the entire repository via the commands in the context menu.

.. _Git: https://git-scm.com/

To use this functionality, the :guilabel:`Project` must be located in a ``git`` repository and the ``git`` and ``gitk`` commands must be on the system path.



=============
Related panes
=============

* :doc:`editor`
* :doc:`fileexplorer`
