##########################
Frequently Asked Questions
##########################

=======================
Installing and updating
=======================

.. dropdown:: Q: How do I install Spyder?
   :container: + dropdown-id-install-spyder

   The easiest way to install Spyder is with the Anaconda Python distribution, which comes with everything you need to get started in an all-in-one package.
   Download it from its `webpage`_.

   .. _webpage: https://www.anaconda.com/products/individual

   For more information, visit our :doc:`installation`.


.. dropdown:: Q: How do I update Spyder using conda?
   :container: + dropdown-id-update-conda

   From the command line (or Anaconda prompt on Windows), run:

   .. code-block:: bash

      conda update anaconda
      conda update spyder

   If this results in an error or does not update Spyder to the latest version, try:

   .. code-block:: bash

      conda install spyder=4


.. dropdown:: Q: How do update I Spyder using Anaconda Navigator?
   :container: + dropdown-id-update-navigator

   Open the "gear" menu in Spyder's section under :guilabel:`Home` in Navigator.
   Go to :guilabel:`Install specific version` and select the version of Spyder you want to use.
   We strongly recommend the latest available, to benefit from new features, bug fixes, performance improvements and usability enhancements.

   .. image:: images/faq/faq-navigator-install.png
      :alt: Navigator showing installing specific version of Spyder



==============
Running Spyder
==============

.. dropdown:: Q: How do I run Spyder?
   :container: + dropdown-id-run-spyder

   You can launch it in any of the following ways:

   * **From the command line**: Type ``spyder`` in your terminal (or Anaconda prompt on Windows).

   * **From Anaconda Navigator**: Scroll to :guilabel:`Spyder` under :guilabel:`Home`, and click :guilabel:`Launch`.

     .. image:: images/faq/faq-launch-anaconda.png
        :alt: Navigator showing running a specific version of Spyder

   * ***Windows Only***: Launch it via the Start menu shortcut.

     .. image:: images/faq/faq-windows-launch.png
        :alt: Spyder shortcut in the Windows Start menu


.. dropdown:: Q: Can I try Spyder without installing it?
   :container: + dropdown-id-run-binder

   Yes!
   With `Binder`_, you can work with a fully functional copy of Spyder that runs right in your web browser.
   Try it `here`_.

   .. _Binder: https://mybinder.org/
   .. _here: https://mybinder.org/v2/gh/spyder-ide/spyder/4.x?urlpath=/desktop


.. dropdown:: Q: What are the system requirements for Spyder? How resource-intensive is it?
   :container: + dropdown-id-run-system-reqs

   Spyder works on modern versions of Windows, macOS and Linux (see the table below for recommended versions) via Anaconda, as well as other methods.
   It typically uses relatively minimal CPU when idle, and 0.5 GB - 1 GB of RAM, depending on how long you've been using it and how many files, projects, panes and consoles you have open.
   It should work on any system with a dual-core or better x64 processor and at least 4 GB of RAM, although 8 GB is *strongly* recommended for best performance when running other applications.
   However, the code you run, such as scientific computation and deep learning models, may require additional resources beyond this baseline for Spyder itself.

   .. table::

      ================   ===================
      Operating system   Version
      ================   ===================
      Windows            Windows 8.1
      macOS              High Sierra (10.13)
      Linux              Ubuntu 16.04
      ================   ===================


.. dropdown:: Q: How do I run Spyder installed in a conda environment using Anaconda Navigator?
   :container: + dropdown-id-run-navigator

   Select the environment you want to launch Spyder from under :guilabel:`Applications on`.
   If Spyder is installed in this environment, you will see it in Navigator's :guilabel:`Home` window.
   Click :guilabel:`Launch` to start Spyder in your selected environment.

   .. image:: images/faq/faq-run-environment.png
      :alt: Navigator showing running Spyder in a specific environment


