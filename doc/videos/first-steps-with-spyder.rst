#######################
First Steps with Spyder
#######################

The videos in this section provide a starting point for new users who have never opened Spyder before.
You'll get familiar with opening Spyder in different ways, working with the four main panes and customizing the Spyder to your heart's content.



===============
Getting started
===============

Discover the basics of using the Spyder interface and get an introduction to its four main panes, along with a quick look at the others.

* Find out different ways to open Spyder
* Understand the key elements of Spyder’s interface
* Learn more about Spyder’s four core panes
* Explore the other default panes

.. youtube:: E2Dap5SfXkI
   :height: 360
   :width: 640
   :align: left

.. rst-class:: dropdown-videos

.. dropdown:: Transcript
   :animate: fade-in

   .. div:: scroll

      Hello everyone! I'm Juanita, and in this video I'm going to show you how to open Spyder and go over the basics of Spyder's interface. We will learn about Spyder's four panes that you'll likely be using most often, as well as briefly explore the others that are open by default. If you don't have Spyder installed and would like to follow along, you can `download it here`_.

      .. _download it here: https://www.spyder-ide.org/#section-download

      The easiest way to open Spyder is by opening Anaconda Navigator and clicking on the Spyder application. In case you have an older version of Spyder in Anaconda, open the command line (or the Anaconda Prompt in the case of Windows) and type the commands:

      .. code-block:: bash

         conda update anaconda
         conda install spyder=4

      To launch Spyder without opening Navigator, open your command line and type ``spyder``. If you followed the :doc:`/installation`, you should have everything necessary to open Spyder 4.

      This is what Spyder 4 looks like in its default configuration, though you can thoroughly customize it, which we'll get to in a later tutorial. You can see that it is divided into three sections showing three different panes: the Editor, the IPython Console and the Help viewer. These three, along with the Variable Explorer, are the four core panes you'll work with the most in Spyder.

      On the left we have the Editor, where you can open, edit and run files. Bottom right is the IPython Console, which you can use both interactively and to run your code in the Editor. It shows you which version of Python you are using. Above it, you'll find the Help pane, where you can get more information and documentation for any object in the Editor or Console by pressing :kbd:`Ctrl-I` (or :kbd:`Cmd-I` on macOS). We'll see how to do this in our next video.

      For the two sections on the right, you can switch tabs to see the other panes that are open by default when launching Spyder. In the top section, you can switch to the Variable Explorer, which shows you the name, type, size and value of the variables that you have previously defined in the Editor or the Console. You can also modify the value of these variables directly from this pane by double clicking them under the Value column. The Plots pane will show you the figures you generate with Matplotlib and other libraries, and the Files pane allows you to browse the files on your computer and open them in the Editor with just a click.

      Finally, in the bottom section you can also access the History pane, which shows you the commands you have entered in the Console, including those from previous sessions.

      I hope you're now familiar with the basics of using the Spyder interface. In the next video, we will start working with Spyder's core panes.

      Happy Spydering!



===================
Learning the basics
===================

Learn the basics of using Spyder’s four main panes.

* Open and edit a file in Spyder’s Editor
* Run a script in the Editor and see the output in Spyder’s IPython Console
* Execute basic Python commands in the IPython Console
* Define variables in the Editor and modify their values in the IPython Console
* View and interact with the variables in Spyder’s Variable Explorer
* Get documentation in the Help pane in two different ways

.. youtube:: WV9bm4ey7Cg
   :height: 360
   :width: 640
   :align: left
.. rst-class:: dropdown-videos

