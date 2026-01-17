<script setup>
import '@material/web/icon/icon.js';
import '@material/web/iconbutton/icon-button.js';

defineProps({
  title: {
    type: String,
    default: 'SkillLoop'
  },
  subtitle: {
    type: String,
    default: 'Learn with Material Web'
  }
});
</script>

<template>
  <header class="app-header surface">
    <div class="title-block">
      <div class="title">{{ title }}</div>
      <div class="subtitle">{{ subtitle }}</div>
    </div>
    <div class="actions">
      <md-icon-button aria-label="search">
        <md-icon>search</md-icon>
      </md-icon-button>
      <md-icon-button aria-label="notifications">
        <md-icon>notifications</md-icon>
      </md-icon-button>
      <md-icon-button aria-label="account">
        <md-icon>account_circle</md-icon>
      </md-icon-button>
    </div>
  </header>
</template>

<style scoped>
.app-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 24px 32px;
  position: sticky;
  top: 0;
  z-index: 10;
  border-bottom: 1px solid var(--md-sys-color-outline-variant);
  backdrop-filter: blur(6px);
}

.title-block {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.title {
  font: var(--md-sys-typescale-title-large);
}

.subtitle {
  font: var(--md-sys-typescale-body-small);
  color: var(--md-sys-color-on-surface-variant);
}

.actions {
  display: flex;
  gap: 4px;
}
</style>
