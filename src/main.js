import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCHpD6Vi5PBT9hwd5uLXQkyGNpjKJFsWUk",
  authDomain: "porta-inmobiliarias.firebaseapp.com",
  projectId: "porta-inmobiliarias",
  storageBucket: "porta-inmobiliarias.appspot.com",
  messagingSenderId: "682048475301",
  appId: "1:682048475301:web:80c81e61d6485e0efbfd4c"
};

initializeApp(firebaseConfig);

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
