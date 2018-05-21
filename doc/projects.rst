########
Projects
########

Spyder allows users to associate a given directory with a **Project**, which offers several main advantages:

* Opening, closing or switching to a Project automatically saves and restores your Editor panes and open files to exactly how you left off.
  This allows you to easily switch between many different development tasks without having to manually re-create your session for each one.
* Your project's root directory is automatically added to the ``PYTHONPATH``, so you can easily ``import`` and work with any modules and packages you create with zero setup.
* The project path is also used to automatically set your working directory, and can be used as an automatic preset for several modules, such as the :doc:`findinfiles` search location.
* You can browse all your Project files from the :ref:`Project Explorer <project-explorer>`, regardless of your current working directory or :doc:`fileexplorer` location.
* Projects are :ref:`integrated <vcs-section>` with the ``git`` version control system, allowing you to commit files and open them or your repository in the ``gitk`` GUI right from within Spyder.

.. note::

   Projects are completely optional and not imposed on users.
   All of Spyder' functionality (session saving, File Explorer, working directory, etc) is available without creating a project, just on a global rather than project-specific basis.


Creating a project
==================

To create a project, click the New Project entry in the Projects menu, choose whether you'd like to associate a Project with an existing directory or make a new one, and enter the project's name and path:

|projectsmenu| |newprojectdialog|

.. |projectsmenu| image:: images/menu/menu_projects.png
   :width: 37%
   :alt: Closeup of Spyder's Projects menu, containing project-related commands

.. |newprojectdialog| image:: images/dialog/dialog_new_project.png
   :width: 62%
   :alt: New project dialog, with options to set the name, type and location

|


.. _project-explorer:

Using the Project Explorer
==========================

Once a Project is opened, the Project Explorer pane is shown, presenting a tree view of the current project's files and directories.
This pane allows you to perform all the same operations as a normal Spyder :doc:`fileexplorer`.

|projectexplorer| |contextmenu|

.. |projectexplorer| image:: images/projects/project_explorer_standard.png
   :width: 30%
   :alt: Spyder Project Explorer, displaying a directory tree of project files

.. |contextmenu| image:: images/projects/project_explorer_inset_contextmenu.png
   :width: 50%
   :alt: Inset of the context-menu for a directory in project explorer

|


.. _vcs-section:

Working with version control
============================

Spyder has basic integration with the `Git`_ distributed version control system.
You can commit or browse (in the ``gitk`` GUI) a file, directory or the entire repository via the commands in the context menu for the relevant object (right-click).

.. _Git: http://git-scm.com/

To use this functionality, the project must be located in a ``git`` repository and the ``git`` and ``gitk`` commands must be on the system path.
For Windows systems, the `Git for Windows`_ package provides a convenient installer and the option to place common git commands on the system path without creating conflicts with Windows system tools.
The second option in the dialog below is generally a safe approach.

.. _Git for Windows: https://git-for-windows.github.io/

.. image:: images/other/git_for_windows_install_path.png
   :align: center
   :alt: Git for Windows installer on the PATH options page; 2nd option chosen

|


Related components
~~~~~~~~~~~~~~~~~~

* :doc:`editor`
* :doc:`fileexplorer`
