<script setup>
import { ref, computed, watch, onMounted } from 'vue';
import { useMenus } from '../composables/useMenus';
import AppSidebar from '../components/AppSidebar.vue';
import '@material/web/iconbutton/icon-button.js';
import '@material/web/icon/icon.js';

const { menus } = useMenus();
const selectedRootId = ref(null);
const sidebarCollapsed = ref(window.innerWidth <= 768);

watch(menus, (newMenus) => {
  if (newMenus.length > 0 && !selectedRootId.value) {
    selectedRootId.value = newMenus[0].id;
  }
});

const currentRoot = computed(() => menus.value.find(m => m.id === selectedRootId.value));
const currentSidebarItems = computed(() => currentRoot.value?.children || []);
const currentRootPages = computed(() => currentRoot.value?.pages || []);

const handleRootSelect = (menuId) => {
  selectedRootId.value = menuId;
};

const toggleSidebar = () => {
  sidebarCollapsed.value = !sidebarCollapsed.value;
};
</script>

<template>
  <div class="layout-container" :class="{ 'sidebar-collapsed': sidebarCollapsed }">
    <AppSidebar
      :menus="menus"
      :items="currentSidebarItems"
      :root-pages="currentRootPages"
      :selected-root-id="selectedRootId"
      :collapsed="sidebarCollapsed"
      class="layout-sidebar"
      @select-root="handleRootSelect"
      @toggle-collapse="toggleSidebar"
    />

    <!-- Expand button when sidebar is collapsed -->
    <button
      v-if="sidebarCollapsed"
      class="sidebar-expand-btn"
      @click="toggleSidebar"
      aria-label="展开侧边栏"
    >
      <md-icon>menu</md-icon>
    </button>

    <div class="layout-body">
      <main class="layout-content">
        <router-view />
      </main>
    </div>
  </div>
</template>

<style scoped>
.layout-container {
  display: flex;
  min-height: 100vh;
  background: transparent;
}

.layout-sidebar {
  position: fixed;
  top: 0;
  left: 0;
  width: 320px;
  height: 100vh;
  border-right: 1px solid var(--md-sys-color-outline-variant);
  backdrop-filter: blur(8px);
  z-index: 100;
  transition: transform 0.3s ease;
}

.sidebar-collapsed .layout-sidebar {
  transform: translateX(-100%);
}

.sidebar-expand-btn {
  position: fixed;
  top: 16px;
  left: 16px;
  z-index: 99;
  width: 48px;
  height: 48px;
  border: none;
  border-radius: 12px;
  background: var(--md-sys-color-surface-container-high);
  color: var(--md-sys-color-on-surface);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--md-elevation-level2);
  transition: background 0.2s ease;
}

.sidebar-expand-btn:hover {
  background: var(--md-sys-color-surface-container-highest);
}

.layout-body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  flex: 1;
  margin-left: 320px;
  background: linear-gradient(135deg, rgba(32, 37, 51, 0.7), rgba(26, 30, 40, 0.85));
  transition: margin-left 0.3s ease;
}

.sidebar-collapsed .layout-body {
  margin-left: 0;
}

.layout-content {
  padding: 24px 32px 32px;
  overflow-y: auto;
  flex: 1;
}

@media (max-width: 960px) {
  .layout-sidebar {
    width: 260px;
  }
  .layout-body {
    margin-left: 260px;
  }
}

@media (max-width: 768px) {
  .layout-sidebar {
    width: 280px;
  }
  .layout-body {
    margin-left: 0;
  }
}
</style>