.. dropdown:: Q: How do I run Spyder installed in a conda environment using the command line?
   :container: + dropdown-id-run-terminal

   Activate your conda environment by typing the following in your terminal (or Anaconda Prompt on Windows):

   .. code-block:: bash

      conda activate <ENVIRONMENT-NAME>

   Then, type ``spyder`` to launch the version installed in that environment.



============
Using Spyder
============

.. dropdown:: Q: How do I install Python packages to use within Spyder?
   :container: + dropdown-id-using-install-packages

   The first approach for installing a package should be using conda.
   In your system terminal (or Anaconda Prompt on Windows), type:

   .. code-block:: bash

      conda install <PACKAGE-NAME>

   If your installation is not successful, follow steps 3 through 5 of Part 2 in our video on solving and avoiding problems with pip, Conda and Conda-Forge.

   .. youtube:: Ul79ihg41Rs
      :height: 360
      :width: 640
      :align: left
      :start: 306


.. dropdown:: Q: How do I get Spyder to work with my existing Python packages/environment?
   :container: + dropdown-id-using-existing-environment

   To work with an existing environment in Spyder, you need to change Spyder’s default Python interpreter.
   To do so, click the name of the current environment in the status bar, and then click :guilabel:`Change default environment in Preferences`.

   .. image:: images/faq/faq-change-environment.png
      :alt: Change default environment in Preferences option in status bar

   This will open the :guilabel:`Preferences` dialog in the :guilabel:`Python interpreter` section.
   Here, select the option :guilabel:`Use the following Python interpreter`, and use the dropdown below to select your preferred environment.
   If its not listed, use the text box or the :guilabel:`Select file` button to enter the path to the Python interepreter you want to use.
   See the :doc:`ipythonconsole` for more information.

   .. image:: images/faq/faq-python-interpreter.png
      :alt: Preferences showing changing Python interpreter

   Click :guilabel:`Restart kernel` in the :guilabel:`Consoles` menu for this change to take effect.


.. dropdown:: Q: How do I reset Spyder's preferences to the defaults?
   :container: + dropdown-id-using-reset-prefs

   Either use the :guilabel:`Reset Spyder to factory defaults` under :guilabel:`Tools` in Spyder's menu bar, the `Reset Spyder settings` Start menu shortcut (Windows), or run ``spyder --reset`` in your system terminal (Anaconda prompt on Windows).

   .. image:: images/faq/faq-reset-spyder.png
      :alt: Spyder reset button in tools


.. dropdown:: Q: How do I change Spyder's language?
   :container: + dropdown-id-using-change-language

   Under :guilabel:`General` in Spyder's :guilabel:`Preferences`, go to the :guilabel:`Advanced settings` tab and select your language from the options displayed under :guilabel:`Language`.

   .. image:: images/faq/faq-change-language.png
      :alt: Spyder change language in preferences.


.. dropdown:: Q: How do I use code cells in Spyder?
   :container: + dropdown-id-using-code-cells

   To create a cell in Spyder's :doc:`editor`, type ``#%%`` in your script.
   Each ``#%%`` will make a new cell.
   To run a cell, press :kbd:`Shift-Enter` (while your cursor is focused on it) or use the :guilabel:`Run current cell` button in Spyder's toolbar.

   .. image:: images/faq/faq-cells.png
      :alt: Spyder showing cell generation.


.. dropdown:: Q: How do I use plugins with Spyder (e.g. Spyder-Notebook, Spyder-Terminal, Spyder-Unittest)?
   :container: + dropdown-id-using-plugins

   Spyder plugins are available in the ``spyder-ide`` conda channel.
   To install one, type on the command line (or Anaconda Prompt on Windows):

   .. code-block:: bash

      conda install -c spyder-ide <PLUGIN>

   Replace ``<PLUGIN>`` with the name of the plugin you want to use.
   For more information on a specific plugin, go to the its repository:

   * `spyder-unittest`_
   * `spyder-terminal`_
   * `spyder-notebook`_
   * `spyder-memory-profiler`_
   * `spyder-line-profiler`_

   .. _spyder-unittest: https://github.com/spyder-ide/spyder-unittest
   .. _spyder-terminal: https://github.com/spyder-ide/spyder-terminal
   .. _spyder-notebook: https://github.com/spyder-ide/spyder-notebook
   .. _spyder-memory-profiler: https://github.com/spyder-ide/spyder-memory-profiler
   .. _spyder-line-profiler: https://github.com/spyder-ide/spyder-line-profiler


