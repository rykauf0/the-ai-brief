/* ================================================================
   THE AI BRIEF — main.js
   Topic filter + reading progress bar
   Progressive enhancement — site works fully without JS
   ================================================================ */

/* ── Topic filter ── */
(function () {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.issue-card');
  if (!filterBtns.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const topic = btn.dataset.topic;

      cards.forEach(card => {
        if (topic === 'all') {
          card.style.display = '';
        } else {
          const topics = (card.dataset.topics || '').split(' ');
          card.style.display = topics.includes(topic) ? '' : 'none';
        }
      });
    });
  });
})();

/* ── Mobile nav toggle ── */
(function () {
  const btn = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.masthead-nav');
  if (!btn || !nav) return;

  btn.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', isOpen);
  });
})();

/* ── Reading progress bar ── */
(function () {
  const bar = document.getElementById('reading-progress');
  if (!bar) return;

  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        bar.style.width = pct.toFixed(1) + '%';
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
})();
