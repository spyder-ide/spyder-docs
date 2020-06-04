########
Overview
########

Spyder, the Scientific Python Development Environment, includes the following key features:

* :doc:`editor`:

  * Customizable syntax highlighting themes
  * :doc:`debugging` breakpoints and conditional breakpoints (through ``ipdb`` integration)
  * Interactive execution: Run line/selection, run cell, run file, re-run and debug
  * Run configuration settings:

    * Working directory selection
    * Command line options
    * Run in Current/dedicated/external console choice
    * Automatically clear variables or enter debugging

  * :guilabel:`Outline Explorer`: Navigate cells, functions, classes, blocks, and more
  * Real-time code introspection features (powered by ``rope`` and ``jedi``):

    * On-demand (:kbd:`Tab`) and "dot" automatic code completion
    * Automatic popup calltips showing function signatures
    * Go-to-definition for any symbol: Functions, classes, attributes, etc. (:kbd:`Ctrl`-Click or :kbd:`Ctrl-G` by default)

  * Occurrence highlighting: Select or double-click any word to show all other instances throughout the current document
  * On-the-fly automatic formatters (optional):

    * Automatic insertion of closing quotes parentheses, braces and brackets
    * Automatic indentation after 'else', 'elif', 'finally', etc.
    * Smart auto-indentation based on code structure
    * Automatic insertion of colons after for, if, def, etc.
    * Automatically fix mixed indentation, EOL characters and trailing spaces

  * Real-time code analysis:
    * Errors/warnings/problems (powered by ``pyflakes``)
    * PEP 8 and code style (powered by ``pycodestyle``)
    * Code annotation parsing and "Todo lists" (``TODO``, ``FIXME``, ``XXX``, etc.)

* :doc:`ipythonconsole`:

  * Any number of individual consoles, each executed in a separate, isolated processes
  * Each console uses the full IPython kernel as a backend with a light GUI frontend
  * Supports all of the powerful IPython magic commands and functionality
  * Automatic code completion and calltips, and automatic link to :doc:`help`
  * Range of code run options and interactivity
  * :doc:`debugging` integration with enhanced ``ipdb`` debugger and the :doc:`editor`
  * Inline display of Matplotlib graphics (optional)
  * The :guilabel:`User Module Reloader`, automatically re-importing modified source files

* :doc:`variableexplorer`:

  * Can list all global variables, functions, classes, and other objects, or filter them by several criteria
  * GUI-based editors for numerous data types (numeric, strings, collections, NumPy arrays, Pandas DataFrames, dates/times, images, and more)
  * Import/export data or an entire session from/to many formats (text, csv, NumPy files, MATLAB files)
  * Interactive data visualization options (plot, histogram, image...) using Matplotlib

* :doc:`help`:

  * Provides documentation or source code for any Python object (class, function, module...)
  * Can be triggered manually, on demand (:kbd:`Ctrl-I` by default) or automatically on typing a left parenthesis after a function name (optional)
  * Real-time rendering and rich HTML display of the popular ``numpydoc`` docstring format (powered by ``Sphinx``)

* :doc:`pylint`: Detects an array of style issues, bad practices, potential bugs, and other problems with your code (powered by ``pylint``)
* :doc:`profiler`: Measures the performance impact of every function in a file to identify bottlenecks and aid optimization
* :doc:`projects`: Allows for easy saving and restoring of settings, sessions and setup for working on multiple development efforts simultaneously
* :doc:`fileexplorer`: Integrated filesystem viewing supporting many common operations
* :doc:`findinfiles`: Find string occurrences in a file, directory, or entire project with full support for powerful regular expressions and excluded locations
* :doc:`onlinehelp`: Search and browse rich HTML documentation on installed Python modules, packages, functions, classes, builtins and more, including your own
* :doc:`historylog`: Chronologically records every command entered into any Spyder console with timestamps, syntax highlighting and de-duplication
* :doc:`internalconsole`: Provides access to viewing, exploring and controlling Spyder's own operation

* Preferences:

  * Fully customizable keyboard shortcuts editor
  * Selection of a custom Python interpreter to use for consoles
  * Choice of 10 built-in syntax coloring theme, or create your own
  * Toggle automatic editor and console introspection, analysis and helper features
  * Options to use a variety of graphics backends and display preferences
  * Much more...

* General Features:

  * MATLAB-like ``PYTHONPATH`` management dialog
  * User environment variables viewer/editor (Windows-only)
  * Handy links to useful resources and documentation (Python, Matplotlib, NumPy, Scipy, Qt, IPython, etc.)
  * Interactive tour, tutorial and shortcut cheat sheet for new users

Beyond its many built-in features, Spyder's abilities can be extended even further via its plugin system and API.
Spyder can also be used as a PyQt5 extension library, allowing you to build upon its functionality and embed its components, such as the interactive console, in your own software.
