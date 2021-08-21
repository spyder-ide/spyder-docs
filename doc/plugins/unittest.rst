###############
Spyder Unittest
###############

**Spyder-unittest** is a plugin that integrates popular unit test frameworks with Spyder: such as Pytest, Unittest, and Nose. Which allow you to run test suites and view the results in the IDE.

.. image:: /images/unittest/unittest-run.png
   :alt: Spyder Unittest in Spyder

| `Pytest <https://docs.pytest.org/en/6.2.x/>`_

| `Unittest <https://docs.python.org/3/library/unittest.html#module-unittest>`_

| `Nose <https://nose.readthedocs.io/en/latest/>`_

===================
Installing Unittest
===================

.. code-block:: bash

   conda install -c spyder-ide spyder-unittest

.. important::

   Please make sure you have Python's Pytest package installed if you are going to use that program as well.

.. code-block:: bash

   conda install pytest

Restart Spyder in order to be able to use the plugin.

==============
Using Unittest
==============

When Unittest is installed, it will be available under the menu item :menuselection:`View --> Panes --> Unit testing`.

.. image:: /images/unittest/unittest-view-panes.png
   :alt: Spyder showing view panes Unittest

You will see it then as a tab in the bottom of the top right area in the same location as the Variable explorer, Help, and Plots views.

Press on the  :guilabel:`Run Green Arrow` to run the testing.

Pytest will run all files of the form :guilabel:`test_*.py` or :guilabel:`*_test.py` in the current directory and its subdirectories.

| `Pytest Run Guide <https://docs.pytest.org/en/6.2.x/getting-started.html#run-multiple-tests>`_

.. image:: /images/unittest/unittest-run-button.png
   :alt: Spyder showing Unittest run button

You can get an expanded view of the testing messages by clicking on the expand option.

.. image:: /images/unittest/unittest-expanded-message-view.png
   :alt: Spyder showing Unittest expanded message view

Press on the  :guilabel:`Hamburger Menu Icon` to view different unittest options.

.. image:: /images/unittest/unittest-hamburger-menu.png
   :alt: Spyder Unittest hamburger menu in Spyder

The configuration view will show you how to choose the pytest option and the directory of where you want to run the test file(s) from.

.. image:: /images/unittest/unittest-configuration-view.png
   :alt: Spyder Unittest configuration view in Spyder

The dependencies view will show you all of your installed package versions.

.. image:: /images/unittest/unittest-dependencies-view.png
   :alt: Spyder Unittest dependencies view in Spyder

Finally, the output viewer can be used to directly view the output results of your testing.  This view can be very useful for viewing the results of unittests.

.. image:: /images/unittest/unittest-output-viewer.png
   :alt: Spyder Unittest output viewer in Spyder
