<template>
  <h1>Cambiar Contraseña</h1>
  <p><input type="text" placeholder="Email" v-model="email" /></p>
  <p><button @click="resetPassword">Enviar</button></p>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getAuth, sendPasswordResetEmail, onAuthStateChanged, } from "firebase/auth";
import router from "@/router";
const email = ref("");
const isLoggedIn = ref(false);

let auth;

onMounted(() => {
  auth = getAuth();
  onAuthStateChanged(auth, (user) => {
    if (user) {
      isLoggedIn.value = true;
    } else {
      isLoggedIn.value = false;
    }
  });
});

const resetPassword = () => {
  sendPasswordResetEmail(getAuth(), email.value)
    .then((data) => {
      alert("Se le envio un correo");

    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;

    });
}
</script>
