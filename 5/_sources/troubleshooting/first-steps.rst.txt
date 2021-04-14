###########
First Steps
###########

If Spyder crashes or you receive an error message, please read the following troubleshooting steps before opening a new issue.
There's a good chance that someone else has already experienced the same problem, so checking for an existing solution will likely get Spyder working again for you as quickly as possible.

.. important::
   To make sure you're getting the most relevant help for your problem, please make sure the issue is actually related to Spyder:

   * If the problem appears to be a result of *your own code*, `Stack Overflow`_ is a better place to start.
   * If the bug also occurs in the *standard Python, IPython, or QtConsole* environments, or only with *a specific package*, it is unlikely to be something in Spyder, and you should report it to those sources instead.
   * If the problem lies with *your specific install*, uninstalling and clean-reinstalling the `Anaconda`_ distribution is strongly recommended.
     As the other methods of installing Spyder can result in tricky user-specific problems, we generally aren't able to give individual support for install issues.

.. _Stack Overflow: https://stackoverflow.com
.. _Anaconda: https://www.anaconda.com/products/individual

Just like the programs you code in it, Spyder is written in Python, so you can often figure out many problems just by reading the last line of the traceback or error message.
To view it, simply click :guilabel:`Show details` in the Spyder error dialog.

.. image:: /images/first-steps/first-steps-show-details.png
   :alt: Spyder showing view internal console option

Often, that alone will tell you how to fix the problem on your own, but if not, we're here to help.



=====================
Where to go from here
=====================

If you check out our list of issue categories and problem descriptions and see a question, error message or traceback that looks familiar, the relevant sub-section will likely be of the most specific help solving your issue as quickly as possible.

.. rst-class:: fasb fa-first-aid

As a first step to solving your issue, you can try some :doc:`basic-first-aid`.

.. rst-class:: fasb fa-heartbeat

If Spyder won't launch, check the :doc:`emergency-cpr` section and see if that clears it up.

.. rst-class:: fasb fa-user-md

If your problem is related to the kernel not starting, autocompletion or a plugin go to :doc:`common-illnesses` section.

.. rst-class:: fasb fa-phone

If you still can't get it to work, and the problem is indeed Spyder-related, you should consult the the :doc:`call-for-help` section for other resources to explore.

.. rst-class:: fasb fa-bug

Finally, if you couldn't solve your problem and want to submit an issue to our Github issue tracker, so the bug can hopefully be fixed for everyone, :doc:`submit-a-report`.
