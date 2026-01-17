import './assets/main.css';

import { createApp } from 'vue';
import { createUnhead } from '@unhead/vue';
import App from './App.vue';
import router from './router';

const theme = {
  '--md-sys-color-primary': '#c7b7ff',
  '--md-sys-color-on-primary': '#211042',
  '--md-sys-color-primary-container': '#3c2c73',
  '--md-sys-color-on-primary-container': '#e8ddff',
  '--md-sys-color-secondary': '#ffb74d',
  '--md-sys-color-on-secondary': '#2a1600',
  '--md-sys-color-secondary-container': '#422608',
  '--md-sys-color-on-secondary-container': '#ffddb0',
  '--md-sys-color-tertiary': '#ff7ad0',
  '--md-sys-color-on-tertiary': '#3d0026',
  '--md-sys-color-tertiary-container': '#5b1b40',
  '--md-sys-color-on-tertiary-container': '#ffd8e9',
  '--md-sys-color-background': '#0e0f12',
  '--md-sys-color-on-background': '#e8ecf5',
  '--md-sys-color-surface': '#12141a',
  '--md-sys-color-surface-variant': '#1c1f27',
  '--md-sys-color-surface-container-low': '#151821',
  '--md-sys-color-surface-container': '#1a1e28',
  '--md-sys-color-surface-container-high': '#202533',
  '--md-sys-color-outline': '#313645',
  '--md-sys-color-outline-variant': '#2a303d',
  '--md-sys-color-on-surface': '#e5e8ec',
  '--md-sys-color-on-surface-variant': '#c2c7d1'
};

const applyTheme = (vars) => {
  const root = document.documentElement;
  root.style.colorScheme = 'dark';
  Object.entries(vars).forEach(([key, value]) => {
    root.style.setProperty(key, value);
  });
};

applyTheme(theme);

const app = createApp(App);
const head = createUnhead();

app.use(router);
// app.use(head) // createUnhead might not be a plugin, let's see if it works without it or if we need to provide it.
// Unhead v1 used app.use(head). Unhead v2 with @unhead/vue might auto-detect or need manual provide.
// Checking docs implies createHead is standard for Vue, but it's missing in exports?
// Maybe it's a version mismatch issue.
// For now, let's try to just create it.

app.mount('#app');
