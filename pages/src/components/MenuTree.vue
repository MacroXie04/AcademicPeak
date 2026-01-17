<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import '@material/web/list/list.js';
import '@material/web/list/list-item.js';
import '@material/web/icon/icon.js';

const props = defineProps({
  items: {
    type: Array,
    default: () => []
  },
  level: {
    type: Number,
    default: 0
  }
});

const openItems = ref(new Set());
const router = useRouter();

const toggle = (item) => {
  const hasContent = (item.children && item.children.length > 0) || (item.pages && item.pages.length > 0);
  if (!hasContent) return;
  const next = new Set(openItems.value);
  if (next.has(item.id)) {
    next.delete(item.id);
  } else {
    next.add(item.id);
  }
  openItems.value = next;
};

const navTo = (slug) => {
  router.push(`/page/${slug}`);
};

const isOpen = (item) => openItems.value.has(item.id);
const hasSubItems = (item) => (item.children && item.children.length > 0) || (item.pages && item.pages.length > 0);
</script>

<template>
  <md-list class="menu-list">
    <template v-for="item in items" :key="item.id">
      <!-- Menu Node -->
      <md-list-item 
        type="button"
        @click="toggle(item)"
        class="menu-item"
      >
        <div slot="headline">{{ item.name }}</div>
        <md-icon slot="start" v-if="level === 0">folder</md-icon>
        <md-icon slot="start" v-else>folder_open</md-icon>
        
        <md-icon slot="end" v-if="hasSubItems(item)">
          {{ isOpen(item) ? 'expand_less' : 'expand_more' }}
        </md-icon>
      </md-list-item>
      
      <!-- Expanded Content -->
      <div v-if="hasSubItems(item) && isOpen(item)" class="nested-menu">
        <!-- Pages inside this Menu -->
        <md-list-item 
          v-for="page in item.pages" 
          :key="'page-' + page.id"
          type="button"
          @click="navTo(page.slug)"
          class="page-item"
          :class="{ 'active': $route.path === `/page/${page.slug}` }"
        >
          <div slot="headline">{{ page.title }}</div>
          <md-icon slot="start">article</md-icon>
        </md-list-item>

        <!-- Sub Menus -->
        <MenuTree :items="item.children" :level="level + 1" />
      </div>
    </template>
  </md-list>
</template>

<style scoped>
.menu-list {
  --md-list-container-color: transparent;
}
.nested-menu {
  padding-left: 12px; 
  border-left: 1px solid var(--md-sys-color-outline-variant);
  margin-left: 4px;
}
.menu-item {
  cursor: pointer;
  background-color: var(--md-sys-color-surface-container-low);
  border-radius: var(--md-sys-shape-corner-small);
}
.page-item {
  cursor: pointer;
  border-radius: var(--md-sys-shape-corner-small);
}
.active {
  background-color: var(--md-sys-color-secondary-container);
  color: var(--md-sys-color-on-secondary-container);
}
</style>
