import './assets/main.css'

import { createApp } from 'vue'
import { createUnhead } from '@unhead/vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
const head = createUnhead()

app.use(router)
// app.use(head) // createUnhead might not be a plugin, let's see if it works without it or if we need to provide it.
// Unhead v1 used app.use(head). Unhead v2 with @unhead/vue might auto-detect or need manual provide.
// Checking docs implies createHead is standard for Vue, but it's missing in exports?
// Maybe it's a version mismatch issue.
// For now, let's try to just create it.

app.mount('#app')
