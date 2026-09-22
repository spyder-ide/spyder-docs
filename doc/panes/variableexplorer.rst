.. _panes-variables:

#################
Variable Explorer
#################

The **Variable Explorer** allows you to interactively browse and manage the data and objects created by your code.

.. image:: /images/variable_explorer/variable-explorer-execution.gif
   :alt: Spyder Variable Explorer execution with a variable of type list

It shows the namespace contents (including all global objects, variables, class instances and more) of the currently selected :ref:`panes-console` session, and allows you to add, remove, and edit their values through a variety of GUI-based editors.

.. image:: /images/variable_explorer/variable-explorer-standard.png
   :alt: Spyder Variable Explorer, with a list of variables and their contents

The Variable Explorer gives you information on the name, size, type and value of each object.
To modify a scalar variable, like an number, string or boolean, simply double click it in the pane and type its new value.

.. image:: /images/variable_explorer/variable-explorer-modifying.gif
   :alt: Spyder Variable Explorer modifying value of a variable



.. _panes-variables-viewers:

==============
Object viewers
==============

The :guilabel:`Variable Explorer` offers built in support for editing lists, strings, dictionaries, NumPy arrays, Pandas DataFrames, Series and more; as well as being able to plot and visualize them with one click.

Every viewer has a refresh button, which updates the displayed object to the current value of the variable if it has changed in the meantime.
Click any column to sort by it, ascending or descending, and if the object is editable you can double-click any cell to change its value, which will open a new viewer if that object isn't a basic scalar data type (int, float, string).


.. _panes-variables-viewers-str:

Strings
~~~~~~~

When a string variable is longer than forty characters, you can double-click it to see its value in a text editor to modify it more easily.

.. image:: /images/variable_explorer/variable-explorer-text-long.png
   :width: 500
   :alt: Variable Explorer text editor, displaying a long string in a window


.. _panes-variables-viewers-dict:

Dictionaries
~~~~~~~~~~~~

Double-clicking on dictionaries will show a viewer displaying each of its keys with its associated value.
The Toolbar buttons allow you to insert, duplicate and remove individual key-value pairs and adjust the row and column width, as well as view the dictionary as a generic object.

.. image:: /images/variable_explorer/variable-explorer-dictionary.png
   :width: 500
   :alt: Dictionary editor displaying keys and their types, sizes, and values


.. _panes-variables-viewers-list:

Lists
~~~~~

For lists, the main Variable Explorer pane displays a preview of the first ten values.
To see them all, double click the list to open a viewer that will display the index, type, size and value of each element of the list.
Just like dictionaries, you can double-click values to edit them, and use the toolbar to insert, duplicate or delete them, along with options to resize and open in the object explorer.

.. image:: /images/variable_explorer/variable-explorer-list.png
   :width: 500
   :alt: List editor displaying a list, showing one being edited


.. _panes-variables-viewers-array:

NumPy arrays
~~~~~~~~~~~~

Like lists, for NumPy arrays the Variable Explorer shows a preview of their values.
Double-clicking them will open a viewer displaying the array values in a "heat map", with each value in a grid cell colored based on its numeric quantity.
You can deactivate this by selecting the :guilabel:`Use default background color` option in the :guilabel:`Display options` dialog under the pane options ("hamburger") menu in the top right.
To improve performance, the background heatmap will be turned off automatically if the array is very large.

.. image:: /images/variable_explorer/variable-explorer-heat-map.png
   :alt: Array editor array, displaying a "heatmap" of its values

You can manually adjust the size of the rows and columns of the array by expanding or contracting their headers.
Clicking the resize button on the right of the dialog toolbar will set the widths automatically.

.. image:: /images/variable_explorer/variable-explorer-resize.gif
   :alt: Array editor with a 2D int array, showing resizing of columns

