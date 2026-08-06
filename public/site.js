/*
 * Gideon Bullock — site behaviour
 * The interactive parts of the old app.js, unchanged in effect.
 * All routing, page swapping, and article rendering are gone: those are
 * real pages now, built by Astro.
 */
(function () {
  'use strict';

  // ───── Scroll Reveal Observer ─────
  var scrollObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        scrollObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach(function (el) {
    scrollObserver.observe(el);
  });

  // ───── Sticky header border ─────
  var header = document.getElementById('site-header');
  window.addEventListener('scroll', function () {
    header.classList.toggle('scrolled', window.scrollY > 10);
  }, { passive: true });

  // ───── Portrait: mouse-driven frame switching ─────
  (function initPortrait() {
    var imgs = document.querySelectorAll('.portrait-wrapper img');
    if (imgs.length < 3) return; // no portrait on page
    var frames = [imgs[1], imgs[2]]; // skip spacer
    var currentFrame = 0;
    var hasMouse = false;

    function setFrame(index) {
      if (index === currentFrame) return;
      frames[currentFrame].classList.remove('active');
      currentFrame = index;
      frames[currentFrame].classList.add('active');
    }

    document.addEventListener('mousemove', function (e) {
      hasMouse = true;
      var ratio = e.clientX / window.innerWidth;
      var index = Math.min(Math.floor(ratio * frames.length), frames.length - 1);
      setFrame(index);
    });

    document.addEventListener('touchmove', function (e) {
      var touch = e.touches[0];
      var ratio = touch.clientX / window.innerWidth;
      var index = Math.min(Math.floor(ratio * frames.length), frames.length - 1);
      setFrame(index);
    }, { passive: true });

    // Ambient fallback for no-mouse devices
    var sequence = [0, 1];
    var seqIndex = 0;
    setInterval(function () {
      if (hasMouse) return;
      seqIndex = (seqIndex + 1) % sequence.length;
      setFrame(sequence[seqIndex]);
    }, 10000);
  })();
})();
