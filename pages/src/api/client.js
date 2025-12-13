import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default {
  getMenus() {
    return apiClient.get('/menus/');
  },
  getPages(params) {
    return apiClient.get('/pages/', { params });
  },
  getPage(slug) {
    return apiClient.get(`/pages/${slug}/`);
  },
};

