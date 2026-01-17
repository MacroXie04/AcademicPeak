<script setup>
import { computed, ref } from 'vue';
import { useRouter } from 'vue-router';
import MenuTree from './MenuTree.vue';
import '@material/web/icon/icon.js';
import '@material/web/iconbutton/icon-button.js';
import '@material/web/textfield/outlined-text-field.js';
import '@material/web/list/list.js';
import '@material/web/list/list-item.js';

const router = useRouter();
const search = ref('');

const props = defineProps({
  menus: {
    type: Array,
    default: () => []
  },
  items: {
    type: Array,
    default: () => []
  },
  rootPages: {
    type: Array,
    default: () => []
  },
  selectedRootId: {
    type: [String, Number, null],
    default: null
  },
  collapsed: {
    type: Boolean,
    default: false
  }
});

const emit = defineEmits(['select-root', 'toggle-collapse']);

const filteredMenus = computed(() => {
  if (!search.value) return props.menus;
  return props.menus.filter(m => m.name.toLowerCase().includes(search.value.toLowerCase()));
});

const goHome = () => router.push('/');

const goToPage = (slug) => {
  router.push(`/page/${slug}`);
};
</script>

<template>
  <aside class="app-sidebar">
    <div class="sidebar-inner">
      <div class="brand-row">
        <div class="logo-mark">SL</div>
        <div class="brand-text">
          <div class="brand-title">SkillLoop</div>
        </div>
        <md-icon-button aria-label="home" @click="goHome">
          <md-icon>home</md-icon>
        </md-icon-button>
        <md-icon-button aria-label="收起侧边栏" @click="emit('toggle-collapse')">
          <md-icon>menu_open</md-icon>
        </md-icon-button>
      </div>

      <md-outlined-text-field
        v-model="search"
        label="Search topics"
        class="search"
      >
        <md-icon slot="leading-icon">search</md-icon>
      </md-outlined-text-field>

      <div class="section">
        <div class="section-title">Browse</div>
        <md-list>
          <md-list-item
            v-for="menu in filteredMenus"
            :key="menu.id"
            type="button"
            :selected="menu.id === selectedRootId"
            @click="emit('select-root', menu.id)"
            class="menu-root"
          >
            <md-icon slot="start">folder</md-icon>
            <div slot="headline">{{ menu.name }}</div>
          </md-list-item>
        </md-list>
      </div>

      <div v-if="rootPages.length || items.length" class="section nested">
        <div class="section-title">Content</div>
        <md-list v-if="rootPages.length" class="pages-root">
          <md-list-item
            v-for="page in rootPages"
            :key="'root-page-' + page.id"
            type="button"
            @click="goToPage(page.slug)"
          >
            <md-icon slot="start">article</md-icon>
            <div slot="headline">{{ page.title }}</div>
          </md-list-item>
        </md-list>
        <MenuTree :items="items" />
      </div>
    </div>
  </aside>
</template>

<style scoped>
.app-sidebar {
  width: 100%;
  background: linear-gradient(180deg, rgba(26, 30, 40, 0.96), rgba(22, 25, 33, 0.98));
  color: var(--md-sys-color-on-surface);
  height: 100%;
  overflow-y: auto;
  padding: 20px 18px;
}

.sidebar-inner {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.brand-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-mark {
  width: 36px;
  height: 36px;
  border-radius: 12px;
  background: linear-gradient(135deg, #ff7ad0 0%, #ffb74d 50%, #c7b7ff 100%);
  display: grid;
  place-items: center;
  font-weight: 700;
  color: #1e102f;
  box-shadow: var(--md-elevation-level2);
}

.brand-text {
  flex: 1;
}

.brand-title {
  font: var(--md-sys-typescale-title-medium);
}

.search {
  width: 100%;
}

.section {
  background: var(--md-sys-color-surface-container-low);
  border: 1px solid var(--md-sys-color-outline-variant);
  border-radius: var(--md-sys-shape-corner-medium);
  padding: 12px;
  box-shadow: var(--md-elevation-level1);
}

.section-title {
  font: var(--md-sys-typescale-title-small);
  color: var(--md-sys-color-on-surface);
  margin-bottom: 8px;
}

.menu-root {
  border-radius: var(--md-sys-shape-corner-small);
}

.nested {
  background: var(--md-sys-color-surface-container);
}

.pages-root md-list-item {
  border-radius: var(--md-sys-shape-corner-small);
}
</style>
