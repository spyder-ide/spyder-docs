// Custom scripts for the Spyder docs site


;(function () {

    'use strict';

    /* Top-level variables */

    // Interactive tour driver options
    var driverOptions = {
        animate: false,
        opacity: 0.1,
        padding: 0,
        allowClose: false,
        nextBtnText: 'Next <span class="tour-arrow">→</span>',
        prevBtnText: '<span class="tour-arrow">←</span> Previous',
    };

    // Step definitions for the quickstart tour
    var quickstartTourSteps = [
      {
        element: '#introduction-rect',
        popover: {
          title: 'Spyder',
          description: 'Spyder is a powerful scientific IDE for Python. Here, we will guide you through some of its most important features.',
          position: 'right',
        },
      },
      {
        element: '#toolbar-rect',
        popover: {
          title: 'Toolbar',
          description: 'The toolbar allows you to quickly access some of the most common commands in Spyder, such as run, save and debug files.',
          position: 'bottom',
        },
      },
      {
        element: '#statusbar-rect',
        popover: {
          title: 'Status Bar',
          description: 'The status bar shows your current Python environment, git branch, memory usage and various attributes of the currently active file.',
          position: 'top',
        },
      },
      {
        element: '#options-menu-rect',
        popover: {
          title: 'Options Menu',
          description: 'You can display each pane\'s options menu by clicking the "hamburger" icon at the top right. It contains useful settings and actions relevant to the pane.',
          position: 'right',
        },
      },
      {
        element: '#context-menu-rect',
        popover: {
          title: 'Context Menu',
          description: 'To display the context menu for a pane, right-click anywhere over it. The menu shows actions relevant to the element under your cursor.',
          position: 'right',
        },
      },
      {
        element: '#editor-rect',
        popover: {
          title: 'Editor',
          description: 'The <a href="editor.html">Editor</a> is the pane where you can create, open and edit files. It contains useful features like autocompletion, real-time analysis and syntax highlighting.',
          position: 'right',
        },
      },
      {
        element: '#console-rect',
        popover: {
          title: 'IPython Console',
          description: 'The <a href="ipythonconsole.html">Console</a> allows you to run your code from the Editor or interactively. You can also use it to control Spyder’s debugger.',
          position: 'left',
        },
      },
      {
        element: '#help-rect',
        popover: {
          title: 'Help',
          description: 'The <a href="help.html">Help</a> pane displays documentation for the objects you are using in the Editor or the IPython Console. To trigger Help, press Ctrl-I (Cmd-I on macOS) with your cursor over an object, or type its name in the Object field.',
          position: 'left',
        },
      },
      {
        element: '#variable-explorer-rect',
        popover: {
          title: 'Variable Explorer',
          description: 'The <a href="variableexplorer.html">Variable Explorer</a> allows you to browse and interact with the objects generated when running your code. Double-clicking a variable will open a specialized viewer, allowing you to inspect its contents.',
          position: 'left',
        },
      },
      {
        element: '#plots-rect',
        popover: {
          title: 'Plots',
          description: 'The <a href="plots.html">Plots</a> pane shows the figures and images created during your code execution. It allows you to browse, zoom, copy, and save the generated plots.',
          position: 'left',
        },
      },
      {
        element: '#files-rect',
        popover: {
          title: 'Files',
          description: 'The <a href="fileexplorer.html">Files</a> pane lets you browse the directories on your computer, open files in the Editor, and perform a variety of other operations.',
          position: 'left',
        },
      },
      {
        element: '#find-rect',
        popover: {
          title: 'Find',
          description: 'The <a href="findinfiles.html">Find</a> pane allows you to search for text in a given directory and navigate through all the found occurrences.',
          position: 'left',
        },
      },
      {
        element: '#profiler-rect',
        popover: {
          title: 'Profiler',
          description: 'The <a href="profiler.html">Profiler</a> helps you optimize your code by determining the run time and number of calls for every function and method used in a file. It also allows you to save and compare your results between runs.',
          position: 'left',
        },
      },
      {
        element: '#code-analysis-rect',
        popover: {
          title: 'Code Analysis',
          description: 'The <a href="pylint.html">Code Analysis</a> helps you improve the quality of your programs by detecting style issues, bad practices and potential bugs.',
          position: 'left',
        },
      },
    ];

    /* Helper functions */

    // Set the active image for the tour based on the element's class
    function setActiveTourImage(activeElement) {
        var activeClass = 'tour-screenshot-active';
        var classNames = activeElement.node.className.baseVal.split(' ');
        for (var i = 0; i < classNames.length; i++) {
            var imageToActivate = document.getElementById(classNames[i]);
            if (imageToActivate) break;
        };
        var imageToDeactivate = document.getElementsByClassName(activeClass)[0];
        imageToDeactivate.classList.remove(activeClass);
        imageToActivate.classList.add(activeClass);
    };

    // Add a span for the progress indicator to each tour step title
    function addProgressSpan(tourSteps) {
        for (var i = 0; i < tourSteps.length; i++) {
            var spanToAdd = '<span class="tour-progress-indicator">' + (i + 1).toString() + '/' + tourSteps.length.toString() + '</span>';
            tourSteps[i].popover.title += spanToAdd;
        };
    };

    /* Main functions */

    driverOptions.onHighlightStarted = setActiveTourImage;
    var driver = new Driver(driverOptions);

    // Event handler to start tour
    function startTour() {
        driver.start();
    };

    // Interactive tour of Spyder for Quickstart using Driver
    function setupTourDriver(driverObj, tourSteps) {
        addProgressSpan(tourSteps)
        driver.defineSteps(tourSteps);
        document.getElementById('quickstart-tour-start').onclick = startTour;
    };

    /* Fire when document ready */

    document.addEventListener('DOMContentLoaded', function() {
        setupTourDriver(driver, quickstartTourSteps);
        startTour();
    });

}());
