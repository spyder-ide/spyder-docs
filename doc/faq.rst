##########################
Frequently asked questions
##########################

=======================
Installing and updating
=======================

.. dropdown:: Q: How do I install Spyder?

   The easiest way to install Spyder is with Anaconda Python distribution, which comes with everything you need to get started in an all-in-one package. Download it from its `webpage`_.

   .. _webpage: https://www.anaconda.com/products/individual

   For more information visit our :doc:`installation`.

.. dropdown:: Q: How do I update Spyder using conda?

   From the command line (or Anaconda prompt on Windows) run:

   .. code-block:: bash
   
      conda update anaconda
      conda update spyder

   If this doesn't work try:

   .. code-block:: bash
   
      conda update anaconda
      conda install spyder=4

.. dropdown:: Q: How do update I Spyder using Anaconda Navigator?

   Open the preferences menu in the Spyder's section in the Navigator. Go to "install specific version" and select the version of Spyder you want to install.

   .. image:: images/FAQ/FAQ-Navigator-install.png
     :alt: Navigator showing installing specific version of Spyder



==============
Running Spyder
==============

.. dropdown:: Q: How do I run Spyder?
   
   You can run Spyder in any of the following ways:

   #. **From the command line**: Type ``spyder`` in your command line (or Anaconda prompt on Windows).

   #. **From Anaconda Navigator**: Scroll to Spyder under Home, and click Launch.

      .. image:: images/FAQ/FAQ-launch-anaconda.png
         :alt: Navigator showing running a specific version of Spyder

   #. ***Windows Only***: Launch it via the Start menu shortcut. 

      .. image:: images/FAQ/FAQ-windows-launch.png
         :alt: Navigator showing running a specific version of Spyder

.. dropdown:: Q: Can I try Spyder without installing it?

   Yes! With `Binder`_ you can work with a fully functional copy of Spyder online that runs right in your web browser. Try it `here`_.

   .. _Binder: https://mybinder.org/
   .. _here: https://mybinder.org/v2/gh/spyder-ide/spyder/4.x?urlpath=/desktop

.. dropdown:: Q: What are the system requirements for Spyder? How resource-intensive is it?

   Spyder works on modern versions of Windows, macOS and Linux (see table below for recommended versions) via Anaconda, as well as other methods. It typically uses relatively minimal CPU when idle, and 0.5 GB - 1 GB of RAM, depending on how long you've been using it and how many files, projects, panes and consoles you have open. It should work on any system with a dual-core or better x64 processor and at least 4 GB of RAM, although 8 GB is strongly recommended for best performance when running other applications. However, the code you run, such as scientific computation and deep learning models, may require additional resources beyond this baseline for Spyder itself.

   .. table:: 

      ================   ===================
      Operative system   Version
      ================   ===================
      Windows            Windows 8
      macOS              High Sierra (10.13)
      Linux              Ubuntu 16.04
      ================   ===================

.. dropdown:: Q: How do I run Spyder in a conda environment using Anaconda Navigator?

   Select the environment you want to launch Spyder from under "Applications on:". If Spyder is installed in this environment, you will see it on Navigator's Home window. Click `Launch` to use Spyder with your selected environment. 

   .. image:: images/FAQ/FAQ-run-environment.png
      :alt: Navigator showing running Spyder in a specific environment

.. dropdown:: Q: How do I run Spyder in a conda environment using the command line?

   Activate your conda environment typing on your command line (or Anaconda Prompt on Windows):

   .. code-block:: bash
   
      conda activate <ENVIRONMENT-NAME>
   
   Then, type ``spyder``.



============
Using Spyder
============

.. dropdown:: Q: How do I install Python packages to use within Spyder?

   The first approach for installing a package should be using conda. In your command line (or Anaconda Prompt on Windows) type:

   .. code-block:: bash

      conda install <PACKAGE-NAME>

   If your installation is not successful go through steps 3 to 5 of Part 2 in our `video`_ on solving and avoiding problems with pip, Conda and Conda-Forge. 

   .. _video: https://www.youtube.com/watch?v=Ul79ihg41Rs&t=306s

.. dropdown:: Q: How do I get Spyder to work with my existing Python packages/environment?

   To work with an existing environment in Spyder, change Spyder’s default python interpreter. To do so, first go to your terminal, type ``conda info --envs``, and copy the path from the environment you created to your clipboard. 

   .. image:: images/FAQ/faq-conda-info.png
      :alt: Navigator showing installing specific version of Spyder

   Now, go to :guilabel:`Preferences` in Spyder’s main window, click :guilabel:`Python interpreter`, check :guilabel:`Use the following Python interpreter` paste the path and add `/bin/python` at the end for Mac and Linux or `/python.exe` in Windows.

   .. image:: images/FAQ/faq-python-interpreter.png
      :alt: Navigator showing installing specific version of Spyder

   Restart Spyder for these changes to take effect. 

.. dropdown:: Q: How do I reset Spyder's preferences to the defaults?

   Either use the :guilabel:`Reset Spyder to factory defaults` under :guilabel:`Tools` in Spyder's menu bar, the `Reset Spyder settings` start menu shortcut (Windows), or run ``spyder --reset`` in your system terminal (Anaconda prompt on Windows).

   .. image:: images/FAQ/faq-reset-Spyder.png
      :alt: Spyder reset botton in tools

