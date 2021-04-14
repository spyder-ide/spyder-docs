#################
Variable Explorer
#################

The **Variable Explorer** allows you to interactively browse and manage the objects generated running your code.

.. image:: /images/variable_explorer/variable-explorer-execution.gif
   :alt: Spyder Variable Explorer execution with a variable of type list

It shows the namespace contents (including all global objects, variables, class instances and more) of the currently selected :doc:`ipythonconsole` session, and allows you to add, remove, and edit their values through a variety of GUI-based editors.

.. image:: /images/variable_explorer/variable-explorer-standard.png
   :alt: Spyder Variable Explorer, with a list of variables and their contents

The Variable Explorer gives you information on the name, size, type and value of each object.
To modify a scalar variable, like an number, string or boolean, simply double click it in the pane and type its new value.

.. image:: /images/variable_explorer/variable-explorer-modifying.gif
   :alt: Spyder Variable Explorer modifying value of a variable



==============
Object viewers
==============

Spyder's :guilabel:`Variable Explorer` offers built in support for editing lists, strings, dictionaries, NumPy arrays, Pandas DataFrames, Series and more; as well as being able to plot and visualize them with one click.


Strings
~~~~~~~

When a string variable is longer than forty characters, you can double click it to see its value in a text editor to more easily modify it.

.. image:: /images/variable_explorer/variable-explorer-text-long.png
   :width: 500
   :alt: Variable Explorer text editor, displaying a long string in a window


Dictionaries
~~~~~~~~~~~~

Double-clicking on dictionaries will show a viewer displaying each of its keys with its associated value.
You can double click any of the values to modify them, which will open a new viewer if the value is itself an object.

.. image:: /images/variable_explorer/variable-explorer-dictionary.png
   :width: 500
   :alt: Dictionary editor displaying keys and their types, sizes, and values


Lists
~~~~~

For lists, the main Variable Explorer displays a preview of the first ten values.
To see them all, double click the list to open a viewer that will display the index, type, size and value of each element of the list.
Just like dictionaries, you can double-click values to edit them.

.. image:: /images/variable_explorer/variable-explorer-list.png
   :width: 500
   :alt: List editor displaying a list, showing one being edited


Numpy arrays
~~~~~~~~~~~~

Like lists, for Numpy arrays the Variable Explorer shows a preview of their values.
Double-clicking them will open a viewer displaying the array values in a "heat map", with each value in a grid cell colored based on its numeric quantity.
You can deactivate the background color by unchecking the appropriate option in the viewer, which will happen automatically if the array is too large to improve performance.

.. image:: /images/variable_explorer/variable-explorer-heat-map.png
   :alt: Array editor array, displaying a "heatmap" of its values

If supported by the datatype, you can also change the format of the array's values, choosing the number of decimals that you want the array to display.
For this, click the :guilabel:`Format` button and and set the desired formatting in the dialog that appears, using standard `Printf-style syntax`_.

.. _Printf-style syntax: https://docs.python.org/3/library/stdtypes.html#printf-style-bytes-formatting

Additionally, you can adjust the size of the rows and columns of the array by expanding or contracting their headers.
Clicking the :guilabel:`Resize` button will set it automatically.

.. image:: /images/variable_explorer/variable-explorer-resize.gif
   :alt: Array editor with a 2D int array, showing resizing of columns


DataFrames
~~~~~~~~~~

DataFrames, like Numpy arrays, display in a viewer where you can show or hide "heatmap" colors, change the format and resize the rows and columns either manually or automatically.

.. image:: /images/variable_explorer/variable-explorer-dataframe.png
   :alt: Dataframe editor showing data frame "heatmap"

Additionally, starting in Spyder 4, the Variable Explorer has MultiIndex support in its DataFrame inspector, including for multi-level and multi-dimensional indices.


.. image:: /images/variable_explorer/variable-explorer-multi-index.png
   :alt: Dataframe editor showing multi-index support



============
Options menu
============

The options menu in the top right of the Variable Explorer pane allows you filter the objects shown by a number of different criteria.

.. image:: /images/variable_explorer/variable-explorer-menu.png
   :alt: Spyder Variable Explorer, with options menu

It also allows you to display the min and max of Numpy arrays instead of a preview of their values.

.. image:: /images/variable_explorer/variable-explorer-array-min-max.png
   :width: 500
   :alt: Variable Explorer showing max and min values of numpy array



===============
Toolbar buttons
===============

The Variable Explorer's toolbar includes several useful features that affect the entire namespace.
For example, you can save the current session's data as a ``.spydata`` file, which can be loaded later to recover all the variables stored.

.. image:: /images/variable_explorer/variable-explorer-import-data.gif
   :alt: Variable Explorer showing how to save and import data

There is also a button to remove all displayed variables, and a search box to find objects by  name or type.

.. image:: /images/variable_explorer/variable-explorer-search.gif
   :alt: Variable Explorer showing how to search variables

Finally, there is a button to refresh the Variable Explorer's contents, which will update it to show the current state of the code running in the IPython console.



======================
Advanced functionality
======================

The context menu, available by right-clicking any variable, provides numerous additional options to interact with objects of various types.
These include renaming, removing or editing existing variables, as well as the :guilabel:`duplicate` option to create a new copy of one of them under a new name you enter in the resulting dialog box.

.. image:: /images/variable_explorer/variable-explorer-duplicate.gif
   :alt: Variable Explorer showing duplicating a variable

Furthermore, you can copy and paste the value of a variable, saving it in the Variable Explorer with any name that you choose.
This allows you to change the type of the variable that you are pasting which can be very useful, allowing you to, for example, easily copy the elements of a list into an array.

.. image:: /images/variable_explorer/variable-explorer-copy-paste.gif
   :alt: Variable Explorer showing copying list into array

Additionally, you can create an object from scratch directly in the Variable Explorer with the :guilabel:`Insert` option, which allows you to type the key (which should be in quotation marks) and the value for the item that you want to insert.
In addition to adding a new top-level variable, this feature also allows you to create a new key in a dictionary, a new element in a list, and much more.

.. image:: /images/variable_explorer/variable-explorer-insert.gif
   :alt: Variable Explorer showing insertion of a new variable

For lists and Numpy arrays, more advanced options are available, including generating plots and histograms of their values appropriate to their type and dimensions.

.. image:: /images/variable_explorer/variable-explorer-histogram-plot.gif
   :alt: Plot window showing a plot, generated via the previous options

You can even save an array to a ``.npy`` file by simply clicking the appropriate option, which can later be loaded by Spyder or in your code via ``numpy.load()``.

.. image:: /images/variable_explorer/variable-explorer-contextmenu-array.png
   :width: 500
   :alt: Context menu for an int array, with the Show image option selected

For two-dimensional arrays, you can also display them as images, treating their values as RGB colors. For this, Spyder uses Matplotlib's colormaps, which can be `easily changed to match your preferences`_.

.. _easily changed to match your preferences: https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

.. image:: /images/variable_explorer/variable-explorer-show-image.gif
   :alt: Interactive image based on the array's data

Finally, we added a context-menu action to open any object using the new Object Explorer even if they already have a builtin viewer (DataFrames, arrays, etc), allowing for deeper inspection of the inner workings of these datatypes.

.. image:: /images/variable_explorer/variable-explorer-object-explorer.png
   :alt: Object explorer showing dataframe



==================
Related components
==================

* :doc:`debugging`
* :doc:`ipythonconsole`
