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
  }, { threshold: 0.02, rootMargin: '0px 0px 0px 0px' });

  document.querySelectorAll('.reveal').forEach(function (el) {
    scrollObserver.observe(el);
  });

  // ───── Sticky header border ─────
  var header = document.getElementById('site-header');
  window.addEventListener('scroll', function () {
    header.classList.toggle('scrolled', window.scrollY > 10);
  }, { passive: true });

})();
