####################
Static Code Analysis
####################

The **Static Code Analysis** module detects style issues, bad practices, potential bugs, and other quality problems in your code, all without having to actually execute it.
Spyder's static analyzer is powered by the best in class `Pylint`_ backend, which can intelligently detect an enormous and customizable range of problem signatures.

.. _Pylint: https://www.pylint.org/

.. image:: images/pylint/static_analysis_standard.png
   :alt: Spyder Pylint pane, showing numerous issues discovered in a file

|


=========================
Using the static analyzer
=========================

You can run Spyder's :guilabel:`Static Code Analysis` directly from the :doc:`editor`, or you can manually enter the Python module or package path you'd like it to check.
The analyzer works with both ``.py`` (or ``.pyw``) Python scripts and whole Python packages (directories containing an :file:`__init__.py` file).
To go directly to the file and line in the :doc:`editor` highlighted by a failed check, just click its name.
Start and cancel analyzing a file with the :guilabel:`Analyze` and :guilabel:`Stop` buttons respectively, and if analysis fails, click the :guilabel:`Output` button to find out why.
You click the dropdown or press the down arrow in the filename field to view results of previous analyses; the number of recent runs Spyder should remember can be customized in the :guilabel:`History` dialog from the :guilabel:`Static Code Analysis` context menu.
All standard checks are run by default.
You can turn certain messages off at the line, block or file/module level by adding a ``# pylinet: disable=insert, message-names, here`` comment at the respective level, or by editing the :file:`.pylintrc` configuration file in your user home directory (for more details on configuring Pylint, see the `Pylint documentation`_).

.. _Pylint documentation: https://pylint.readthedocs.io/en/latest/faq.html#message-control


Related components
~~~~~~~~~~~~~~~~~~

* :doc:`editor`