.. dropdown:: Transcript
   :animate: fade-in

   .. div:: scroll

      Hello everyone! I'm Juanita, and in this video I will show you how to start working with Spyder's four main panes. First, let's take a look at the Editor, which you can use to open, edit and run files from your computer. I will open a short "Hello World" program for this demo, which you can `download here`_. Once you have it open in your Editor, you can execute it by pressing the green run button. We can see the output in the Python Console [Show IPython console] as well as the path of the file that we are running and the working directory where this code was run.

      .. _download here: https://drive.google.com/file/d/18Ai-XY9kIPm9x_7-0RBakV2a6dRVqh-L/view

      We can also run any Python code that is entered directly in the IPython Console. For example, we can type ``print("Hello")`` and see the output. Or, we can try some math operations and see the results here too. Note that for implicitly printed output, there is a red indication that differs from the output of the ``print()`` function.

      Now, let's start defining some variables. We can do this both from the editor or from the Console. If I define a variable ``a = 10`` and then run this code, I can see its value in the console just by typing its name ``a``. However, you can also assign any variable in the IPython console (``b = 20``) and its value will be stored too. In both cases, they can also be seen in the Variable Explorer pane, which shows the name, type, size and value of each of the objects previously defined. In this case, we see variables ``a`` and ``b``, both of type int and with size 1. We can also define a list ``l`` with ``l = [1, 2, 3]`` and see that the type of the variable is list and the size is 3.

      We can change the values of the variables in the Variable Explorer too by double-clicking them and typing their new value. Now, we can check their new value in the console. In the case of a more complex type like a list, double-clicking it will open a viewer in which you can modify each of its values separately, along with other more complex operations which we'll demonstrate in a future video. We can remove a variable by right-clicking it and selecting the option Remove. After doing this, we can check in the IPython Console that the variable was actually deleted.

      Finally, we are going to learn how to get help for objects in two different ways. First, we can press :kbd:`Ctrl-I` (or :kbd:`Cmd-I` on macOS) right after the name of an object written in the Editor or the Console, for example ``numpy.array``. You can see that we obtain its documentation in the Help pane if it is available. Second, if we change the Source dropdown option to Console, we can type its name in the object box in the Help pane. Now we can get help for Numpy arrays.

      You should now be ready to start using Spyder's four main panes. Check out our next video to continue learning and as always, Happy Spydering!



=============
Customization
=============

Learn how to customize Spyder’s interface to match your workflow and development style.

* Choose your preferred fonts
* Switch between different interface, icon and syntax themes
* Show, hide, undock and rearrange Spyder panes
* Split, close and pop out Editor panels

.. youtube:: -dARZBUDk_s
   :height: 360
   :width: 640
   :align: left

.. rst-class:: dropdown-videos

.. dropdown:: Transcript
   :animate: fade-in

   .. div:: scroll

      Hello everyone, I'm Juanita! In this video, I will show you how to customize Spyder to match your workflow and development style.

      First, we are going to learn how to change the font in the Editor, IPython Console and Help panes. To do this, go to Preferences, select the Appearance entry and scroll down to Fonts. You can change both the style and the size of the font for both plain and rich text. You can see how this affects the font in the Editor, Console and Help panes.

      In this same dialog, you can easily change the syntax highlighting theme, for which you can see the preview at the right of the window. Note that Spyder's interface theme changes to match the highlighting theme because the Interface theme option is set to Automatic by default. However, you can change the theme for the entire Spyder interface, choosing between Light and Dark. After selecting this change, click Apply to restart Spyder to apply the new theme.

      Beyond just Spyder's preferences, you can freely rearrange the panes in Spyder's main window. To show or hide panes, go to Panes under the View menu, and select which ones you want to see. For example, let's hide the Files pane and show the Profiler pane. You can also close a pane from its options menu, which will hide it from the main window.

      By default, the panes and toolbars are locked so they can't be moved accidentally. However, unchecking the option Lock panes and toolbars in the View menu will allow you to move them freely anywhere on the window, by dragging them from the top and dropping them at any position you like. You can also undock a pane, which will open a new window with it. You can have as many separate windows as you have panes, if you choose. This feature is very useful if you work with several monitors because you can undock the Editor and move it to a different monitor, while working with the rest of the panes in your main monitor.

      Additionally, you can split the Editor pane vertically or horizontally in as many copies as you want, and open one or more panels in separate Spyder windows, complete with their own toolbar, outline and status bar.

      Finally, each pane can be customized further under its respective options menu and Preferences panel.

      With all these options, you can customize Spyder to your heart's content. However, if you ever want to return to its default configuration, you can always reset the window layout under Window Layouts in the View menu, or your entire Spyder configuration with the Reset to Default button in the Preferences.

      Enjoy your customized version of Spyder, and Happy Spydering!
