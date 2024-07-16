import './assets/main.css'

import { createApp } from 'vue';
import App from './App.vue';
import router from './router'
import store from './store';
import directives from '@/directives';
import components from "@/components/UI";

const app = createApp(App)

components.forEach(component => {
    // console.log(component.name);
    app.component(component.name, component)
})

directives.forEach(directive => {
    app.directive(directive.name, directive);
});

app.use(router)
app.use(store)

app.mount('#app')
