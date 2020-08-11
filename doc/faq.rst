##########################
Frequently asked questions
##########################

=======================
Installing and updating
=======================

.. dropdown:: Q: How do I install Spyder?


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

.. dropdown:: Q: What are the system requirements for Spyder? How 			resource-intensive is it?

   Spyder works on modern versions of Windows, macOS and Linux via Anaconda, as well as other methods. It typically uses relatively minimal CPU when idle, and 0.5 GB - 1 GB of RAM, depending on how long you've been using it and how many files, projects, panes and consoles you have open. It should work on any system with a dual-core or better x64 processor and at least 4 GB of RAM, although 8 GB is strongly recommended for best performance when running other applications. However, the code you run, such as scientific computation and deep learning models, may require additional resources beyond this baseline for Spyder itself.

   Windows 8
   Mac 10.13
   Ubuntu 

.. dropdown:: Q: How do I run Spyder in a conda environment using Anaconda Navigator?

   .. image:: images/FAQ/FAQ-run-environment.png
      :alt: Navigator showing running Spyder in a specific environment

.. dropdown:: Q: How do I run Spyder in a conda environment using the command line?



============
Using Spyder
============

.. dropdown:: Q: How do I install Python packages to use within Spyder?

   Following Part 2, steps 2-4 of pip-conda video

.. dropdown:: Q: How do I get Spyder to work with my existing Python packages/environment?

   Following Part 2 Step 5 of pip-conda video, and "packages and environments with Spyder" guide

.. dropdown:: Q: How do I reset Spyder's preferences to the defaults?

   Either use the :guilabel:`Reset to defaults` button in Spyder's :guilabel:`Preferences` windows, the `Reset Spyder settings` start menu shortcut (Windows), or run ``spyder --reset`` in your system terminal (Anaconda prompt on Windows).

   TOOOLS

.. dropdown:: Q: How do I change Spyder's language?

	asjkdajlskdasd

.. dropdown:: Q: How do I use code cells in Spyder?

   General info how to create and run a code cell

.. dropdown:: Q: How do I use plugins with Spyder (e.g. Spyder-Notebook, Spyder-Terminal, Spyder-Unittest)?

   Brief description of installing from conda-forge, etc.

.. dropdown:: Q: How do I change the way Spyder runs my code (e.g. clear variables before execution, run in a dedicated console or external system terminal)?
	
	(Separated in 3)	

   Use the options in :guilabel:`Run configuration per file...`

.. dropdown:: Q: How do I use global variables in Spyder (CARLOS)?

   Run -> Run configuration file -> General settings -> second option

.. dropdown:: Q: How do I change the syntax highlighting theme?

   ajlklaksdjlasd

===============
Troubleshooting
===============

.. dropdown:: Q: I've found a bug or issue with Spyder, what do I do?

   Troubleshooting guide then search issue tracker then follow the issue submission instructions

.. dropdown:: Q: I get an error in the IPython console running my code! Help!

   Discuss the difference between an error with your code and with Spyder. Ref standard troubleshooting procedure, the note in the introductory section and general Python resources.

.. dropdown:: Q: Code completion/help doesn't work; what can I do?

   Summary of the completion section I wrote in the common illnesses section


.. dropdown:: Q: I get the message "An error occurred while starting the kernel". How do I fix it?

   Summary of the spyder-kernels section I wrote in the common illnesses section





