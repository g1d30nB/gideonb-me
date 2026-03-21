/*
 * ═══════════════════════════════════════
 * Gideon Portfolio — App Controller
 * ═══════════════════════════════════════
 * Handles: SPA routing, page transitions,
 * article rendering, scroll reveals, nav state
 */

(function () {
  'use strict';

  // ───── DOM refs ─────
  const homePage         = document.getElementById('home-page');
  const articlePage      = document.getElementById('article-page');
  const writingPage      = document.getElementById('writing-page');
  const articlesList     = document.getElementById('articles-list');
  const featuredArticles = document.getElementById('featured-articles');
  const writingArticlesList = document.getElementById('writing-articles-list');
  const mainNav          = document.getElementById('main-nav');
  const header           = document.getElementById('site-header');
  const pageContainer    = document.getElementById('page-container');

  let currentPage = 'home';

  // ───── Get articles for homepage (first 3 + latest) ─────
  function getHomepageArticles() {
    const first3 = ARTICLES.slice(0, 3);
    const latest = ARTICLES[ARTICLES.length - 1];
    // Avoid duplicates if latest is already in first 3
    if (first3.find(a => a.slug === latest.slug)) return first3;
    return [...first3, latest];
  }

  // ───── Render article list on homepage ─────
  function renderArticlesList() {
    const articles = getHomepageArticles();
    articlesList.innerHTML = articles.map(a => `
      <div class="article-row reveal" data-article="${a.slug}" role="link" tabindex="0">
        <span class="article-title-text">${a.title}</span>
        <span class="article-meta">
          <span class="article-category">${a.category}</span><br>
          <span class="article-read-time">${a.readTime}</span>
        </span>
        <img class="article-thumb" src="${a.thumb}" alt="" loading="lazy">
        <svg class="article-arrow" width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M4 12L12 4M12 4H6M12 4V10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
    `).join('');

    // Attach click handlers
    articlesList.querySelectorAll('.article-row').forEach(row => {
      row.addEventListener('click', () => navigateTo('article', row.dataset.article));
      row.addEventListener('keydown', e => { if (e.key === 'Enter') navigateTo('article', row.dataset.article); });
    });

    // Observe new reveals
    articlesList.querySelectorAll('.reveal').forEach(el => scrollObserver.observe(el));
  }

  // ───── Render Writing Page ─────
  function renderWritingPage() {
    // Featured articles
    const featured = ARTICLES.filter(a => a.featured);
    featuredArticles.innerHTML = featured.map(a => `
      <div class="featured-card" data-article="${a.slug}">
        <img class="featured-card-img" src="${a.heroImg}" alt="">
        <div class="featured-card-body">
          <span class="featured-card-category">${a.category}</span>
          <h3 class="featured-card-title">${a.title}</h3>
          <span class="featured-card-meta">${a.readTime}</span>
        </div>
      </div>
    `).join('');
    
    // Click handlers for featured cards
    featuredArticles.querySelectorAll('.featured-card').forEach(card => {
      card.addEventListener('click', () => navigateTo('article', card.dataset.article));
    });

    // All articles list (excluding featured, since they're shown as hero cards above)
    const nonFeatured = ARTICLES.filter(a => !a.featured);
    writingArticlesList.innerHTML = nonFeatured.map(a => `
      <div class="article-row" data-article="${a.slug}" role="link" tabindex="0">
        <span class="article-title-text">${a.title}</span>
        <span class="article-meta">
          <span class="article-category">${a.category}</span><br>
          <span class="article-read-time">${a.readTime}</span>
        </span>
        <img class="article-thumb" src="${a.thumb}" alt="" loading="lazy">
        <svg class="article-arrow" width="16" height="16" viewBox="0 0 16 16" fill="none">
          <path d="M4 12L12 4M12 4H6M12 4V10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
    `).join('');

    writingArticlesList.querySelectorAll('.article-row').forEach(row => {
      row.addEventListener('click', () => navigateTo('article', row.dataset.article));
      row.addEventListener('keydown', e => { if (e.key === 'Enter') navigateTo('article', row.dataset.article); });
    });
  }

  // ───── Render article page ─────
  function renderArticle(slug) {
    const article = ARTICLES.find(a => a.slug === slug);
    if (!article) return;

    document.getElementById('article-title').textContent = article.title;
    document.getElementById('article-subtitle').textContent = article.subtitle || '';
    document.getElementById('article-category').textContent = article.category;
    document.getElementById('article-footer-category').textContent = article.category;
    document.getElementById('article-readtime').textContent = article.readTime;
    document.getElementById('article-hero-img').src = article.heroImg;
    document.getElementById('article-hero-img').alt = article.title;
    document.getElementById('article-body').innerHTML = article.body;

    // Update page title
    document.title = `${article.title} — Gideon Bullock`;
  }

  // ───── Navigation / Transitions ─────
  function navigateTo(page, slug) {
    if (page === 'home' && currentPage === 'home') return;
    if (page === 'article' && !slug) return;
    if (page === 'writing-page' && currentPage === 'writing-page') return;

    const transition = () => {
      // Hide all pages
      homePage.classList.remove('active');
      articlePage.classList.remove('active', 'article-enter');
      writingPage.classList.remove('active');

      if (page === 'home') {
        homePage.classList.add('active');
        currentPage = 'home';
        document.title = 'Gideon Bullock — Design Leader';
        updateNav('home');
        window.history.pushState({ page: 'home' }, '', '#');

        // Re-observe reveals that might not be visible yet
        homePage.querySelectorAll('.reveal:not(.visible)').forEach(el => scrollObserver.observe(el));
      } else if (page === 'article') {
        renderArticle(slug);
        articlePage.classList.add('active', 'article-enter');
        currentPage = 'article';
        updateNav('article');
        window.history.pushState({ page: 'article', slug }, '', `#article/${slug}`);
      } else if (page === 'writing-page') {
        renderWritingPage();
        writingPage.classList.add('active');
        currentPage = 'writing-page';
        updateNav('writing-page');
        window.history.pushState({ page: 'writing-page' }, '', '#writing');
      }

      window.scrollTo({ top: 0, behavior: 'instant' });
    };

    // Use View Transitions API if available
    if (document.startViewTransition) {
      document.startViewTransition(transition);
    } else {
      // Fallback: manual fade
      pageContainer.classList.add('page-transition-out');
      setTimeout(() => {
        transition();
        pageContainer.classList.remove('page-transition-out');
        pageContainer.classList.add('page-transition-in');
        setTimeout(() => pageContainer.classList.remove('page-transition-in'), 400);
      }, 250);
    }
  }

  // ───── Update nav for current page ─────
  function updateNav(page) {
    if (page === 'writing-page') {
      mainNav.innerHTML = `
        <a href="#" class="nav-home" data-nav="home">
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M10 4L6 8L10 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Home
        </a>
        <a href="#" data-nav="writing-page" style="color:#1e1a16">Writing</a>
      `;
    } else if (page === 'article') {
      mainNav.innerHTML = `
        <a href="#" class="nav-home" data-nav="home">
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M10 4L6 8L10 12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Home
        </a>
        <a href="#" data-nav="writing-page">Writing</a>
      `;
    } else {
      mainNav.innerHTML = `
        <a href="#" data-nav="writing-page">Writing</a>
      `;
    }
    attachNavHandlers();
  }

  // ───── Nav click handlers ─────
  function attachNavHandlers() {
    document.querySelectorAll('[data-nav]').forEach(link => {
      link.addEventListener('click', e => {
        e.preventDefault();
        const action = link.dataset.nav;

        if (action === 'home') {
          navigateTo('home');
        } else if (action === 'writing-page') {
          navigateTo('writing-page');
        } else if (action === 'writing' || action === 'expertise') {
          if (currentPage !== 'home') {
            navigateTo('home');
            setTimeout(() => {
              const target = document.getElementById(action);
              if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 400);
          } else {
            const target = document.getElementById(action);
            if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        } else if (action === 'home-writing' || action === 'home-expertise') {
          const section = action.replace('home-', '');
          navigateTo('home');
          setTimeout(() => {
            const target = document.getElementById(section);
            if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }, 400);
        }
      });
    });
  }

  // ───── Back link handlers ─────
  document.querySelectorAll('.back-link').forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      navigateTo('home');
    });
  });

  // ───── Browser back/forward ─────
  window.addEventListener('popstate', e => {
    if (e.state?.page === 'article' && e.state.slug) {
      navigateTo('article', e.state.slug);
    } else if (e.state?.page === 'writing-page') {
      navigateTo('writing-page');
    } else {
      navigateTo('home');
    }
  });

  // ───── Scroll Reveal Observer ─────
  const scrollObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        scrollObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach(el => scrollObserver.observe(el));

  // ───── Sticky header border ─────
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 10);
  }, { passive: true });

  // ───── Handle initial hash route ─────
  function handleInitialRoute() {
    const hash = window.location.hash;
    if (hash.startsWith('#article/')) {
      const slug = hash.replace('#article/', '');
      renderArticle(slug);
      articlePage.classList.add('active', 'article-enter');
      homePage.classList.remove('active');
      writingPage.classList.remove('active');
      currentPage = 'article';
      updateNav('article');
    } else if (hash === '#writing') {
      renderWritingPage();
      writingPage.classList.add('active');
      homePage.classList.remove('active');
      articlePage.classList.remove('active');
      currentPage = 'writing-page';
      updateNav('writing-page');
    } else {
      window.history.replaceState({ page: 'home' }, '', '#');
    }
  }

  // ───── Init ─────
  renderArticlesList();
  renderWritingPage();
  attachNavHandlers();
  handleInitialRoute();

})();
