.. _panes-console:

###############
IPython Console
###############

The **IPython Console** allows you to execute commands and interact with data inside `IPython`_ interpreters.

.. _IPython: https://ipython.org/

.. image:: /images/console/console-standard.png
   :alt: Spyder IPython Console with code, inline plots, and the In prompt

To launch a new IPython instance, go to :guilabel:`New console (default settings)` under the :guilabel:`Consoles` menu, or use the keyboard shortcut :kbd:`Ctrl-T` (:kbd:`Cmd-T` on macOS) when the console is focused.

.. image:: /images/console/console-new.gif
   :alt: Spyder showing opening a new Ipython Console

From the same menu, you can stop currently executing code with :guilabel:`Interrupt kernel`, clear a console's namespace with :guilabel:`Remove all variables`, or relaunch a fresh one with :guilabel:`Restart kernel`.
As each console is executed in a separate process, this won't affect any others you've opened, and you will be able to easily test your code in a clean environment without disrupting your primary session.



.. _console-features:
.. _panes-console-features:

==================
Supported features
==================

Any :guilabel:`IPython Console`, whether :ref:`external <panes-console-external>` or started by Spyder, supports:

* Automatic code completion
* Real-time function calltips
* Full GUI integration with the enhanced Spyder :ref:`panes-debugger`.
* The :ref:`panes-variables`, with GUI-based editors for many built-in and third-party Python objects.
* Display of Matplotlib graphics in Spyder's :ref:`panes-plots` pane, if the :guilabel:`Inline` backend is selected under :menuselection:`Preferences --> IPython console --> Graphics --> Graphics backend`, and inline in the console if :guilabel:`Mute inline plotting` is unchecked under the :guilabel:`Plots` pane's options menu.

.. image:: /images/console/console-completion.png
   :alt: Spyder IPython Console, with a popup list of code completion guesses

For information on the features, commands and capabilities built into IPython itself, see the `IPython documentation`_.

.. _IPython documentation: https://ipython.readthedocs.io/en/stable/overview.html



.. _panes-console-special:

================
Special consoles
================

Spyder also supports several types of specialized consoles.
A `Sympy console`_ enables creating and displaying symbolic math expressions right inside Spyder.
A `Cython console`_ allows you to use the Cython language to speed up your code and call C functions directly from Python.
Finally, a `Pylab console`_ loads common Numpy and Matplotlib functions by default; while this is deprecated and strongly discouraged for new code, it can still be used if necessary for legacy scripts that need it.

.. _Cython console: https://cython.org/#documentation
.. _Sympy console: https://docs.sympy.org/latest/index.html
.. _Pylab console: https://matplotlib.org/stable/api/index.html

.. image:: /images/console/console-special.gif
   :alt: Spyder showing opening a new special Console



.. _panes-console-external:
.. _panes-console-remote:

============================
External and remote consoles
============================

You can open a new console in a remote environment you've set up using the :ref:`panes-remote` by selecting it under :menuselection:`Consoles --> New console in remote server`, or the equivalent item in the context menu.
For more details about creating and managing remote connections, see the :ref:`panes-remote` documentation.

You can also open a new console tab connected to an existing running kernel, either local or remote, by using the advanced option :menuselection:`Consoles --> Connect to existing kernel...`.
See :ref:`panes-remote-existing` for more information.



.. _panes-console-options:

============
Options menu
============

The options menu allows you to inspect your current environment variables (:guilabel:`Show environment variables`), and the contents of your system's ``PATH`` (:guilabel:`Show sys.path contents`).
In addition, you can have each console display how long it has been running with :guilabel:`Show elapsed time`.

.. image:: /images/console/console-options-menu.png
   :alt: Spyder IPython Console with options menu

You can also change the name of the current :guilabel:`IPython console` tab with the :guilabel:`Rename tab` option, or by simply double-clicking it.

.. image:: /images/console/console-rename.gif
   :alt: Spyder IPython Console showing renaming console



.. _umr-section:
.. _panes-console-umr:

======================
Reload changed modules
======================

When working in an interactive session, Python only loads a module from its source file once, the first time it is imported.

Spyder's :guilabel:`User Module Reloader` (UMR) automatically reloads modules right in your existing IPython consoles whenever they are modified and re-imported.
With the UMR enabled, you can test changes to your code without restarting the kernel.

.. image:: /images/console/console-reload-modules.png
   :alt: Spyder showing reloading modules in console

UMR is enabled by default, and it will provide you with a red ``Reloaded modules:`` message in the console listing the files it has refreshed when it is activated.
If desired, you can turn it on or off, and prevent specific modules from being reloaded, under :menuselection:`Preferences --> Python interpreter --> User Module Reloader (UMR)`.

.. image:: /images/console/console-umr-preferences.png
   :alt: Spyder preferences showing option to use module reloader



.. _panes-console-related:

=============
Related panes
=============

* :ref:`panes-debugger`
* :ref:`panes-editor`
* :ref:`panes-help`
* :ref:`panes-history`
* :ref:`panes-variables`
