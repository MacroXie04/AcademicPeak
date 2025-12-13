<script setup>
import { useRouter } from 'vue-router';
import '@material/web/tabs/primary-tab.js';
import '@material/web/tabs/tabs.js';

const props = defineProps({
  menus: {
    type: Array,
    default: () => []
  }
});

const router = useRouter();

const emit = defineEmits(['select']);

const onTabChange = (event) => {
  // event.target.activeTabIndex is the index
  const index = event.target.activeTabIndex;
  if (props.menus[index]) {
    emit('select', props.menus[index].id);
  }
};
</script>

<template>
  <header class="app-header">
    <div class="logo">SkillLoop</div>
    <md-tabs @change="onTabChange">
      <md-primary-tab 
        v-for="menu in menus" 
        :key="menu.id"
        :label="menu.name"
      ></md-primary-tab>
    </md-tabs>
  </header>
</template>

<style scoped>
.app-header {
  display: flex;
  align-items: center;
  padding: 0 16px;
  background: var(--md-sys-color-surface);
  border-bottom: 1px solid var(--md-sys-color-outline-variant);
}
.logo {
  font-size: 1.25rem;
  font-weight: bold;
  margin-right: 24px;
}
</style>

