.. _panes-find:

####
Find
####

The **Find** pane allows you to search the content of text files in a user-defined location, with advanced features to filter your results.

.. image:: /images/find_in_files/find-in-files-inprogress.webp
   :alt: Spyder Find in Files panel, with search results shown per-file



.. _panes-find-using:

===================
Using the Find pane
===================

To search for text in the Find pane, enter it in the field in the top left and press the search button.
This will allow you to view and navigate through all the occurrences of your search text in your working directory.
You can expand or collapse the search results to view the matches in each file.
Clicking on a match will automatically open the file and highlight the line where the text was found.

.. video:: /images/find_in_files/find-in-files-search.webm
   :loop:
   :alt: Spyder Find pane showing search and going to a file

If you want to change the scope of your search, select another directory, project or file in the :guilabel:`Search in` dropdown.
The locations that you select for your search will be stored in the list so you can access them easily in the future.
To erase all of these saved directories, select the :guilabel:`Clear the list of other directories` option from the :guilabel:`Search in` dropdown.

.. video:: /images/find_in_files/find-in-files-directory.webm
   :loop:
   :alt: Spyder Find pane showing choosing new directory and directory stored in the list



.. _panes-find-options:

=======================
Choosing search options
=======================

You can select from a number of options to enable searches as broad or refined as you need.

To enable case sensitivity, which only returns matches with identical capitalization to your search text, toggle the :guilabel:`Aa` button on.

.. video:: /images/find_in_files/find-in-files-case.webm
   :loop:
   :alt: Spyder Find pane showing search with case sensitive activated

To parse your search string as a `regular expression <regular expression_>`__, enable the :guilabel:`.*` button.

.. _regular expression: https://docs.python.org/3/library/re.html

.. video:: /images/find_in_files/find-in-files-regex.webm
   :loop:
   :alt: Spyder Find pane showing regular expression search

To exclude certain filenames, extensions or directories from your search, click the :guilabel:`+` button to display the advanced options for the pane, and then enter them in the :guilabel:`Exclude` text box.

.. video:: /images/find_in_files/find-in-files-extensions.webm
   :loop:
   :alt: Spyder Find pane showing search excluding several file-types

Finally, to change the number of matches displayed, select the :guilabel:`Set maximum number of results` option under the pane's options ("hamburger") menu in the top right.

.. image:: /images/find_in_files/find-in-files-max-results.webp
   :alt: Spyder Find pane showing window with maximum results dialog open



.. _panes-find-related:

=============
Related panes
=============

* :ref:`panes-files`
* :ref:`panes-projects`
