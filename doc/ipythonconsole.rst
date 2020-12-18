###############
IPython Console
###############

The **IPython Console** allows you to execute commands and interact with data inside `IPython`_ interpreters.

.. _IPython: https://ipython.org/

.. image:: images/console/console-standard.png
   :alt: Spyder IPython Console with code, inline plots, and the In prompt

To launch a new IPython instance, go to :guilabel:`New console (default settings)` under the :guilabel:`Consoles` menu, or use the keyboard shortcut :kbd:`Ctrl-T` (:kbd:`Cmd-T` on macOS) when the console is focused.

(Gif with Open Ipython Console)

From the same menu, you can stop currently executing code with :guilabel:`Interrupt kernel`, clear a console's namespace with :guilabel:`Remove all variables`, or relaunch a fresh one with :guilabel:`Restart kernel`.
As each console is executed in a separate process, this won't affect any others you've opened, and you will be able to easily test your code in a clean environment without disrupting your primary session.



.. _console-features:

==================
Supported features
==================

Any :guilabel:`IPython Console`, whether :ref:`external<connecting-external-kernel>` or started by Spyder, supports:

* Automatic code completion
* Real-time function calltips
* Full GUI integration with the enhanced Spyder :doc:`Debugger<debugging>`.
* The :doc:`variableexplorer`, with GUI-based editors for many built-in and third-party Python objects.
* Display of Matplotlib graphics in Spyder's :doc:`plots` pane, if the :guilabel:`Inline` backend is selected under :menuselection:`Preferences --> IPython console --> Graphics --> Graphics backend`, and inline in the console if :guilabel:`Mute inline plotting` is unchecked under the :guilabel:`Plots` pane's options menu.

.. image:: images/console/console-completion.png
   :alt: Spyder IPython Console, with a popup list of code completion guesses

For information on the features, commands and capabilities built into IPython itself, see the `IPython documentation`_.

.. _IPython documentation: https://ipython.readthedocs.io/en/stable/overview.html



================
Special consoles
================

Spyder also supports several types of specialized consoles.
A `Sympy console`_ enables creating and displaying symbolic math expressions right inside Spyder.
A `Cython console`_ allows you to use the Cython language to speed up your code and call C functions directly from Python.
Finally, a `Pylab console`_ loads common Numpy and Matplotlib functions by default; while this is deprecated and not recommended for new code, it can be used for older scripts that need it.

.. _Cython console: https://cython.org/#documentation
.. _Sympy console: https://docs.sympy.org/latest/index.html
.. _Pylab console: https://matplotlib.org/faq/usage_faq.html#matplotlib-pyplot-and-pylab-how-are-they-related

(Gif opening menu and showing opening one of the special consoles)



============
Options menu
============

The options menu allows you to inspect your current environment variables (:guilabel:`Show environment variables`), and the contents of your system's ``PATH`` (:guilabel:`Show sys.path contents`).
In addition, you can have each console display how long it has been running with :guilabel:`Show elapsed time`.

(Screenshot of options menu)

You can also change the name of the current :guilabel:`IPython console` tab with the :guilabel:`Rename tab` option, or by simply double-clicking it.

(Gif of changing name)



.. _connecting-external-kernel:

==================================
Using external kernels with Spyder
==================================

You can connect to external local and remote kernels (including those managed by Jupyter Notebook or QtConsole) through the :guilabel:`Connect to an existing kernel` dialog under the :guilabel:`Consoles` menu.
For this feature to work, a compatible version of the ``spyder-kernels`` package :ref:`must be installed <starting-kernel-problems-ref>` in the environment or machine in which the external kernel is running.

.. image:: images/console/console-menu.png
   :alt: Connect to external kernel dialog of the Spyder IPython console


Connect to a local kernel
~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to a local kernel that is already running (e.g. one started by Jupyter notebook),
#. Run ``%connect_info`` in the notebook or console you want to connect to, and copy the name of its kernel connection file, shown after ``jupyter <app> --existing``.

#. In Spyder, click :guilabel:`Connect to an existing kernel` from the :guilabel:`Consoles` menu.

#. Paste the name of the :guilabel:`Connection file` from the previous step.

   As a convenience, kernel ID numbers (e.g. ``1234``) entered in the connection file path field will be expanded to the full path of the file, :file:`{jupyter/runtime/dir/path}/kernal-{id}.json`.

#. Click :guilabel:`OK` to connect to the kernel.

(Gif of connecting to external kernel SSH ->CAM)


Connect to a remote kernel
~~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to a kernel on a remote machine,

#. Launch a Spyder kernel on the remote host if one is not already running, with ``python -m spyder_kernels.console``.

#. Copy the kernel's connection file (:file:`{jupyter/runtime/dir/path}/kernel-{pid}.json`) to the machine you're running Spyder on.

   You can get :file:`{jupyter/runtime/dir/path}` by executing ``jupyter --runtime-dir`` in the same Python environment as the kernel.
   Usually, the connection file you are looking for will be one of the newest in this directory, corresponding to the time you started the external kernel.

#. Click :guilabel:`Connect to an existing kernel` from the :guilabel:`Consoles` menu.

#. Browse for or enter the path to the connection file from the previous step.

   As a convenience, kernel ID numbers (e.g. ``1234``) entered in the connection file path field will be expanded to :file:`{jupyter/runtime/dir/path}/kernal-{id}.json` on your local machine, if you've copied the connection file there.

#. Check the :guilabel:`This is a remote kernel (via SSH)` box and type the full hostname you're connecting to (in the form :file:`{username}@{hostname}:{port-number}`).
   Then, enter *either* :file:`{username}`'s password on the remote machine, or your user SSH keyfile (typically a  :file:`.perm` file) (only one is needed to connect), and press :guilabel:`OK`.

   :guilabel:`Port` is the port number on your remote machine that the SSH daemon (``sshd``) is listening on, typically 22 unless you or your administrator has configured it otherwise.

(Gif of connecting to external kernel SSH ->CAM)

For more technical details about connecting to remote kernels, see the `Connecting to a remote kernel`_ page in the IPython Cookbook.

.. _Connecting to a remote kernel: https://github.com/ipython/ipython/wiki/Cookbook:-Connecting-to-a-remote-kernel-via-ssh



.. _umr-section:

===================================
Using UMR to reload changed modules
===================================

When working in an interactive session, Python only loads a module from its source file once, the first time it is imported.

Spyder's :guilabel:`User Module Reloader` (UMR) automatically reloads modules right in your existing IPython consoles whenever they are modified and re-imported.
With the UMR enabled, you can test changes to your code without restarting the kernel.

(Screenshot Editor split in two: Module and code with import of module / Console to show message of the module reloaded)

UMR is enabled by default, and it will provide you with a red ``Reloaded modules:`` message in the console listing the files it has refreshed when it is activated.
If desired, you can turn it on or off, and prevent specific modules from being reloaded, under :menuselection:`Preferences --> Python interpreter --> User Module Reloader (UMR)`.

(Screenshot of preferences)



==================
Related components
==================

* :doc:`debugging`
* :doc:`editor`
* :doc:`help`
* :doc:`historylog`
* :doc:`variableexplorer`
