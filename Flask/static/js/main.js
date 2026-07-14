(function () {
  "use strict";

  var tabs = document.querySelectorAll(".story-tab");
  if (!tabs.length) return; // not on the story page

  var scenes = document.querySelectorAll(".story-scene");
  var copies = document.querySelectorAll(".story-copy-inner");
  var indexLabel = document.getElementById("storySceneIndex");
  var progressLabel = document.getElementById("storyProgress");
  var prevBtn = document.getElementById("storyPrev");
  var nextBtn = document.getElementById("storyNext");

  var total = tabs.length;
  var current = 0;

  function pad(n) {
    return n < 10 ? "0" + n : "" + n;
  }

  function goTo(index) {
    current = (index + total) % total;

    tabs.forEach(function (tab, i) {
      var active = i === current;
      tab.classList.toggle("active", active);
      tab.setAttribute("aria-selected", active ? "true" : "false");
    });

    scenes.forEach(function (scene) {
      scene.classList.toggle("is-active", Number(scene.dataset.scene) === current);
    });

    copies.forEach(function (copy) {
      copy.classList.toggle("is-active", Number(copy.dataset.scene) === current);
    });

    if (indexLabel) indexLabel.textContent = pad(current + 1) + " / " + pad(total);
    if (progressLabel) progressLabel.textContent = "Scene " + (current + 1) + " of " + total;
  }

  tabs.forEach(function (tab, i) {
    tab.addEventListener("click", function () {
      goTo(i);
    });
  });

  if (prevBtn) prevBtn.addEventListener("click", function () { goTo(current - 1); });
  if (nextBtn) nextBtn.addEventListener("click", function () { goTo(current + 1); });

  document.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") goTo(current - 1);
    if (e.key === "ArrowRight") goTo(current + 1);
  });
})();
