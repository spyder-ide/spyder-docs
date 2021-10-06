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

   For more information, visit our :doc:`/installation`.


.. dropdown:: Q: How do I install Spyder on Windows Subsystem for Linux 2 (WSL2)?
   :container: + dropdown-id-install-wsl2

   If you already installed Spyder on your Windows machine, you do not need to reinstall it on a WSL2-based Linux environment if your code must run there.

   Instead, just install `Miniconda`_ inside WSL2 and create a new conda environment (or use an existing conda- or virtualenv), then install Spyder-Kernels into that environment with e.g. ``conda install spyder-kernels``.
   You must manually install ``ipython_genutils`` with e.g. ``conda install ipython_genutils``.

   .. note::

      Windows creates a network path located at ``\\wsl$`` that points to the partitions of your WSL2 machines, e.g. ``\\wsl$\Ubuntu-20.04``.
      You **must** map a network drive letter to your machine path, e.g. ``W:``, for Spyder to correctly see its files and folders.

   To start a Spyder kernel, from your Linux terminal run

   .. code-block:: bash

      python -m spyder_kernels.console --matplotlib="inline" --ip=127.0.0.1 -f=~/remotemachine.json &

   It will run the kernel as a subprocess and create a file named :file:`remotemachine.json` in your WSL home folder.

   Finally, under the options menu of Spyder's :doc:`panes/ipythonconsole`, select :guilabel:`Connect to an existing kernel` as described in :ref:`connecting-external-kernel`.
   Insert the absolute path of :file:`remotemachine.json` into the :guilabel:`Connection file` field.
   If you mapped ``W:`` as mentioned in above note, the path should be :file:`W:/home/{username}/remotemachine.json`.
   A new console will open in Spyder, running in the Linux environment.
   Try running ``os.system('ls -la')`` and see if it lists your WSL home folder.
   If you run ``exit()`` from Spyder, the kernel running on Linux will be stopped.


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

   .. image:: /images/faq/faq-navigator-install.png
      :alt: Navigator showing installing specific version of Spyder



==============
Running Spyder
==============

.. dropdown:: Q: How do I run Spyder?
   :container: + dropdown-id-run-spyder

   You can launch it in any of the following ways:

   * **From the command line**: Type ``spyder`` in your terminal (or Anaconda prompt on Windows).

   * **From Anaconda Navigator**: Scroll to :guilabel:`Spyder` under :guilabel:`Home`, and click :guilabel:`Launch`.

     .. image:: /images/faq/faq-launch-anaconda.png
        :alt: Navigator showing running a specific version of Spyder

   * ***Windows Only***: Launch it via the Start menu shortcut.

     .. image:: /images/faq/faq-windows-launch.png
        :alt: Spyder shortcut in the Windows Start menu


.. dropdown:: Q: Can I try Spyder without installing it?
   :container: + dropdown-id-run-binder

   Yes!
   With `Binder`_, you can work with a fully functional copy of Spyder that runs right in your web browser.
   Try it `here`_.

   .. _Binder: https://mybinder.org/
   .. _here: https://mybinder.org/v2/gh/spyder-ide/spyder/5.x?urlpath=/desktop


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

   .. image:: /images/faq/faq-run-environment.png
      :alt: Navigator showing running Spyder in a specific environment


.. dropdown:: Q: How do I run Spyder installed in a conda environment using the command line?
   :container: + dropdown-id-run-terminal

   Activate your conda environment by typing the following in your terminal (or Anaconda Prompt on Windows):

   .. code-block:: bash

      conda activate <ENVIRONMENT-NAME>

   Then, type ``spyder`` to launch the version installed in that environment.



.. _using_spyder_faqs_ref:

============
Using Spyder
============

.. dropdown:: Q: How do I install Python packages to use within Spyder if I installed Spyder with conda?
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

   .. image:: /images/faq/faq-change-environment.png
      :alt: Change default environment in Preferences option in status bar

   This will open the :guilabel:`Preferences` dialog in the :guilabel:`Python interpreter` section.
   Here, select the option :guilabel:`Use the following Python interpreter`, and use the dropdown below to select your preferred environment.
   If its not listed, use the text box or the :guilabel:`Select file` button to enter the path to the Python interepreter you want to use.
   See the :doc:`/panes/ipythonconsole` for more information.

   .. image:: /images/faq/faq-python-interpreter.png
      :alt: Preferences showing changing Python interpreter

   Click :guilabel:`Restart kernel` in the :guilabel:`Consoles` menu for this change to take effect.


