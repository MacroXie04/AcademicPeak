import { ref, onMounted } from 'vue';
import api from '../api/client';

export function useMenus() {
  const menus = ref([]);
  const loading = ref(false);
  const error = ref(null);

  const fetchMenus = async () => {
    loading.value = true;
    try {
      const response = await api.getMenus();
      menus.value = response.data;
    } catch (err) {
      error.value = err;
      console.error('Error fetching menus:', err);
    } finally {
      loading.value = false;
    }
  };

  onMounted(() => {
    fetchMenus();
  });

  return {
    menus,
    loading,
    error,
    fetchMenus
  };
}

