<script setup>
defineProps({
  content: {
    type: String,
    default: ''
  }
});
</script>

<template>
  <div class="rich-content ck-content" v-html="content"></div>
</template>

<style>
/* Add CKEditor content styles or basic typography here */
.rich-content {
  line-height: 1.6;
  max-width: 800px;
}
.rich-content img {
  max-width: 100%;
  height: auto;
}
.rich-content h1, .rich-content h2, .rich-content h3 {
  margin-top: 1.5em;
  margin-bottom: 0.5em;
}
.rich-content p {
  margin-bottom: 1em;
}
.rich-content ul, .rich-content ol {
  padding-left: 2em;
  margin-bottom: 1em;
}
.rich-content blockquote {
  border-left: 4px solid var(--md-sys-color-primary);
  padding-left: 1em;
  margin-left: 0;
  color: var(--md-sys-color-on-surface-variant);
}
</style>