.. dropdown:: Q: How do I clear all variables before executing my code?
   :container: + dropdown-id-using-clear-variables

   Check the option :guilabel:`Remove all variables before execution` in the :guilabel:`Configuration per file...` dialog under the :guilabel:`Run` menu.

   .. image:: images/faq/faq-remove-variables.png
      :alt: Spyder showing cell generation.


.. dropdown:: Q: How do I run my code in a dedicated console or an external system terminal?
   :container: + dropdown-id-using-dedicated-console

   Select the appropriate option in the :guilabel:`Configuration per file...` dialog under the :guilabel:`Run` menu.

   .. image:: images/faq/faq-run-options.png
      :alt: Spyder showing cell generation.


.. dropdown:: Q: How do I change the syntax highlighting theme in the Editor?
   :container: + dropdown-id-using-syntax-theme

   Go to :guilabel:`Preferences` and select the theme you want under :guilabel:`Syntax highlighting theme` in the :guilabel:`Appearance` section.

   .. image:: images/faq/faq-highlighting-theme.png
      :alt: Spyder showing cell generation.



===============
Troubleshooting
===============

.. dropdown:: Q: I've found a bug or issue with Spyder. What do I do?
   :container: + dropdown-id-troubleshooting-spyder

   You should first follow the steps in our :doc:`troubleshooting guide<first-steps>`.
   If you can't solve your problem, open an issue by following the instructions in our :doc:`submit-a-report` section.


.. dropdown:: Q: I get an error in the IPython console running my code! Help!
   :container: + dropdown-id-troubleshooting-running-code

   First, make sure the error you are seeing is not a bug in your code.
   To confirm this, try running it in any standard Python interpreter.
   If the error still occurs, the problem is likely with your code and a site like `Stack Overflow`_ might be the best place to start.
   Otherwise, start at the :doc:`basic-first-aid` section of our troubleshooting guide.

   .. _Stack Overflow: https://stackoverflow.com


.. dropdown:: Q: Code completion/help doesn't work; what can I do?
   :container: + dropdown-id-troubleshooting-completion

   If nothing is displayed in the calltip, hover hint or :doc:`help` pane, make sure the object you are inspecting has a docstring, and try executing your code in the :doc:`ipythonconsole` to get help and completions there.
   If this doesn't work, try restarting PyLS by right-clicking the :guilabel:`LSP Python` label item in the statusbar at the bottom of Spyder's main window, and selecting the :guilabel:`Restart Python Language Server` option.

   For more information, go to the :ref:`code-completion-problems-ref` section in the :doc:`common-illnesses` page of our troubleshooting guide.


.. dropdown:: Q: I get the message "An error occurred while starting the kernel". How do I fix this?
   :container: + dropdown-id-troubleshooting-starting-kernel

   First, make sure your version of Spyder-Kernels is compatible with that of Spyder.

    .. table::

       ==============   ==============
       Spyder           Spyder-Kernels
       ==============   ==============
       4.0.0-4.0.1      1.8.1
       4.1.0-4.1.2      1.9.0
       4.1.3            1.9.1
       4.1.4            1.9.3
       ==============   ==============

   To install the right version, type the following on the command line (or Anaconda Prompt on Windows)

   .. code-block:: bash

      conda install spyder-kernels=<VERSION>

   For more information, go to the :ref:`starting-kernel-problems-ref` section in the :doc:`common-illnesses` page of our troubleshooting guide.
