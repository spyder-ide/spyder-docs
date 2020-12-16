###############
IPython Console
###############

The **IPython Console** allows you to execute commands and enter, interact with and visualize data inside various `IPython`_ interpreters.

.. _IPython: https://ipython.org/

.. image:: images/console/console-standard.png
   :alt: Spyder IPython Console with code, inline plots, and the In prompt

To launch a new IPython instance go to :guilabel:`Open an IPython console` under the :guilabel:`Consoles` menu, the :guilabel:`IPython Console` pane menu or its context menu (:kbd:`Ctrl-T` by default).

(Gif with Open Ipython Console)

From the options menu, you will be able to interrupt execution, restart or terminate a shell and clear all your variables associated to one console.
As each one is executed in a separate process, this won't affect the other shells or Spyder itself, and you will be able to easily test your code in a clean environment without disrupting your primary session.



=============================
Connect to an external kernel
=============================

Connect to a local kernel
~~~~~~~~~~~~~~~~~~~~~~~~~

You can connect to external local and remote kernels, including those managed by QtConsole sessions or the Jupyter Notebook, through the :guilabel:`Connect to an existing kernel` dialog under the same menus.
External kernels still support :ref:`many <console-features>` (though not all) of Spyder's advanced capabilities.

.. image:: images/console/console-menu.png
   :alt: Spyder IPython Console as above, with the options menu open


Connect to a remote kernel
~~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to an external kernel,

#. Launch an IPython kernel on the local or remote host if one is not already running.

   * If using Spyder 3.3.0 or later, you'll need to launch the kernel with ``python -m spyder_kernels.console`` (after you've first installed ``spyder-kernels`` on the host with ``<conda/pip> install spyder-kernels``).
   * If using a version of Spyder before 3.3.0, ``ipython kernel`` should work to launch the kernel, albeit without certain Spyder-specific features.

#. Copy the connection file (:file:`{jupyter/runtime/dir/path}/kernel-{pid}.json`) to the machine you're running Spyder on (if remote) or note its location (if local).

   You can get :file:`{jupyter/runtime/dir/path}` by executing ``jupyter --runtime-dir`` in the same Python environment as the kernel.

#. Click :guilabel:`Connect to an existing kernel` from the :guilabel:`Console` menu or the :guilabel:`IPython Console` pane's "Gear" menu.

#. Browse for or enter the path to the connection file from the previous step.
   If you're connecting to a local kernel, click :guilabel:`Ok` and Spyder should connect to the kernel; if a remote kernel, proceed to the final step.

   As a convenience, kernel ID numbers (e.g. ``1234``) entered in the connection file path field will be expanded to :file:`{jupyter/runtime/dir/path}/kernal-{id}.json` on your local machine.

#. If connecting to a remote kernel over ``ssh``, check the appropriate box and type the full hostname you're connecting to (in the form :file:`{username}@{hostname}:{port-number}`).
   Then, enter *either* :file:`{username}` 's password on the remote machine, or your user SSH keyfile (typically :file:`.perm`) (only one is needed to connect), and press :guilabel:`Ok`.

   The port number is the one on which the SSH daemon (``sshd``) is running, typically 22 unless you or your administrator has configured it otherwise.

(Gif of connecting to external kernel SSH ->CAM)

For more technical details about connecting to remote IPython kernels, see the `Connecting to a remote kernel`_ page in the IPython Cookbook.
Just remember to enter the appropriate details into Spyder's :guilabel:`Connect to an existing kernel` dialog instead of launching a new frontend on the client with ``--existing``.

.. _Connecting to a remote kernel: https://github.com/ipython/ipython/wiki/Cookbook:-Connecting-to-a-remote-kernel-via-ssh



================
Special consoles
================

Depending on your purpose, you can also open specialized consoles within Spyder.
A `Cython console`_ will allow you to use Cython language to write C functions for Python.
A `Sympy console`_ allows Python code with symbolic math expressions.
Finally, a `Pylab console`_ has Numpy, Matplotlib and other useful scientific libraries imported by default.

.. _Cython console: https://cython.org/#documentation
.. _Sympy console: https://docs.sympy.org/latest/index.html
.. _Pylab console: https://matplotlib.org/faq/usage_faq.html#matplotlib-pyplot-and-pylab-how-are-they-related

(Gif opening menu and showing opening one of the special consoles)



.. _console-features:

==================
Supported features
==================

Any :guilabel:`IPython Console`, supports:

* Automatic code completion
* Real-time function calltips
* Debugging toolbar integration for launching the debugger and controlling execution flow

.. image:: images/console/console-completion.png
   :alt: Spyder IPython Console, with a popup list of code completion guesses

Spyder-created consoles support even more advanced capabilities, such as:

* The :doc:`variableexplorer`, with GUI-based editors for many built-in and third-party Python objects.
* Full GUI integration with the enhanced IPython :doc:`debugging`.
* Inline display of Matplotlib graphics, if the ``Inline`` backend is selected under :menuselection:`Preferences --> IPython console --> Graphics --> Graphics backend`.

For information on the features, commands and capabilities built into IPython itself, see the `IPython documentation`_.

.. _IPython documentation: https://ipython.readthedocs.io/en/stable/overview.html



============
Options menu
============

The options allows you to display the environment variables, the system path contents and the elapsed time, in case you want to know for how long your console has been running.

(Screenshot of options menu)

All the tabs in the IPython console have a name by default.
However you can change the name of each tab of the with the corresponding option or double-clicking on top of it.

(Gif of changing name)



.. _umr-section:

===================================
Using UMR to reload changed modules
===================================

When working with scripts and modules in an interactive session, Python only loads a module from its source file once, the first time it is ``import``-ed.

The :guilabel:`User Module Reloader` (UMR), when enabled, automatically reloads modules right in the existing IPython shell whenever they are modified and re-imported.
With UMR enabled, you can test changes to your code without restarting the kernel.

(Screenshot Editor split in two: Module and code with import of module / Console to show message of the module reloaded)

UMR is enabled by default and it will provide you with a red ``Reloaded modules:`` message in the console listing the files it has refreshed when it activates.
If desired, you can turn it and the message on or off, and prevent specific modules from being reloaded, under :menuselection:`Preferences --> Python interpreter --> User Module Reloader (UMR)`.

(Screenshot of preferences)



==================
Related components
==================

* :doc:`debugging`
* :doc:`editor`
* :doc:`help`
* :doc:`historylog`
* :doc:`variableexplorer`
