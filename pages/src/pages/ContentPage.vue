<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import { useHead } from '@unhead/vue';
import api from '../api/client';
import RichContent from '../components/RichContent.vue';
import '@material/web/progress/circular-progress.js';
import '@material/web/icon/icon.js';

const route = useRoute();
const page = ref(null);
const loading = ref(false);
const error = ref(null);

const fetchPage = async (slug) => {
  loading.value = true;
  error.value = null;
  try {
    const response = await api.getPage(slug);
    page.value = response.data;

    useHead({
      title: page.value.seo_title || page.value.title,
      meta: [
        { name: 'description', content: page.value.seo_description },
        { name: 'keywords', content: page.value.seo_keywords }
      ]
    });
  } catch (err) {
    error.value = err;
    page.value = null;
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  if (route.params.slug) {
    fetchPage(route.params.slug);
  }
});

watch(() => route.params.slug, (newSlug) => {
  if (newSlug) {
    fetchPage(newSlug);
  }
});
</script>

<template>
  <div class="content-shell surface">
    <div v-if="loading" class="loading">
      <md-circular-progress indeterminate></md-circular-progress>
      <span>Loading content...</span>
    </div>

    <div v-else-if="error" class="error">
      <md-icon class="error-icon">warning</md-icon>
      <div>
        <h2>Error loading page</h2>
        <p>{{ error.message }}</p>
      </div>
    </div>

    <article v-else-if="page" class="content-article">
      <p class="eyebrow">{{ page.category || 'Content' }}</p>
      <h1>{{ page.title }}</h1>
      <RichContent :content="page.content" />
    </article>

    <div v-else class="placeholder">Select a page from the menu</div>
  </div>
</template>

<style scoped>
.content-shell {
  padding: 24px 28px;
  border-radius: var(--md-sys-shape-corner-large);
  border: 1px solid var(--md-sys-color-outline-variant);
  box-shadow: var(--md-elevation-level1);
  max-width: 980px;
}

.loading, .error {
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--md-sys-color-on-surface-variant);
}

.error-icon {
  color: #ffb74d;
}

.content-article h1 {
  font: var(--md-sys-typescale-headline-medium);
  margin: 6px 0 18px;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--md-sys-color-on-surface-variant);
  font: var(--md-sys-typescale-label-medium);
}

.placeholder {
  color: var(--md-sys-color-on-surface-variant);
}
</style>