.. dropdown:: Q: How do I install Python packages to use within Spyder if I downloaded Spyder from the standalone installers?
   :container: + dropdown-id-using-packages-installer

   Watch our video on using additional modules or follow the instructions below it.

   .. youtube:: i7Njb3xO4Fw
      :height: 360
      :width: 640
      :align: left
      :start: 306

   If you want to use other modules in Spyder that don't come with our installer, you need to install `Miniconda`_ (**only if you don't have Anaconda or Miniconda yet!**).
   For Spyder to recognize it, the installation should be done in one of the following default paths:

   .. table::

       +------------------------------------+---------------------------------+
       |Windows                             | macOS                           |
       +====================================+=================================+
       |C:\\Users\\<username>\\Anaconda     | /Users/<username>/opt/anaconda  |
       +------------------------------------+---------------------------------+
       |C:\\Users\\<username>\\Miniconda    | /Users/<username>/opt/miniconda |
       +------------------------------------+---------------------------------+
       |C:\\Users\\<username>\\Anaconda3    | /Users/<username>/opt/anaconda3 |
       +------------------------------------+---------------------------------+
       |C:\\Users\\<username>\\Miniconda3   | /Users/<username>/opt/miniconda3|
       +------------------------------------+---------------------------------+
       |C:\\Anaconda                        |   /opt/anaconda                 |
       +------------------------------------+---------------------------------+
       |C:\\Miniconda                       |   /opt/miniconda                |
       +------------------------------------+---------------------------------+
       |C:\\Anaconda3                       |   /opt/anaconda3                |
       +------------------------------------+---------------------------------+
       |C:\\Miniconda3                      |   /opt/miniconda3               |
       +------------------------------------+---------------------------------+
       |C:\\ProgramData\\Anaconda           |                                 |
       +------------------------------------+---------------------------------+
       |C:\\ProgramData\\Miniconda          |                                 |
       +------------------------------------+---------------------------------+
       |C:\\ProgramData\\Anaconda3          |                                 |
       +------------------------------------+---------------------------------+
       |C:\\ProgramData\\Miniconda3         |                                 |
       +------------------------------------+---------------------------------+

   .. _Miniconda: https://docs.conda.io/en/latest/miniconda.html

   Then, you need to create a new conda environment with the modules that you want to use with Spyder and include ``spyder-kernels`` in it. For example, if you want to use ``scikit-learn``, open your terminal or the Anaconda prompt on Windows and run the following commands:

   .. code-block:: bash

      conda create -n spyder-env -y
      conda activate spyder-env
      conda install spyder-kernels scikit-learn -y

   Finally, you need to connect Spyder to this environment by changing Spyder’s default Python interpreter. To do this, click the name of the current environment in the status bar, and then click :guilabel:`Change default environment in Preferences`.

   This will open the :guilabel:`Preferences` dialog in the :guilabel:`Python interpreter` section. Here, select the option :guilabel:`Use the following Python interpreter`, and use the dropdown below to select your preferred environment. If it is not listed, use the text box or the :guilabel:`Select file` button to enter the path to the Python interpreter you want to use.

   **Your new environment will only be listed here if you installed Miniconda (or Anaconda) in the default path as shown in the table above.**

   Click :guilabel:`Restart kernel` in the :guilabel:`Consoles` menu for this change to take effect.


.. dropdown:: Q: How do I reset Spyder's preferences to the defaults?
   :container: + dropdown-id-using-reset-prefs

   Either use the :guilabel:`Reset Spyder to factory defaults` under :guilabel:`Tools` in Spyder's menu bar, the :guilabel:`Reset Spyder settings` Start menu shortcut (Windows), or run ``spyder --reset`` in your system terminal (Anaconda prompt on Windows).

   .. image:: /images/faq/faq-reset-spyder.png
      :alt: Spyder reset button in tools


.. dropdown:: Q: How do I change Spyder's language?
   :container: + dropdown-id-using-change-language

   Under :guilabel:`General` in Spyder's :guilabel:`Preferences`, go to the :guilabel:`Advanced settings` tab and select your language from the options displayed under :guilabel:`Language`.

   .. image:: /images/faq/faq-change-language.png
      :alt: Spyder change language in preferences.


.. dropdown:: Q: How do I use code cells in Spyder?
   :container: + dropdown-id-using-code-cells

   To create a cell in Spyder's :doc:`/panes/editor`, type ``#%%`` in your script.
   Each ``#%%`` will make a new cell.
   To run a cell, press :kbd:`Shift-Enter` (while your cursor is focused on it) or use the :guilabel:`Run current cell` button in Spyder's toolbar.

   .. image:: /images/faq/faq-cells.png
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

   .. image:: /images/faq/faq-remove-variables.png
      :alt: Spyder showing cell generation.


.. dropdown:: Q: How do I run my code in a dedicated console or an external system terminal?
   :container: + dropdown-id-using-dedicated-console

   Select the appropriate option in the :guilabel:`Configuration per file...` dialog under the :guilabel:`Run` menu.

   .. image:: /images/faq/faq-run-options.png
      :alt: Spyder showing cell generation.


.. dropdown:: Q: How do I change the syntax highlighting theme in the Editor?
   :container: + dropdown-id-using-syntax-theme

   Go to :guilabel:`Preferences` and select the theme you want under :guilabel:`Syntax highlighting theme` in the :guilabel:`Appearance` section.

   .. image:: /images/faq/faq-highlighting-theme.png
      :alt: Spyder showing cell generation.



===============
Troubleshooting
===============

