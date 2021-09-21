################
Common Illnesses
################

Beyond the general troubleshooting steps, some frequently-reported problems require more specialized solutions.



.. _starting-kernel-problems-ref:

==========================
Errors starting the kernel
==========================

If you receive the message ``An error occurred while starting the kernel`` in the :doc:`/panes/ipythonconsole`, Spyder was unable to launch a new Python interpreter in the current working environment to run your code.
There are a number of problems that can cause this, but most can be fixed fairly quickly with a few easy steps.


Spyder-Kernels not installed/incompatible
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spyder requires a supported version of the ``spyder-kernels`` package to be present in the working environment you want to run your console in.

.. image:: /images/common-illnesses/common-illnesses-kernel-version.png
   :alt: Kernel version error dialog

It is included by default with Anaconda, but if you want to run your code in another Python environment or installation, you'll need to make sure it's installed and updated to the latest version.

Check the required version of spyder-kernels for your version of Spyder in the following table:

.. table:: Spyder and Spyder-Kernels version compatibility

   ==============   ==============
   Spyder           Spyder-Kernels
   ==============   ==============
   4.0.0-4.0.1      1.8.1
   4.1.0-4.1.2      1.9.0
   4.1.3            1.9.1
   4.1.4            1.9.3
   4.1.5-4.1.6      1.9.4
   4.2.0            1.10.0
   5.0.0-5.0.5      2.0.5
   5.1.0-5.1.5      2.1.1
   ==============   ==============

To do so, activate the environment, then install ``spyder-kernels``.
If using Anaconda, open a terminal (Anaconda Prompt on Windows) and run:

.. code-block:: bash

   conda activate ENVIRONEMENT-NAME
   conda install spyder-kernels=<VERSION>

Otherwise, activate your environment by whatever means you created it, and execute:

.. code-block:: bash

   pip install spyder-kernels==<VERSION>

For both of the previous commands, replace ``<VERSION>`` with the corresponding version in the table.


Issue with another dependency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the kernel displays a long error traceback that mentions other packages like ``ipython``, ``ipykernel``, ``jupyter_client``, ``traitlets`` or ``pyzmq``, the problem may be an out of date or incompatible version of a dependency package.
To fix this, activate the environment and update the key dependencies.

In an Anaconda environment:

.. code-block:: bash

   conda activate ENVIRONMENT-NAME
   conda update spyder-kernels ipython ipykernel jupyter_client jupyter_core pyzmq traitlets

Otherwise, activate your environment by whatever means you created it, and run:

.. code-block:: bash

   pip install -U spyder-kernels ipython ipykernel jupyter_client jupyter_core pyzmq traitlets


AttributeError/ImportError
~~~~~~~~~~~~~~~~~~~~~~~~~~

Check the last few lines of the error message, and see if its an ``AttributeError`` or ``ImportError``, or refers to a file you created in your current working directory or your home folder (:file:`C:/Users/YOUR_USERNAME` on Windows, :file:`/Users/YOUR_USERNAME` on macOS, or :file:`/home/YOUR_USERNAME` on Linux).

.. image:: /images/common-illnesses/common-illnesses-atribute-error.png
   :alt: Spyder's AtributeError dialog

If so, the the error is likely due to your file being named the same as a Python standard library module, such as ``string.py`` or ``time.py``, which overrides the built-in module that Spyder-Kernels is trying to load.
To fix this, simply rename your file to something other than one of these names, and try restarting the kernel.
To check the names of these modules, see the list in the `Python standard library documentation`_.

.. _Python standard library documentation: https://docs.python.org/3/library/



.. _code-completion-problems-ref:

===========================
Completion/help not working
===========================

To provide code completions, help and real-time analysis in the Editor, Spyder uses the Python Language Server (PyLS), an implementation of the Language Server Protocol specification used by VSCode, Atom and other popular editors/IDEs.
Most help and completion issues lie outside of Spyder's control, and are either limitations with PyLS or the code that is being introspected, but some can be worked around.


Object missing docstring
~~~~~~~~~~~~~~~~~~~~~~~~

If nothing is displayed in the calltip, hover hint or help pane, the object you're trying to introspect may not have a docstring.

.. image:: /images/common-illnesses/common-illnesses-missing-docstring.png
   :alt: Docstring not found in help pane
   :width: 500px

In this case, the only solution is to add one in the source code of the original function, method or class.


Object cannot be found
~~~~~~~~~~~~~~~~~~~~~~

Some objects, whether due to being written in C, Cython or another language; generated dynamically at runtime; or being a method of an object you create, cannot be easily found without executing the code.

.. image:: /images/common-illnesses/common-illnesses-not-found.png
   :alt: Object not found in help pane
   :width: 500px

However, once you run your code in the :doc:`/panes/ipythonconsole`, you might be able to get help and completions on the object there.


LSP has stopped working
~~~~~~~~~~~~~~~~~~~~~~~

Occasionally, especially after using Spyder for a while, code completion, help and analysis may stop working.
If this is the case, you can check LSP status with the :guilabel:`LSP Python` item in Spyder's status bar at the bottom of the screen, and restart it by right-clicking it and selecting the :guilabel:`Restart Python Language Server` item.

.. image:: /images/common-illnesses/common-illnesses-LSP-restart.png
   :alt: Spyder with LSP restart dialog


Spyder bug/dependency issue
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given the variety of dependencies involved in making LSP work, an incompatible or out of date version in your environment can result in error messages, incomplete results, or help/analysis not working at all.

To address this, first try updating Anaconda and Spyder as described in :doc:`basic-first-aid`.
If the issue still isn't resolved, update the various relevant dependencies with:

.. code-block:: bash

   conda update python-language-server



===============
Plugin Problems
===============

Plugin does not work at all
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have installed a Spyder plugin, but you can't see it, go to the :guilabel:`Panes` submenu of the :guilabel:`View` menu and select the plugin's name, which should make its pane visible.
If you don't see the plugin there, select the :guilabel:`Dependencies` item under the :guilabel:`Help` menu and see if the plugin appears at the bottom.

.. image:: /images/common-illnesses/common-illnesses-plugins.png
   :alt: Dependencies dialog showing Unittest plugin

If the plugin with the problem is not listed in the dependencies dialog, check that you installed it in the same environment as Spyder.
If you have, then the problem may well be caused by a dependency issue.
Test whether you can import the plug-in manually by opening a Python console in the same environment as Spyder and typing, for instance, ``import spyder_unittest`` to test the Spyder-Unittest` plug-in; this command should run without errors.

If none of this helps you to resolve the problem, then continue to the next section.


Other issues
~~~~~~~~~~~~

If you get an error which mentions or involves a Spyder plugin, such as ``spyder-unittest``, ``spyder-terminal`` or ``spyder-notebook``, or if you encounter any other problem with a Spyder plugin, then the first approach should be to update Spyder and the plugin to their latest versions.

If this doesn't fix the problem, you should check the plugin's website or repository to see if it is compatible with your version of Spyder.

Finally, if compatibility doesn't seem to be the problem, please check those repositories to see if an issue was already opened, and report it there if not.
