Variable Explorer
=================

The variable explorer shows the namespace contents (i.e. all global object
references) of the current console

.. image:: images/variable_explorer/variable_explorer_standard.png
   :align: center
   :alt: Spyder Variable Explorer, with a list of variables and their contents

|

The following screenshots show some interesting features such as editing
lists, strings, dictionaries, NumPy arrays, or plotting/showing NumPy arrays
data.

|

.. image:: images/variable_explorer/variable_explorer_text_long.png
   :align: center
   :alt: Variable Explorer text editor, displaying a long string in a window

|

.. image:: images/dialog/dialog_user_env_variables_edit.png
   :align: center
   :alt: Dictionary editor displaying keys and their types, sizes, and values

|

.. image:: images/variable_explorer/variable_explorer_list_timedelta_edit.png
   :align: center
   :alt: List editor displaying a list of timedeltas, showing one being edited

|

.. image:: images/variable_explorer/variable_explorer_array_2D_resize.png
   :align: center
   :alt: Array editor with a 2D int array, displaying a "heatmap" of its values

|

|contextmenu| |histogram|

.. |contextmenu| image:: images/variable_explorer/variable_explorer_inset_contextmenu_array.png
   :width: 45%
   :alt: Variable Explorer with a contextmenu, including plot/histogram options

.. |histogram| image:: images/variable_explorer/variable_explorer_histogram.png
   :width: 50%
   :alt: Plot window showing a histogram, generated via the previous options

|

.. image:: images/variable_explorer/variable_explorer_contextmenu_array.png
   :align: center
   :alt: Contextmenu for an int array, with the Show image option selected

.. image:: images/plot_window/plot_window_show_image.png
   :align: center
   :alt: Plot window showing an interactive image based on the array's data

|


Supported types
---------------

The variable explorer can't show all types of objects. The ones currently
supported are:

#. `Pandas` DataFrame, TimeSeries and Index objects
#. `NumPy` arrays and matrices
#. `PIL/Pillow` images
#. `datetime` dates
#. Integers
#. Floats
#. Complex numbers
#. Lists
#. Sets
#. Dictionaries
#. Tuples
#. Strings

Related plugins:

* :doc:`ipythonconsole`