.. dropdown:: Q: I've found a bug or issue with Spyder. What do I do?
   :container: + dropdown-id-troubleshooting-spyder

   You should first follow the steps in our :doc:`troubleshooting guide</troubleshooting/first-steps>`.
   If you can't solve your problem, open an issue by following the instructions in our :doc:`/troubleshooting/submit-a-report` section.


.. dropdown:: Q: I get an error in the IPython console running my code! Help!
   :container: + dropdown-id-troubleshooting-running-code

   First, make sure the error you are seeing is not a bug in your code.
   To confirm this, try running it in any standard Python interpreter.
   If the error still occurs, the problem is likely with your code and a site like `Stack Overflow`_ might be the best place to start.
   Otherwise, start at the :doc:`/troubleshooting/basic-first-aid` section of our troubleshooting guide.

   .. _Stack Overflow: https://stackoverflow.com


.. dropdown:: Q: Code completion/help doesn't work; what can I do?
   :container: + dropdown-id-troubleshooting-completion

   If nothing is displayed in the calltip, hover hint or :doc:`/panes/help` pane, make sure the object you are inspecting has a docstring, and try executing your code in the :doc:`/panes/ipythonconsole` to get help and completions there.
   If this doesn't work, try restarting PyLS by right-clicking the :guilabel:`LSP Python` label item in the statusbar at the bottom of Spyder's main window, and selecting the :guilabel:`Restart Python Language Server` option.

   For more information, go to the :ref:`code-completion-problems-ref` section in the :doc:`/troubleshooting/common-illnesses` page of our troubleshooting guide.


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
       4.1.5-4.1.6      1.9.4
       4.2.0            1.10.0
       ==============   ==============

   To install the right version, type the following on the command line (or Anaconda Prompt on Windows)

   .. code-block:: bash

      conda install spyder-kernels=<VERSION>

   For more information, go to the :ref:`starting-kernel-problems-ref` section in the :doc:`/troubleshooting/common-illnesses` page of our troubleshooting guide.


.. dropdown:: Q: Spyder doesn't launch or is slow on macOS Big Sur. How can I get it working?
   :container: + dropdown-id-troubleshooting-macos-bigsur

   Spyder is in the final stages of being updated for full compatibility with macOS 11 Big Sur, which will be released by the end of 2020 as part of version 4.2.1.
   However, you can get it working right now with the workaround below.
   Make sure you have the Anaconda or Miniconda distribution installed, and run the following commands in the Terminal to install Spyder from Conda-Forge in a clean environment:

    .. code-block:: bash

       conda create -n spyder-dev python=3
       conda activate spyder-dev
       conda install -c conda-forge spyder

   Then, whenever you want to start Spyder, run the following from the Terminal:

   .. code-block:: bash

      conda activate spyder-dev
      export QT_MAC_WANTS_LAYER=1
      spyder



============
About Spyder
============

.. dropdown:: Q: What's Spyder's licensing situation? Is commercial use allowed?
   :container: + dropdown-id-commercial-use

   Spyder is 100% free and open source; there is no paid version or prohibition on commercial use.
   It is developed by its international user community, and supported by its users through `OpenCollective`_ and by its generous sponsoring organizations, including `Quansight`_ and `NumFOCUS`_.
   Our source code, standalone installers and most of our distribution methods (Pip/PyPI, Linux distros, MacPorts, WinPython, etc) can be freely redistributed, used and modified by anyone, for any purpose, including commercial use.
   For more details about the situation with Anaconda, see `that question`_.

   .. _OpenCollective: https://opencollective.com/spyder
   .. _Quansight: https://www.quansight.com/
   .. _NumFOCUS: https://numfocus.org/
   .. _that question: #anaconda-license


.. dropdown:: Q: What do the Anaconda licensing changes mean for Spyder?
   :container: + dropdown-id-anaconda-license

   If you use Spyder with the Anaconda distribution, they `recently changed`_ their `Terms of Service`_ to add restrictions on large (> 200 employee) for-profit companies using Anaconda on a large scale.
   However, these terms only apply to the package infrastructure (the full Anaconda distribution and the ``defaults`` conda channel).
   Instead, you can simply download the similar `Miniforge distribution`_, which is 100% open source and identical to full Anaconda (aside from not bundling the Python packages installed by default in the Anaconda ``base`` environment, which we recommend you avoid using anyway given any problems here can break your whole installation).
   Then, simply install the packages you need (including Spyder, if you aren't using our recommended :ref:`standalone_installers_ref`) with ``conda`` as you usually do.
   Miniforge will automatically use the community-maintained Conda-Forge repository, which has a much wider variety of packages and is generally more up to date than the Anaconda equivalent, in addition to being free of any commercial restrictions.
   For more, see our :doc:`/installation`.

   .. _recently changed: https://www.anaconda.com/blog/sustaining-our-stewardship-of-the-open-source-data-science-community
   .. _Terms of Service: https://www.anaconda.com/terms-of-service
   .. _Miniforge distribution: https://github.com/conda-forge/miniforge/releases/latest