.. dropdown:: Q: How do I change Spyder's language?

   Go to :guilabel:`Preferences`. Under :guilabel:`General` go to :guilabel:`Advanced settings` and select your language from the options displayed under :guilabel:`Language`.

   .. image:: images/FAQ/faq-change-language.png
      :alt: Spyder change language in preferences.

.. dropdown:: Q: How do I use code cells in Spyder?

   To create a cell in Spyder's Editor type ``#%%`` in your script. Each ``#%%`` will determine a new cell. To run a cell, press shift+enter while in focus of a cell or use the :guilabel:`Run current cell` icon in the Icon Bar.

   .. image:: images/FAQ/faq-cells.png
      :alt: Spyder showing cell generation.

.. dropdown:: Q: How do I use plugins with Spyder (e.g. Spyder-Notebook, Spyder-Terminal, Spyder-Unittest)?

   Spyder plugins are available in the spyder-ide channel in Anaconda. To install them type in your command line (or Anaconda Prompt on Windows):

   .. code-block:: bash

      conda install -c spyder-ide <PLUGIN>

   Replace <PLUGIN> for the name of the plugin you want to use. For more information go to the Plugins' repository:

   * `spyder-reports`_
   * `spyder-unittest`_
   * `spyder-terminal`_
   * `spyder-notebook`_
   * `spyder-memory-profiler`_
   * `spyder-line-profiler`_
   * `spyder-vim`_
   * `spyder-autopep8`_

   .. _spyder-reports: https://github.com/spyder-ide/spyder-reports
   .. _spyder-unittest: https://github.com/spyder-ide/spyder-unittest
   .. _spyder-terminal: https://github.com/spyder-ide/spyder-terminal
   .. _spyder-notebook: https://github.com/spyder-ide/spyder-notebook
   .. _spyder-memory-profiler: https://github.com/spyder-ide/spyder-memory-profiler
   .. _spyder-line-profiler: https://github.com/spyder-ide/spyder-line-profiler
   .. _spyder-vim: https://github.com/spyder-ide/spyder-vim
   .. _spyder-autopep8: https://github.com/spyder-ide/spyder-autopep8

.. dropdown:: Q: How do I clear all my variables before executing my code?

   Check the option :guilabel:`Remove all variables before execution` in the :guilabel:`Configuration per file...`
   dialog under :guilabel:`Run` in the Menu bar.

   .. image:: images/FAQ/faq-remove-variables.png
      :alt: Spyder showing cell generation.

.. dropdown:: Q: How do I run my code in a dedicated console or an external system terminal?
   
   Select the option in the :guilabel:`Configuration per file...` dialog under :guilabel:`Run` in the Menu bar.

   .. image:: images/FAQ/faq-run-options.png
      :alt: Spyder showing cell generation.

.. dropdown:: Q: How do I change the syntax highlighting theme?

   Go to :guilabel:`Preferences` and select the theme under :guilabel:`Syntax highlighting theme in the :guilabel:`Appearence` section.

   .. image:: images/FAQ/faq-highlighting-theme.png
      :alt: Spyder showing cell generation.



===============
Troubleshooting
===============

.. dropdown:: Q: I've found a bug or issue with Spyder, what do I do?

   You should first follow the steps in our Troubleshooting guide. If you can't solve your bug, open an issue by following the instructions in our Submit a Report section.

.. dropdown:: Q: I get an error in the IPython console running my code! Help!

   First, make sure the error you are having is not an error with your code. For this, try running it in any standard Python interpreter. If it turns out the error is with your code, `Stack Overflow`_ might be the best place to start. Otherwise, start at the Basic First Aid section of our troubleshooting guide.

   .. _Stack Overflow: https://stackoverflow.com

.. dropdown:: Q: Code completion/help doesn't work; what can I do?

   If nothing is displayed in the calltip, hover hint or help pane, make sure the object you are inspecting has a docstring and try executing your code in the :doc:`ipythonconsole` to get help and completions on the object there. If this doesn't work, try restarting the LSP by right-clicking it in the bottom of Spyder's main window and selecting the :guilabel:`Restart Python Language Server` item.

   For more information go to the Completion/help not working component in the Common Illnesses section of our troubleshooting guide.

.. dropdown:: Q: I get the message "An error occurred while starting the kernel". How do I fix it?

   First make sure your version of spyder-kernels is compatible with your version of Spyder.
 
    .. table:: 

       ==============   ==============
       Spyder           Spyder-Kernels
       ==============   ==============
       4.0.0-4.0.1      1.8.1
       4.1.0-4.1.2      1.9.0
       4.1.3            1.9.1
       4.1.4            1.9.2   
       ==============   ==============
   
   To install the right version, type on your command line (or Anaconda Prompt on Windows)

   .. code-block:: bash

    conda install spyder-kernels=<VERSION>

   For more information go to the Errors starting the kernel component in the Common Illnesses section of our troubleshooting guide.
