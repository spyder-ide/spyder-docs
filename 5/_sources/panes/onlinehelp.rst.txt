###########
Online Help
###########

The **Online Help** pane provides a built-in web browser to explore dynamically generated Python documentation on installed modules—including your own—rendered by a `pydoc`_ server running in the background.

.. _pydoc: https://docs.python.org/3/library/pydoc.html

.. image:: /images/online_help/online-help-standard.png
   :alt: Spyder Online Help pane on the index page, a list of builtin modules



=====================
Using the Online Help
=====================

The Online Help's home shows an index where you can browse the documentation of standard library modules, third party packages installed in your Python environment, and your own local code.
Click on the name of any module to open its documentation.

.. image:: /images/online_help/online-help-browse.gif
   :alt: Spyder Online Help pane showing module browsing

Enter the name of the item you'd like help on in the :guilabel:`Package` field to load its documentation directly.

.. image:: /images/online_help/online-help-name.gif
   :alt: Spyder Online Help pane showing module browsing by name

The module's file location is linked to the right of the doc's title, which you can click to view its source code.

.. image:: /images/online_help/online-help-path.gif
   :alt: Spyder Online Help pane showing source code clicking module's path

Standard library modules also have a link to the corresponding `Python docs`_, which can be viewed right inside of the pane.

.. _Python docs: https://docs.python.org/

.. image:: /images/online_help/online-help-python-docs.gif
   :alt: Spyder Online Help pane showing python docs embedded in pane

If you're not sure of the name of the object you want help on, or are looking for a specific keyword, use the :guilabel:`Search` field to get a list of results.

.. image:: /images/online_help/online-help-search.gif
   :alt: Spyder Online Help pane showing search of a keyword

Links above the search field provide an index of topics with general help and a list of Python keywords linked to their corresponding docs.

.. image:: /images/online_help/online-help-topics.png
   :alt: Spyder Online Help pane on the topics page



=============
Toolbar items
=============

Just like in a web browser, the forward and back buttons move through the pages you have visited, and the home button (house icon) returns you to the module index.

.. image:: /images/online_help/online-help-navigation.gif
   :alt: Spyder Online Help pane showing navigation with arrows

Perform a realtime search within a page's content with the :guilabel:`Find` button (magnifying glass icon top left) or :kbd:`Ctrl-F`, navigate through matches with the Up and Down buttons, and make matching case sensitive with the :guilabel:`Aa` button.

.. image:: /images/online_help/online-help-find.gif
   :alt: Spyder Online Help pane showing finding a word on a module

You can view and re-run previous searches from the drop-down menu in the :guilabel:`Package` field.

.. image:: /images/online_help/online-help-history.png
   :alt: Spyder Online Help pane showing previous searches

You can also use the zoom in/out buttons (:guilabel:`-` and :guilabel:`+`, top right) to change the font size to suit your preferences.

.. image:: /images/online_help/online-help-zoom.gif
   :alt: Spyder Online Help pane showing changing the font

To cancel searching or page loading, click the stop button (red square), and to reload the page (such as when you change your own package's documentation), press the refresh button (circular arrow).

.. image:: /images/online_help/online-help-refresh.gif
   :alt: Spyder Online Help pane showing refreshing pane when updating docs



==================
Related components
==================

* :doc:`help`
