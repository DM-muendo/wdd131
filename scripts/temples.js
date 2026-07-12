document.addEventListener('DOMContentLoaded', function () {
  const yearEl = document.getElementById('currentyear');
  const lastModifiedEl = document.getElementById('lastModified');
  const navToggle = document.querySelector('.nav-toggle');
  const siteNav = document.querySelector('.site-nav');
  const navLinks = siteNav ? siteNav.querySelectorAll('a') : [];

  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  if (lastModifiedEl) {
    lastModifiedEl.textContent = 'Last modified: ' + document.lastModified;
  }

  function updateToggleState(isOpen) {
    if (!navToggle) return;
    navToggle.setAttribute('aria-expanded', String(isOpen));
    navToggle.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
    navToggle.textContent = isOpen ? '✕' : '☰';
  }

  function resetMenu() {
    if (!siteNav) return;
    if (window.innerWidth >= 760) {
      siteNav.classList.remove('open');
      updateToggleState(false);
    }
  }

  if (navToggle && siteNav) {
    navToggle.addEventListener('click', function () {
      const isOpen = siteNav.classList.toggle('open');
      updateToggleState(isOpen);
    });

    navLinks.forEach(function (link) {
      link.addEventListener('click', function () {
        if (siteNav.classList.contains('open')) {
          siteNav.classList.remove('open');
          updateToggleState(false);
        }
      });
    });

    window.addEventListener('resize', resetMenu);
    resetMenu();
  }
});
