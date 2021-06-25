###############
Spyder Notebook
###############

**Spyder-notebook** is a plugin that allows you to open, edit and interact with Jupyter Notebooks right inside Spyder.

.. image:: /images/console/console-standard.png
   :alt: Spyder Notebook in Spyder

Using notebooks inside of Spyder allows you to take advantage of its web interface alongside Spyder’s powerful features such as the Variable explorer, the console and the debugger.

=======================
Installing the Notebook
=======================

If you installed Spyder using conda, the best way to install the the Notebook is to run the following in your terminal or Anaconda prompt on Windows:

.. code-block:: bash

   conda install spyder-notebook -c spyder-ide

.. important::

   At the moment it is not possible to use this plugin with the Spyder installers for Windows and macOS. We're working to make that possible in the future.

Restart Spyder in order to be able to use the plugin.

==================
Using the Notebook
==================

When the Notebook is installed, it will be available under the menu item :menuselection:`View --> Panes --> Notebook`.

.. image:: /images/console/console-standard.png
   :alt: Spyder showing view panes Notebook

You will see it then as a tab in the bottom of the editor area. When switching to it, you will see a welcome screen, from where you can create a new notebook by right-clicking it and selecting :guilabel:`New notebook`.

.. image:: /images/console/console-standard.png
   :alt: Spyder with context menu showing new notebook option

You can also click the :guilabel:`Plus` button at the top right of the pane. A new Jupyter Notebook will be opened as a tab, ready for user input in temporary space. This can serve as a scratch pad where you can do quick calculations and plots.

.. image:: /images/console/console-standard.png
   :alt: Spyder showing a new notebook

To save this notebook go to the options menu at the top right of the pane and click the :guilabel:`Save as...` option. This will store your notebook locally with ``ipynb`` extension which will allow you to open it then as a Jupyter Notebook outside of Spyder.

.. image:: /images/console/console-standard.png
   :alt: Gif showing save as

You can also open any Jupyter Notebook inside Spyder. For this go to the options menu at the top right of the pane and click :guilabel:`Open` which will allow you to browse the files in your computer. Click any notebook that you want to open inside Spyder and you will be able to see it as a new tab in the Notebook pane.

.. image:: /images/console/console-standard.png
   :alt: Gif showing opening a Jupyter notebook inside Spyder

The :guilabel:`Open recent` option displays a list of the recent notebooks you opened in Spyder from which you can select them and open them in Spyder too.

=============================
Connecting an Ipython Console
=============================

You can connect an Ipython Console to your notebook which will allow you to view the variables of your notebook in the :guilabel:`Variable Explorer`. To do so, go to the options menu and click the :guilabel:`Open console` option. This will open a new console with the same name of your notebook and display in the Variable Explorer, the variables of the cells that you have executed preciously in your Notebook.

.. image:: /images/console/console-standard.png
   :alt: Gif showing connecting console and displaying variables

You can view, modify and create new ones in the console.

Since the Variable Explorer is associated to each console, closing the notebook's console will immediately delete the variables from your variable explorer.

==================
Additional Options
==================

The context menu, available by right-clicking pane area outside of the notebook, allows you to zoom your notebook in or out.

.. image:: /images/console/console-standard.png
   :alt: Gif zooming in and out the notebook.

You can also select the code from your Notebook and copy it on your clipboard to paste this code anywhere you want.

.. image:: /images/console/console-standard.png
   :alt: Gif copying and pasting

Finally, you can see all the server information of your notebook by clicking the :guilabel:`Server info` option in the context menu.

.. image:: /images/console/console-standard.png
   :alt: Server info for notebook in Spyder
