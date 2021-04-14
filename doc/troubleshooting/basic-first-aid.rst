###############
Basic First Aid
###############

These suggestions, while more of a shotgun approach, tend to fix the majority of reported issues just on their own.



=================================
Recommended troubleshooting steps
=================================

#. **Restart Spyder**, and try what you were doing before again.

#. **Upgrade Spyder** to the latest release, and you might find your issue is resolved (along with new features, enhancements, and other bug fixes).
   Minor releases come out every couple months, so unless you've updated recently, there is a good chance your version isn't the latest.
   You can find out with the :guilabel:`Check for updates` command under the :guilabel:`Help` menu.

   .. image:: /images/basic-first-aid/basic-first-aid-updates.png
      :alt: Spyder showing view internal console option

   To perform the update with Conda (strongly recommended), from your terminal (or Anaconda Prompt on Windows) run:

   .. code-block:: bash

      conda update anaconda
      conda update spyder

#. **Update Spyder's dependencies and environment**, either by installing the latest version of your distribution (e.g. the recommended Anaconda), or with the relevant "update all" command in your terminal (or Anaconda Prompt on Windows).
   To get the latest stable version of everything using Conda, you can run:

   .. code-block:: bash

      conda update qt pyqt spyder-kernels ipython ipykernel jupyter_client jupyter_core pyzmq

#. **Restart your machine**, in case the problem lies with a lingering process or another such issue.

#. **Restore Spyder's config files** to their defaults, which solves a huge variety of Spyder issues.
   From your terminal (or Anaconda Prompt on Windows), run:

   .. code-block:: bash

      spyder --reset

   .. note::

      This will reset your preferences, as well as any custom keyboard shortcuts or syntax highlighting schemes.
      If you particularly care about any of those, you should make a copy of the :file:`.spyder-py3` folder in your user home directory (:file:`C:/Users/YOUR_USERNAME` on Windows, :file:`/Users/YOUR_USERNAME` on macOS, or :file:`/home/YOUR_USERNAME` on Linux), and restore it afterwards if this doesn't solve the problem.

#. **Try installing Spyder into a new Conda environment** (recommended) or ``virtualenv``/``venv``, and see if the issue reoccurs.

In your system terminal (or Anaconda Prompt on Windows), run the following commands to create an a fresh, clean environment and start Spyder in it:

.. code-block:: bash

   conda create -n spyder-env spyder -y
   conda activate spyder-env
   spyder

If this fixes the issue, the problem was likely due to another package installed on your system, particularly if done with pip, which can cause many problems and should be avoided if at all possible.

#. **Watch our video** on solving and avoiding problems with pip, Conda and Conda-Forge, and follow its instructions.

   .. youtube:: Ul79ihg41Rs
      :height: 360
      :width: 640
      :align: left



.. _troubleshooting-reinstalling-spyder-ref:

===================
Reinstalling Spyder
===================

If none of the previous steps solve your issue, you should do a full uninstall of Spyder by whatever means you originally installed it.

For Anaconda, follow all the steps under Option B in the `Anaconda uninstall guide`_, delete the Anaconda directory wherever it was originally installed, and (on Windows) remove the :file:`%appdata%/python` directory if it exists.

.. image:: /images/basic-first-aid/basic-first-aid-app-data.gif
   :alt: Deleting appdata/python directory

Then, do a clean install of the latest version of the `Anaconda distribution`_ which is how we recommend you install Spyder and keep it up to date.

.. important::

   While you are welcome to get Spyder working on your own by one of the many other means we offer, we are only able to provide individual support for install-related issues for users of the Anaconda distribution.
   In particular, pip installation, while doable, is only really for experts, as there are many pitfalls involved and different issues specific to your setup, which is why we recommend using Conda whenever possible.
   For further information, please visit our :doc:`/installation`.

.. _Anaconda uninstall guide: https://docs.anaconda.com/anaconda/install/uninstall/
.. _Anaconda distribution: https://www.anaconda.com/products/individual



==================
Isolating problems
==================

If you get an error while running a specific line, block, or script/program, it may not be an issue with Spyder, but rather something lower down in the packages it depends on.
Try running it in the following in order if and until it starts working as you expect.
If you manage to isolate the bug, report it to the last one it *doesn't* work in.

#. **Spyder** itself, of course!
   Make sure you can reproduce the error after closing and reopening it, if possible.

#. **A bare QtConsole instance**, e.g. launched from Anaconda navigator or from the Anaconda Prompt/Terminal/command line (Windows/Mac/Linux) with ``jupyter qtconsole``.

   .. image:: /images/basic-first-aid/basic-first-aid-qtconsole.png
      :alt: Anaconda navigator showing qtconsole

   QtConsole is the GUI console backend Spyder depends on to run its code, so most issues involving Spyder's :doc`ipythonconsole` are actually something with QtConsole instead, and can be reported to their `issue tracker`_.

#. **An IPython command line shell**, launched with e.g. ``ipython`` from the Anaconda Prompt/Terminal/command line (Windows/Mac/Linux).
   Reproducible bugs can be reported to their `Github page`_, though make sure to read their guidelines and docs first.

#. **A standard Python interpreter**, either run as a script file with ``python path/to/your/file.py`` or launched interactively with ``python`` from your Anaconda Prompt/Terminal/command line (Windows/Mac/Linux).
   While it is not impossible that you've found Python bug, it is much more likely to be an issue with the code itself or a package you are using, so your best sources are the `Python docs`_ and the other resources listed above.

.. _issue tracker: https://github.com/jupyter/qtconsole/issues/
.. _Github page: https://github.com/ipython/ipython/issues
.. _Python docs: https://www.python.org/doc/

.. tip::

   If the problem reoccurs in a similar or identical way with any of these methods (other than only Spyder itself), then it is almost certainly not an issue with Spyder, and would be best handled elsewhere.
   As we usually aren't able to do much about issues not related to Spyder, a forum like `Stack Overflow`_ or the relevant package's docs is a much better place to get help or report the issue.

.. _Stack Overflow: https://stackoverflow.com/

See the :doc:`call-for-help` section for other places to look for information and assistance.



======================
Debugging and patching
======================

If you know your way around Python, you can often diagnose and even fix Spyder issues yourself, since the IDE is written in the same language you use in it.
You can explore the error messages you're receiving and Spyder's inner workings with the :guilabel:`Internal Console`, available under the menu item :menuselection:`View --> Panes --> Internal Console`.

.. image:: /images/basic-first-aid/basic-first-aid-internal-console.png
   :alt: Spyder showing Internal console

For more detailed debug output, start Spyder from the command line (Anaconda Prompt on Windows) with ``spyder --debug-info verbose``.

Even if you don't manage to fix the problem yourself, this output can be very helpful in aiding us to quickly narrow down and solve your issue for you.
