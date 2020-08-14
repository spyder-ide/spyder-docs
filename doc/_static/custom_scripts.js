// Custom scripts for the Spyder docs site


;(function () {

    'use strict';

    // Set the active image for the tour based on the element's class
    function setActiveTourImage(activeElement) {
        var activeClass = "tour-screenshot-active";
        var classNames = activeElement.node.className.baseVal.split(" ");
        for (var i = 0; i < classNames.length; i++) {
            var imageToActivate = document.getElementById(classNames[i]);
            if (imageToActivate) break;
        };
        var imageToDeactivate = document.getElementsByClassName(activeClass)[0];
        imageToDeactivate.classList.remove(activeClass);
        imageToActivate.classList.add(activeClass);
    };

    // Interactive tour driver
    var driver = new Driver({
        animate: false,
        opacity: 0.1,
        padding: 0,
        allowClose: false,
        onHighlightStarted: setActiveTourImage,
    });

    // Event handler to start tour
    function startTour() {
        driver.start();
    };

    // Interactive tour of Spyder for Quickstart using Driver
    function setupTourDriver() {
        driver.defineSteps([
          {
            element: "#editor-rect",
            popover: {
              title: "Editor",
              description: "Spyder's Editor is really really slow",
              position: "right",
            },
          },
          {
            element: "#console-rect",
            popover: {
              title: "IPython Console",
              description: "The IPython Console runs code",
              position: "left",
            },
          },
          {
            element: "#options-menu-rect",
            popover: {
              title: "Options Menu",
              description: "Each pane has an options menu",
              position: "left",
            },
          },
        ]);

        document.getElementById("quickstart-tour-start").onclick = startTour;
    };

    // Document on load
    $(function(){
        setupTourDriver();
        startTour()
    });

}());
