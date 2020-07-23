:orphan:

####
Find
####

The **Find** pane allows you to search the content of files in a user-defined location, with advanced features to filter your results.

.. image:: images/find_in_files/find_in_files_inprogress.png
   :alt: Spyder Find in Files panel, with search results shown per-file

|

===================
Using the Find pane
===================

To search for text in the Find pane, write it in the top bar of the pane and press the search button.
This will allow you to view and navigate through all the occurances of your search text in your working directory. You can expand or contract the search results to view the results on each file. Clicking on any of these matches, will automatically open the file showing where the text was found.

[GIF showing search and cliking file]

If you want to change the scope of your search, select another directory, project or file in the :guilabel: 'Search in' menu. The locations that you select for your search will be stored in the list so you can access them easily. To erase all of these locations, select the "clear the list" option from the dropdown menu in the "Search in" field.

[GIF showing chosing new directory and directory stored in the list]

=======================
Choosing search options
=======================

You can select from a number of options to enable searches as broad or refined as you need:

To enable case sensitivity, controlling whether matches are returned with a different case than your search text, toggle the :guilabel:`Aa` button on.

[GIF showing search with case sensitive activated]

To parse your search string as a regular expression, toggle the :guilabel:`Gear` button on.

[GIF showing regular expression search]

To exclude certain filenames, types, or directories from your search, use the :guilabel:`Exclude:` text box, by displaying the advanced options clicking the :guilabel:`Plus:` icon. 

[GIF showing search excluding several file-types]

Finally, to change the number of results displayed, select the 'Set maximum number of results' option under the Options menu on the pane.

[Screenshot showing window with maximum results dialog open]


Related components
~~~~~~~~~~~~~~~~~~

* :doc:`editor`
* :doc:`fileexplorer`
