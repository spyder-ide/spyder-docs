####################
Spyder Line Profiler
####################

**Spyder-Line-Profiler** is a plugin to run the Python `line profiler <https://pypi.python.org/pypi/line_profiler>`_.
This package profiles the time that individual lines of code take to execute.

.. image:: /images/lineprofiler/lineprofiler-overview.png
   :alt: Spyder with the Line Profiler pane open


============================
Installing the Line Profiler
============================

If you installed Spyder using conda, the best way to install Spyder-line-profiler is to run the following command in your terminal or Anaconda prompt on Windows:

.. code-block:: bash

   conda install spyder-line-profiler -c spyder-ide

.. important::

   At the moment it is not possible to use this plugin with the Spyder :ref:`standalone_installers_ref` for Windows and macOS. We're working to make that possible in the future.

Restart Spyder in order to be able to use the plugin.

=======================
Using the Line Profiler
=======================

When the Line Profiler is installed, it will be available under the menu item :menuselection:`View --> Panes --> Line Profiler`.

.. image:: /images/lineprofiler/lineprofiler-view-panes.png
   :alt: Spyder showing View Panes Line Profiler

You will see it then as a tab next to the 'Files' tab. For the Line Profiler to work, we must place the ``@profile`` decorator on top of the functions that we wish to profile.

.. image:: /images/lineprofiler/lineprofiler-add-decorators.gif
   :alt: Adding 'profile' decorators to script to profile it line by line.

Now that the decorators have been added, you can then either select a script with the button present in the pane or run the profiler from :menuselection:`Run --> Profile line by line`.
Your file will then be profiled line by line.

.. image:: /images/lineprofiler/lineprofiler-run-menu.png
   :alt: Spyder showing the line profiler button in the Run menu

After running the Line Profiler, either from the button in the Pane or the :menuselection:`Run` menu,
the results are shown in the Line Profiler pane. The path displayed there is the path of the file being profiled.

.. image:: /images/lineprofiler/lineprofiler-run-profiler.gif
   :alt: Running the line profiler and inspecting the results.
