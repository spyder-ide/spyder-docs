#############
Code Analysis
#############

The **Code Analysis** pane detects style issues, bad practices, potential bugs, and other quality problems in your code, all without having to actually execute it.
Based on these results, it also gives your code an overall quality score.
Spyder's code analyzer is powered by the best-in-class `Pylint`_ back-end, which can intelligently detect an enormous and customizable range of potential errors, bad practices, quality issues, style violations, and more.

.. _Pylint: https://pylint.pycqa.org/

.. image:: /images/pylint/code-analysis-standard.png
   :alt: Spyder Pylint pane, showing numerous issues discovered in a file



=======================
Using the code analyzer
=======================

You can select the desired file to analyze directly in the :doc:`editor` by clicking anywhere within it.
To run the analysis, press the configurable shortcut (:kbd:`F8` by default), select :menuselection:`Source --> Run code analysis` from the menu bar or click the :guilabel:`Analyze` button in the Code Analysis pane.
If the Code Analysis pane is not visible, you can open it under :menuselection:`View --> Panes --> Code Analysis`.
All standard checks are run by default.
To go directly to a line in the :doc:`editor` highlighted by a failed check, just click its name.

.. image:: /images/pylint/code-analysis-editor.gif
   :alt: Spyder Pylint pane, showing running analysis and clicking failed check

You can also manually enter the path of a file you'd like it to check in the path entry box in the pane's toolbar.
The analyzer works with both individual scripts and whole Python packages (directories containing an :file:`__init__.py` file).

.. image:: /images/pylint/code-analysis-file.gif
   :alt: Spyder Pylint pane, showing running analysis browsing file

Cancel analyzing a file with the :guilabel:`Stop` button, and if analysis fails, click the :guilabel:`Output` button to find out why.
If Pylint does succeed, the :guilabel:`Output` will show the raw plain text analysis results on the selected file, allowing you to easily browse and copy/paste the full message names and descriptions.

.. image:: /images/pylint/code-analysis-output.png
   :alt: Spyder Pylint pane, showing output

Finally, you can click the dropdown or press the dropdown arrow in the filename field to view results of previous analyses.

.. image:: /images/pylint/code-analysis-history.png
   :alt: Spyder Pylint pane, showing history



============
Options menu
============

The number of recent runs Spyder should remember can be customized in the :guilabel:`History` dialog, available from the Code Analysis options menu.

.. image:: /images/pylint/code-analysis-history-custom.gif
   :alt: Spyder Pylint pane, customizing history dialog

You can also expand or collapse one or all the sections in the pane by using the corresponding options in the options menu.

.. image:: /images/pylint/code-analysis-expand-collapse.gif
   :alt: Spyder Pylint pane, expanding and collapsing sections



================
Advanced options
================

You can turn certain messages off at the line, block or file/module level by adding a ``# pylint: disable=MESSAGE-NAMES`` comment at the respective `scope`_, where ``MESSAGE_NAMES`` should be replaced with a comma-separated list (or single value) of `Pylint message names`_.
For example, a directive might look like ``# pylint: disable=invalid-name``, or ``# pylint: disable=fixme, line-too-long``.

.. _scope: https://pylint.pycqa.org/en/stable/user_guide/message-control.html

.. _Pylint message names: https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html#pylint-checkers-options-and-switches

.. image:: /images/pylint/code-analysis-pylint-disable.gif
   :alt: Spyder Pylint pane, showing disabling a message locally

Or, you can globally suppress specific messages and adjust other Pylint settings by editing the :file:`.pylintrc` configuration file in your user folder.
If it doesn't exist, you can generate it by running ``pylint --generate-rcfile > .pylintrc`` in your user directory, from Anaconda Prompt (on Windows) or your terminal (macOS/Linux).
For more details on configuring Pylint, see the `Pylint documentation`_.

.. _Pylint documentation:  https://pylint.pycqa.org/en/stable/index.html

.. image:: /images/pylint/code-analysis-pylint-file.gif
   :alt: Spyder Pylint pane, disabling a message globally in the .pylintrc



=============
Related panes
=============

* :doc:`editor`
* :doc:`profiler`
