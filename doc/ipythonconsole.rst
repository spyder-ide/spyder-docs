###############
IPython Console
###############

The **IPython Console** allows you to execute commands and enter, interact with and visualize data inside any number of fully featured `IPython <https://ipython.org/>`_ interpreters.
Each console is executed in a separate process, allowing you to run scripts, interrupt execution and restart or terminate a shell without affecting the others or Spyder itself, and easily test your code in a clean environment without disrupting your primary session.

.. image:: images/console/console_standard.png
   :align: center
   :alt: Spyder IPython Console with code, inline plots, and the In prompt


|


=======================
Connecting to a console
=======================

Spyder can launch new ``IPython`` instances itself, through "Open an IPython console" under the :guilabel:`Consoles` menu, the :guilabel:`IPython Console` pane menu or its context menu (:kbd:`Ctrl-T` by default), to take advantage of the full suite of Spyder's features.
Each console implements a robust two-process ``IPython`` session, with a lightweight front-end interface connected to a full kernel back end.
Additionally, you can connect to external kernels managed by QtConsole sessions or the Jupyter Notebook, through the :guilabel:`Connect to an existing kernel` dialog under the same menus, which support many of Spyder's advanced capabilities.

.. image:: images/console/console_menu.png
   :align: center
   :alt: Spyder IPython Console as above, with the options menu open

|

When :guilabel:`Connect to an existing kernel` is selected, Spyder prompts for the connection details:

.. image:: images/console/console_dialog_connect.png
   :align: center
   :alt: Connect to kernel dialog, requesting path and connection details

|


==================
Supported features
==================

Any :guilabel:`IPython Console` in Spyder, internally or externally created, supports additional features including:

.. image:: images/console/console_completion.png
   :align: right
   :width: 50%
   :alt: Spyder IPython Console, with a popup list of code completion guesses

* Automatic code completion
* Real-time function calltips
* Debugging toolbar integration for launching the debugger and controlling execution flow

Spyder-created consoles support even more advanced capabilities, such as:

* The :doc:`variableexplorer`, with GUI-based editors for many built-in and third-party Python objects
* Full GUI integration with the enhanced ``IPython`` debugger, ``ipdb``, including viewing and setting normal and conditional breakpoints interactively in any file, a :guilabel:`Breakpoints` pane, and following along with execution flow in the in the :doc:`editor` (see the :doc:`debugging` documentation for more details)
* The :ref:`User Module Reloader <umr-section>`, which can automatically re-import modified packages and files
* Inline display of ``Matplotlib`` graphics, if the ``Inline`` backend is selected under :menuselection:`Preferences --> IPython console --> Graphics --> Graphics backend`

For information on the features, commands and capabilities built into ``IPython`` itself, see the `IPython documentation`_.

.. _IPython documentation: https://ipython.readthedocs.io/en/stable/overview.html


.. _umr-section:

===================================
Using UMR to reload changed modules
===================================

When working with scripts and modules in an interactive session, Python only loads a module from its source file once, the first time it is ``import``ed.
During this first ``import``, the bytecode (``.pyc`` file) is generated if necessary and the imported module object is cached in ``sys.modules``.
If you subsequently re-import the module anytime in the same session without Spyder, this cached code object will be used even if its source code (``.py{w}`` file) has changed in the meantime.
While efficient for final production code, this behavior is often undesired when working interactively, such as when analyzing data or testing your own modules.
In effect, you're left with no way to update or modify any already-imported modules, aside from manually removing the relevant ``.pyc`` files, or restarting the console entirely.

Fortunately, in Spyder, there's an easy solution: the :guilabel:`User Module Reloader` (UMR), a Spyder-exclusive feature that, when enabled, automatically reloads modules right in the existing ``IPython`` shell whenever they are modified and re-imported, without any of the downsides of the above workarounds.
Even better, Spyder also loads the ``%autoreload`` magic by default into any kernels it starts, allowing changes in already imported modules to be automatically picked up the as soon as the modified file is saved, without any additional user action.
With UMR enabled, you can test complex applications within the same ``IPython`` interpreter without having to restart it every time you make a change, saving large amounts of manual tedium and long restart times.
Or, if you're analyzing data step by step using your own custom libraries, you can easily add or tweak a function in the latter and see the results reflected in the former, all without the overhead of reloading the data and re-running your whole script to restore your session to the same point.

UMR is enabled by default, and will do its work automatically without user intervention, although it will provide you with a red ``Reloaded modules:`` message in the console listing the files it has refreshed when it activates. If desired, you can turned it and the message on and off, and prevent specific modules from being reloaded, under :menuselection:`Preferences --> Python interpreter --> User Module Reloader (UMR)`.


Related components
~~~~~~~~~~~~~~~~~~

* :doc:`debugging`
* :doc:`editor`
* :doc:`help`
* :doc:`historylog`
* :doc:`variableexplorer`
