:orphan:

###############
Spyder Notebook
###############

**Spyder-notebook** is a plugin that allows you to open, edit and interact with Jupyter Notebooks right inside Spyder.

.. image:: /images/notebook/notebook-standard.png
   :alt: Spyder Notebook in Spyder

Using notebooks inside Spyder allows you to take advantage of their web interface alongside Spyder’s powerful features such as the Variable explorer, console and debugger.

=======================
Installing the Notebook
=======================

If you installed Spyder using conda, the best way to install Spyder-notebook is to run the following command in your terminal or Anaconda prompt on Windows:

.. code-block:: bash

   conda install spyder-notebook -c spyder-ide

.. important::

   At the moment it is not possible to use this plugin with the Spyder :ref:`standalone_installers_ref` for Windows and macOS. We're working to make that possible in the future.

Restart Spyder in order to be able to use the plugin.

==================
Using the Notebook
==================

When the Notebook is installed, it will be available under the menu item :menuselection:`View --> Panes --> Notebook`.

.. image:: /images/notebook/notebook-view-panes.png
   :alt: Spyder showing view panes Notebook

You will see it then as a tab in the bottom of the editor area. When switching to it, a welcome screen will be displayed, from where you can create a new notebook by right-clicking it and selecting :guilabel:`New notebook`.

.. image:: /images/notebook/notebook-new-notebook-option.png
   :alt: Spyder with context menu showing new notebook option

You can also click the :guilabel:`Plus` button at the top right of the pane. A new Jupyter Notebook will be opened as a tab, ready for user input in a temporary file. This can serve as a scratch pad where you can do quick calculations and plots.

.. image:: /images/notebook/notebook-new-notebook.png
   :alt: Spyder showing a new notebook

To save this notebook go to the options menu at the top right of the pane and click the :guilabel:`Save as...` option. This will store your notebook locally with the ``ipynb`` extension, which will allow you to open it then as a Jupyter Notebook outside of Spyder.

.. image:: /images/notebook/notebook-save.gif
   :alt: Gif showing save as

You can also open any Jupyter Notebook inside Spyder. For this go to the options menu at the top right of the pane and click :guilabel:`Open`, which will allow you to look for ``ipynb`` files in your computer. Click any notebook that you want to open inside Spyder and you will be able to see it as a new tab in the Notebook pane.

.. image:: /images/notebook/notebook-open.gif
   :alt: Gif showing opening a Jupyter notebook inside Spyder

The :guilabel:`Open recent` option displays a list of the recent notebooks you opened in Spyder, from which you can select them and open them again in Spyder.

=============================
Connecting an IPython Console
=============================

You can connect an :doc:`/panes/ipythonconsole` to your notebook, which will allow you to view your variables in the :doc:`/panes/variableexplorer`. To do so, go to the options menu and click the :guilabel:`Open console` option. This will open a new console with the same name of your notebook and display the variables of the cells that you have executed previously in your Notebook. If you don't see them, press :kbd:`Enter` in the console.

.. image:: /images/notebook/notebook-console.gif
   :alt: Gif showing connecting console and displaying variables

You can view, modify and create new ones in the console too.

Since the Variable Explorer is associated to each console, closing the notebook's console will immediately hide the variables from the Variable Explorer.

==================
Additional Options
==================

The context menu, available by right-clicking the pane area outside the notebook, allows you to zoom your notebook in or out.

.. image:: /images/notebook/notebook-zoom.gif
   :alt: Gif zooming in and out the notebook.

You can also select the code from your Notebook and copy it on your clipboard to paste this code anywhere you want.

.. image:: /images/notebook/notebook-copy-paste.gif
   :alt: Gif copying and pasting

Finally, you can see all the server information of your notebook by clicking the :guilabel:`Server info` option in the context menu.

.. image:: /images/notebook/notebook-server-info.png
   :alt: Server info for notebook in Spyder
