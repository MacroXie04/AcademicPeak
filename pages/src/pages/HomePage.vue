<script setup>
import '@material/web/button/filled-button.js';
import '@material/web/button/outlined-button.js';
import '@material/web/icon/icon.js';
</script>

<template>
  <div class="page">
    <section class="hero surface">
      <div class="hero-copy">
        <p class="eyebrow">Web</p>
        <h1>Material Web</h1>
        <p class="lede">Material Web is Google's component library for building applications that work in any web framework.</p>
        <div class="hero-actions">
          <md-filled-button>Get started</md-filled-button>
          <md-outlined-button>Components</md-outlined-button>
        </div>
      </div>
      <div class="hero-visual" aria-hidden="true">
        <div class="blob blob-a"></div>
        <div class="blob blob-b"></div>
        <div class="blob blob-c"></div>
      </div>
    </section>

    <section class="section-block">
      <div class="section-header">
        <div>
          <p class="eyebrow">Announcements</p>
          <h2>Material Web Components are currently in maintenance mode.</h2>
          <p class="section-sub">No updates are currently being made to this library. Material 3 Expressive is not implemented on Web.</p>
        </div>
        <md-outlined-button>See all updates</md-outlined-button>
      </div>

      <div class="card-grid">
        <div class="info-card">
          <div class="card-media magenta"></div>
          <div class="card-body">
            <h3>Material Web 2.0</h3>
            <p>Start using lightweight and accessible Material Components in any web framework.</p>
          </div>
        </div>

        <div class="info-card">
          <div class="card-media orange"></div>
          <div class="card-body">
            <h3>Web roadmap</h3>
            <p>Material Web is currently in maintenance mode; the roadmap lists what used to be planned and all past releases.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.page {
  display: flex;
  flex-direction: column;
  gap: 28px;
  color: var(--md-sys-color-on-surface);
}

.hero {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  padding: 28px;
  background: linear-gradient(135deg, rgba(26, 20, 46, 0.9), rgba(40, 28, 58, 0.85));
  position: relative;
  overflow: hidden;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--md-sys-color-on-surface-variant);
  font: var(--md-sys-typescale-label-medium);
  margin-bottom: 4px;
}

h1 {
  font: var(--md-sys-typescale-display-small);
  margin: 0 0 12px;
}

.lede {
  font: var(--md-sys-typescale-body-large);
  color: var(--md-sys-color-on-surface-variant);
  max-width: 46ch;
}

.hero-actions {
  display: flex;
  gap: 12px;
  margin-top: 16px;
}

.hero-visual {
  position: relative;
  min-height: 220px;
  background: radial-gradient(circle at 20% 20%, rgba(255, 122, 208, 0.5), transparent 35%),
    radial-gradient(circle at 80% 30%, rgba(255, 183, 77, 0.5), transparent 35%),
    radial-gradient(circle at 50% 70%, rgba(199, 183, 255, 0.5), transparent 45%);
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.blob {
  position: absolute;
  filter: blur(24px);
  opacity: 0.9;
}

.blob-a {
  width: 240px;
  height: 200px;
  background: #ff7ad0;
  top: -20px;
  left: -10px;
}

.blob-b {
  width: 280px;
  height: 240px;
  background: #ffb74d;
  right: -40px;
  top: 30px;
}

.blob-c {
  width: 220px;
  height: 180px;
  background: #c7b7ff;
  bottom: -20px;
  left: 120px;
}

.section-block {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.section-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
}

h2 {
  font: var(--md-sys-typescale-headline-small);
  margin: 4px 0;
}

.section-sub {
  color: var(--md-sys-color-on-surface-variant);
  max-width: 80ch;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
}

.info-card {
  background: var(--md-sys-color-surface-container);
  color: var(--md-sys-color-on-surface);
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid var(--md-sys-color-outline-variant);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 4px 8px rgba(0, 0, 0, 0.08);
  transition: box-shadow 0.2s ease;
}

.info-card:hover {
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15), 0 8px 16px rgba(0, 0, 0, 0.12);
}

.card-media {
  height: 140px;
  background: #ff7ad0;
}

.card-media.orange {
  background: #ffb74d;
}

.card-body {
  padding: 16px 18px 18px;
}

h3 {
  font: var(--md-sys-typescale-title-large);
  margin: 0 0 6px;
}

p {
  margin: 0;
}

@media (max-width: 768px) {
  .section-header {
    flex-direction: column;
  }
}
</style>
