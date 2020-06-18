########
Profiler
########

The **Profiler** pane recursively determines the run time and number of calls for every function and method called in a file, breaking down each procedure into its smallest individual units.
This allows you to easily identify the bottlenecks in your code, points you toward the exact statements most critical for optimization, and measures the performance delta after followup changes.

.. image:: images/profiler/profiler_standard.png
   :alt: Spyder Profiler pane, displaying a list of functions and their execution time

|


====================
Running the Profiler
====================

You can browse for a file using the open button or manually enter the path in the :guilabel:`Profiler`'s path box (top left of the pane). You can then run the analysis on the file by pressing :guilabel:`Profile` in the :guilabel:`Profiler` pane.

GIF (selecting file)

You can also run profiling for the file that is currently open in the :doc:`editor` by
clicking :menuselection:`&Run --> Profile` in the menu bar, or by using a configurable shortcut (:kbd:`F10` by default).

GIF (no file in the path, profile from the menu)

If you'd like to cancel an in-progress run, click the :guilabel:`Stop` button in the top right, and if profiling fails for any reason, the :guilabel:`Output` dialog will be displayed, indicating the error that occurred. 

You can double-click an item in the profiler to go directly to the file and line in the :doc:`editor` where it was called.

GIF (click some function that opens another file)

You can increase the number of levels displayed for a particular object by clicking the dropdown arrows to the left of the name, and expand/collapse all the items with the buttons in the top left.

GIF (dropdown arrows + buttons)

You can click the dropdown or press the :kbd:`Down Arrow` key in the filename field to recall paths of previous profiled files.

(Screenshot)

You can save the data for a given run to disk as a file with the ``.Result`` extension using the :guilabel:`Save data` button, and it can be loaded to compare with another run using the :guilabel:`Load data` button.
To remove the loaded data, click the :guilabel:`Clear comparison` button.

GIF (Have analysis, save data, running again, loading data) 



========================
Interpreting the results
========================

Results are broken down by function/method/statement, with each sub-element listed hierarchically under the top-level item that called them.
:guilabel:`Total Time` is that taken by the specified item and every function "underneath" (*i.e.* called by) it, while :guilabel:`Local Time` only counts the time spent in the particular callable object's own scope.
The :guilabel:`Calls` column displays the total number of times the specified object was called at that level inside its parent calling function (or within the ``__main__`` scope, if a top-level object).
Finally, the numbers in the :guilabel:`Diff` columns for each of the three appear if a comparison is loaded, and indicate the deltas between each measurement.

.. image:: images/profiler/profiler_comparison.png
   :alt: Profiler with a comparison loaded, displaying the time deltas between two runs

|

For example, suppose you ran the :guilabel:`Profiler` on a file calling a function ``print_wrapper()`` that in turn called the ``print()`` function, and the ``print_wrapper()`` function took a total of 3 ms to run, with 2 ms of that spent executing the ``print()`` function inside it.
Therefore, if ``print()`` called nothing else itself, its :guilabel:`Total Time` and :guilabel:`Local Time` would both be identical, at 2 ms.
Meanwhile, :guilabel:`Total Time` for ``print_wrapper()`` would be 3 ms, but :guilabel:`Local Time` only 1 ms as the rest of that time was spend inside the ``print()`` function it called.



================
Profiler Plugins
================

There are two additional components that you can install to enable different types of profiling in Spyder. 
First, Spyder Line Profiler allows you to benchmark each line of your code individually. 
To learn more, visit the `spyder-line-profiler git repository`_.

.. _spyder-line-profiler git repository: https://github.com/spyder-ide/spyder-line-profiler

Second, Spyder Memory Profiler measures the memory usage of your code. 
For more information, see the `spyder-memory-profiler git repository`_.

.. _spyder-memory-profiler git repository: https://github.com/spyder-ide/spyder-memory-profiler



Related components
~~~~~~~~~~~~~~~~~~

* :doc:`ipythonconsole`
* :doc:`pylint`
