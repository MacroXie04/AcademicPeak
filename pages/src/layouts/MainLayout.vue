<script setup>
import { ref, computed, watch } from 'vue';
import { useMenus } from '../composables/useMenus';
import AppHeader from '../components/AppHeader.vue';
import AppSidebar from '../components/AppSidebar.vue';

const { menus, loading, error } = useMenus();
const selectedRootId = ref(null);

// Select first menu by default when loaded
watch(menus, (newMenus) => {
  if (newMenus.length > 0 && !selectedRootId.value) {
    selectedRootId.value = newMenus[0].id;
  }
});

const currentSidebarItems = computed(() => {
  if (!selectedRootId.value) return [];
  const root = menus.value.find(m => m.id === selectedRootId.value);
  return root ? root.children || [] : [];
});

const handleRootSelect = (menuId) => {
  selectedRootId.value = menuId;
};
</script>

<template>
  <div class="layout-container">
    <AppHeader 
      :menus="menus" 
      @select="handleRootSelect" 
      class="layout-header"
    />
    
    <div class="layout-body">
      <AppSidebar 
        v-if="currentSidebarItems.length" 
        :items="currentSidebarItems" 
        class="layout-sidebar" 
      />
      
      <main class="layout-content">
        <router-view />
      </main>
    </div>
  </div>
</template>

<style scoped>
.layout-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}
.layout-header {
  flex: 0 0 auto;
}
.layout-body {
  display: flex;
  flex: 1;
  overflow: hidden;
}
.layout-sidebar {
  flex: 0 0 auto;
}
.layout-content {
  flex: 1;
  overflow-y: auto;
  padding: 24px;
}
</style>

