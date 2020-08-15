###############
Spyder Notebook
###############

Spyder-notebook is a plugin that allows you to open, edit and interact with Jupyter Notebooks right inside Spyder. Using notebooks inside of Spyder allows you to take advantage of its web interface alongside Spyder’s powerful features such as the Variable explorer, the console and the debugger. When installed, it is available as a tab in the bottom of the editor area.



Due to the nature in which Spyder developed the editor was originally the only way to edit documents. Jupyter notebooks were developed later with the success of iPython console. 

Currently the main icons / menus are associated with the editor “tab” and the notebook “tab” has its own methods for opening a notebook. The interfaces are planned to be merged as part of Spyder 5.


Using Spyder Notebook

When the user switches to the notebook tab they are presented with a welcome screen, as shown below.



The screenshot above shows the main elements of the plugin:
Welcome tab:
This shows the help screen that helps in discovery of the features of the Spyder Notebook for new and old users alike.
New Notebook:
A new Jupyter Notebook is opened ready for user input in temporary space. This can serve as a scratch pad where the user can do quick calculations and plots, or save the notebook if they want to preserve its contents for later.  
Create additional notebooks:
The “plus” button can be used to create additional notebooks, which reside in the temp space until they are saved by the user. If the notebooks are not saved they are cleared upon restart. Once the user saves the notebook the kernel is restarted and the notebook is re-rendered.
Options Menu:
The Options Menu is used to bring up the menu that is needed for opening existing notebooks or saving open notebooks as this functionality is not available from the main menu or toolbars. 
Context Menu:
Right clicking anywhere in the notebook interface will bring up the context menu similar to the menu button. Its features are described further in the Context menu  [link] section.
Notebook / Editor tabs:
These tabs in the bottom are used to switch between the Editor and Notebook interfaces of Spyder.

Context Menu:
Right clicking anywhere on the notebook area brings up the context menu 

that can be used to:
Create a new notebook 
Open an existing notebook anywhere on the users filesystem.
A list of recent notebooks
Rename the notebook
Selection and copy functions.
Zoom the notebook interface
[Rephrase this as not a numbered list]



Connecting an IPython console to the notebook


If you click on the tab of the particular notebook the user can create a console associated with the notebook [Image ??].

[Replace this screenshot for a gif showing from this image to the next one]

Once the console is opened, the variables of the notebook can be viewed in the Variable Explorer pane. (Limitation: The user may have to click enter once in the console for Spyder to update the variables in the variable explorer).





The + symbol on the top right corner can be used to create new notebooks that reside in the Temp location (Is it /tmp or is it in memory? Maybe we can make that clear so that the user does not run out of memory and crash)
When the user saves the notebook the notebook is re rendered (and restarts the kernel? Does the user need to rerun the notebook to refresh the variables and functions after save as ?) 





