#################
Variable Explorer
#################

The **Variable Explorer** shows the namespace contents (all global object references, such as variables, functions, modules, etc.) of the currently selected :doc:`ipythonconsole` session, and allows you to interact with them through a variety of GUI-based editors.

.. image:: images/variable_explorer/variable_explorer_standard.png
   :align: center
   :alt: Spyder Variable Explorer, with a list of variables and their contents

|


====================
Features and editors
====================

Spyder's :guilabel:`Variable Explorer` offers built in support for editing lists, strings, dictionaries, NumPy arrays, Pandas DataFrames, and more, and can also histogram, plot, or even display some of them as an RGB image.
Several examples of this functionality follow:

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

|varexpcontextmenu| |histogram|

.. |varexpcontextmenu|
   image:: images/variable_explorer/variable_explorer_inset_contextmenu_array.png
   :width: 45%
   :alt: Variable Explorer with a context menu, including plot/histogram options

.. |histogram|
   image:: images/variable_explorer/variable_explorer_histogram.png
   :width: 50%
   :alt: Plot window showing a histogram, generated via the previous options

|

.. image:: images/variable_explorer/variable_explorer_contextmenu_array.png
   :align: center
   :alt: Context menu for an int array, with the Show image option selected

.. image:: images/plot_window/plot_window_show_image.png
   :align: center
   :alt: Plot window showing an interactive image based on the array's data

|


===============
Supported types
===============

The Variable Explorer has specialized editors for a range of common built-in and third-party Python objects, and can view, edit, and deeply introspect most arbitrary objects via a more general :guilabel:`Object explorer`.
Types with specialized editing support include:

* Integers
* Floats
* Complex numbers
* Strings
* ``datetime`` dates and ``Timedelta`` s
* Lists
* Tuples
* Dictionaries
* NumPy arrays and matrices
* Pandas ``DataFrame``, ``TimeSeries`` and ``DatetimeIndex`` objects
* ``PIL``/``Pillow`` images
* Namespaces


Related components
~~~~~~~~~~~~~~~~~~

* :doc:`debugging`
* :doc:`ipythonconsole`
