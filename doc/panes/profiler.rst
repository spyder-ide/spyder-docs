.. _panes-profiler:

########
Profiler
########

The **Profiler** pane recursively determines the run time and number of calls for every function and method invoked in a file, breaking down each procedure into its smallest individual units.
This allows you to identify the bottlenecks in your code, points you toward the exact statements most critical for optimization, and measures the performance delta after followup changes.

.. image:: /images/profiler/profiler-standard.png
   :alt: Spyder Profiler pane, displaying a list of functions and their execution time



.. _panes-profiler-using:

====================
Running the Profiler
====================

You can run profiling for the current :ref:`panes-editor` file, cell, selection or line by clicking the corresponding  :guilabel:`Profile <scope>` item in the :guilabel:`Run` menu, or the respective icon in Spyder's main toolbar.

.. image:: /images/profiler/profiler-execution-menu.gif
   :alt: Spyder Profiler pane, showing running profiler from menu bar

To cancel an in-progress run and see the results so far, click the :guilabel:`Stop` button on the Profiler pane toolbar.
If profiling fails, such as due to a bug in your code, the error output will be shown in the :ref:`panes-console`.

Results are broken down by function/method/statement, with each sub-element listed hierarchically under the top-level item that called them.
To or expand or collapse all items by one level of the call stack, click the :guilabel:`+` or :guilabel:`-` buttons in the left of the pane toolbar.

.. image:: /images/profiler/profiler-dropdown.gif
   :alt: Spyder Profiler pane, showing dropdown arrows and buttons for expanding and collapsing

Right-click an item in the Profiler and select :guilabel:`Go to definition` to be taken to the file and line in the :ref:`panes-editor` where it was called.

.. image:: /images/profiler/profiler-open-file.gif
   :alt: Spyder Profiler pane, showing opening a file when clicking on its analysis

You can display all functions regardless of level in the call stack, sorted by :guilabel:`Local Time` (the time spent inside just that function), using the :guilabel:`Show items with large local time` toolbar button.

To filter calls to third-party packages outside your own code, use the :guilabel:`Hide calls to external libraries` button.

Right-click any function to show every function that calls it, or every function called by it.
You can restore the default view with the :guilabel:`Show functions or modules called by the root item` toolbar button.

To find a specific function, click the :guilabel:`Search` button and type its name into the field that appears.

Finally, you can save the data for a given run to disk as a file with the ``.prof`` extension using the :guilabel:`Save profiling data` button.
This can be loaded to compare with a previous run of the same file using the :guilabel:`Load data` button.
To remove the loaded data, click the :guilabel:`Clear comparison` button.

.. image:: /images/profiler/profiler-save-load.gif
   :alt: Spyder Profiler pane, showing running profiler from menu bar



.. _panes-profiler-results:

========================
Interpreting the results
========================

Results are broken down by function/method/statement, with each sub-element listed hierarchically under the top-level item that called them.
:guilabel:`Total Time` is that taken by the specified item and every function "underneath" (*i.e.* called by) it, while :guilabel:`Local Time` only counts the time spent in the particular callable object's own scope.
The :guilabel:`Calls` column displays the total number of times the specified object was called at that level inside its parent calling function (or within the ``__main__`` scope, if a top-level object).
Finally, the numbers in the :guilabel:`Diff` columns for each of the three appear if a comparison is loaded, and indicate the deltas between each measurement, with red (+) numbers meaning the current version is slower than the previous comparison, and green (-) numbers meaning it is faster.

.. image:: /images/profiler/profiler-comparison.png
   :alt: Profiler with a comparison loaded, displaying the time deltas between two runs

For example, suppose you ran the Profiler on a file calling a function ``sleep_wrapper()`` which took a total of 10 ms to run, 9 ms of which was spent in the ``time.sleep()`` function it called in turn.
Therefore, if ``time.sleep()`` called nothing else itself, its :guilabel:`Total Time` and :guilabel:`Local Time` would both be identical, at 9 ms.
Meanwhile, :guilabel:`Total Time` for ``sleep_wrapper()`` would be 10 ms, but :guilabel:`Local Time` only 1 ms as the rest was spent inside the ``time.sleep()`` function it called.



.. _panes-profiler-plugins:

====================
Line profiler plugin
====================

There is an additional plugins that you can install to enable other types of profiling in Spyder.
Spyder Line Profiler allows you to benchmark each line of your code individually.
To learn more, visit the `spyder-line-profiler git repository`_.

.. _spyder-line-profiler git repository: https://github.com/spyder-ide/spyder-line-profiler

.. image:: /images/profiler/profiler-line-profiler.png
   :alt: Spyder Profiler pane, displaying a list of functions and their execution time



.. _panes-profiler-related:

=============
Related panes
=============

* :ref:`panes-console`
* :ref:`panes-pylint`