If supported by the datatype, you can also change the format of the array's values, choosing the number of decimals that you want the array to display.
For this, enter the desired format string (using Python's standard `format specification mini-language`_) under :guilabel:`Formatting` in the :guilabel:`Display options` dialog under the pane options ("hamburger") menu in the top right.

.. _format specification mini-language: https://docs.python.org/3/library/string.html#format-specification-mini-language



.. _panes-variables-viewers-dataframe:

DataFrames
~~~~~~~~~~

DataFrames, like :ref:`panes-variables-viewers-array`, display in a viewer where you can change the format, resize the rows and columns either manually or automatically and show or hide "heatmap" colors, with an added option for making the heatmap global or per-column.

.. image:: /images/variable_explorer/variable-explorer-dataframe.png
   :alt: Dataframe editor showing data frame "heatmap"

Additionally, toolbar buttons allow inserting, duplicating or deleting both rows and columns, and plotting a histogram of the selected columns.

The Variable Explorer has MultiIndex support in its DataFrame inspector, including for multi-level and multi-dimensional indices.

.. image:: /images/variable_explorer/variable-explorer-multi-index.png
   :alt: Dataframe editor showing multi-index support



.. _panes-variables-options:

============
Options menu
============

The options ("hamburger") menu in the top right of the Variable Explorer pane allows you filter the objects shown by a number of different criteria, which can be toggled on and off with the filter button to the right of the toolbar.

.. image:: /images/variable_explorer/variable-explorer-menu.png
   :alt: Spyder Variable Explorer, with options menu

It also allows you to display the min and max of NumPy arrays instead of a preview of their values.

.. image:: /images/variable_explorer/variable-explorer-array-min-max.png
   :width: 500
   :alt: Variable Explorer showing max and min values of numpy array



.. _panes-variables-toolbar:
.. _panes-variables-import-export:

=======================
Importing and exporting
=======================

The Variable Explorer's toolbar includes several useful features to import, export and manage variables and data.
The :guilabel:`Import data` button can be used to load a variety of types of data files, including JOSN, NumPy, Matlab, CSV, images, Python pickles and HDF5.
The :guilabel:`Save data` and :guilabel:`Save data as` buttons allows saving the current session as a ``.spydata`` file, which can be loaded later with the :guilabel:`Import data` button to restore the saved variables to your active session.

.. image:: /images/variable_explorer/variable-explorer-import-data.gif
   :alt: Variable Explorer showing how to save and import data

.. warning::

   You should **not** load any ``.spydata`` file from any source you don't fully trust (ideally, only those files you've saved yourself).
   Like with any `Python pickle`_, it is inherently not secure against malicious code, as it can load any Python object and can execute arbitrary code on your machine.
   Additionally, it is not guaranteed to work reliably across all Python environments other than the one it was created in, so it should be only used as a local persistence format, not for interchange.

.. _Python pickle: https://docs.python.org/3/library/pickle.html

The trash button allows removing all displayed variables, and the search button allows finding objects by name or type.

.. image:: /images/variable_explorer/variable-explorer-search.gif
   :alt: Variable Explorer showing how to search variables

Finally, the refresh updates the Variable Explorer's contents to show the current state of the code running in the :ref:`panes-console`.



.. _panes-variables-advanced:

======================
Advanced functionality
======================

The context menu, available by right-clicking any variable, provides numerous additional options to interact with objects of various types.
These include renaming, removing or editing existing variables, as well as a :guilabel:`Duplicate` option to create a new copy of one of them under a new name.

.. image:: /images/variable_explorer/variable-explorer-duplicate.gif
   :alt: Variable Explorer showing duplicating a variable

Furthermore, you can copy and paste the value of a variable, saving it in the Variable Explorer with any name that you choose.
This allows you to change the type of the variable that you are pasting which can be very useful, allowing you to, for example, easily copy the elements of a list into an array.

.. image:: /images/variable_explorer/variable-explorer-copy-paste.gif
   :alt: Variable Explorer showing copying list into array

Additionally, you can create an object from scratch directly in the Variable Explorer with the :guilabel:`Insert` option, which allows you to type the key and the value for the item that you want to insert.
In addition to adding a new top-level variable, this feature also allows you to create a new key in a dictionary, a new element in a list, and much more.

.. image:: /images/variable_explorer/variable-explorer-insert.gif
   :alt: Variable Explorer showing insertion of a new variable

For lists and NumPy arrays, more advanced options are available, including generating plots and histograms of their values appropriate to their type and dimensions.

.. image:: /images/variable_explorer/variable-explorer-histogram-plot.gif
   :alt: Plot window showing a plot, generated via the previous options

You can save an array to a ``.npy`` file by clicking the appropriate option, which can later be loaded in the Variable Explorer via :guilabel:`Import data` or in your code via ``numpy.load()``.

.. image:: /images/variable_explorer/variable-explorer-contextmenu-array.png
   :width: 500
   :alt: Context menu for an int array, with the Show image option selected

For two-dimensional arrays, you can also display them as images, treating their values as RGB colors. For this, Spyder uses Matplotlib's colormaps, which can be `easily changed to match your preferences`_.

.. _easily changed to match your preferences: https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

.. image:: /images/variable_explorer/variable-explorer-show-image.gif
   :alt: Interactive image based on the array's data

Finally, there is a context-menu action to open any object using the new Object Explorer even if they already have a builtin viewer (DataFrames, arrays, etc), allowing for deeper inspection of the inner workings of these data types.

.. image:: /images/variable_explorer/variable-explorer-object-explorer.png
   :alt: Object explorer showing DataFrame



.. _panes-variables-related:

=============
Related panes
=============

* :ref:`panes-debugger`
* :ref:`panes-console`
