// Initialize Video.js on documentation screencasts (sphinxcontrib-video output).

(function () {
  "use strict";

  const PLAYER_OPTIONS = {
    controls: true,
    fluid: true,
    inactivityTimeout: 0,
    preload: "auto",
    controlBar: {
      children: [
        "playToggle",
        "volumePanel",
        "currentTimeDisplay",
        "timeDivider",
        "durationDisplay",
        "progressControl",
        "fullscreenToggle",
      ],
    },
  };

  function initDocVideos() {
    if (typeof videojs === "undefined") {
      return;
    }

    document
      .querySelectorAll(".sphinx-contrib-video-container video")
      .forEach(function (el) {
        if (videojs.getPlayer(el)) {
          return;
        }

        el.classList.add("video-js");

        const player = videojs(el, PLAYER_OPTIONS);

        player.one("loadedmetadata", function () {
          const w = player.videoWidth();
          const h = player.videoHeight();
          if (w && h) {
            player.aspectRatio(w + ":" + h);
          }
        });
      });
  }

  document.addEventListener("DOMContentLoaded", initDocVideos);
})();
