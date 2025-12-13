<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import { useHead } from '@unhead/vue';
import api from '../api/client';
import RichContent from '../components/RichContent.vue';

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
    
    // SEO
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
  <div class="content-page">
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="error" class="error">
      <h2>Error loading page</h2>
      <p>{{ error.message }}</p>
    </div>
    <article v-else-if="page">
      <h1>{{ page.title }}</h1>
      <RichContent :content="page.content" />
    </article>
    <div v-else>Select a page from the menu</div>
  </div>
</template>

<style scoped>
.content-page {
  max-width: 900px;
  margin: 0 auto;
}
h1 {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  color: var(--md-sys-color-on-surface);
}
</style>

