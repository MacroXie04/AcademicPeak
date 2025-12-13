<script setup>
import MenuTree from './MenuTree.vue';

defineProps({
  items: {
    type: Array,
    default: () => []
  }
});
</script>

<template>
  <aside class="app-sidebar">
    <MenuTree :items="items" />
  </aside>
</template>

<style scoped>
.app-sidebar {
  width: 280px;
  background: var(--md-sys-color-surface-container);
  border-right: 1px solid var(--md-sys-color-outline-variant);
  overflow-y: auto;
  height: 100%;
}
</style>

