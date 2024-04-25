<template>
  <div class="decoration-line"></div>
    <div class="component-logo">
      <router-link class="navbar-brand" to="/">
        <img src="@/assets/portaLogo.png" alt="" width="200" height="200" />
      </router-link>
    </div>
  <Div class="container">
    <div class="container-text">
  <h1>Cambiar Contraseña</h1>
</div>
  <p><input type="text" placeholder="Email" v-model="email" class="input-field" /></p>
  <p><button @click="resetPassword" class="custom-button">Enviar</button></p>
</Div>
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

<style scoped>
.container{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin-top: -350px;
}
.container-text h1{
  margin-bottom: 30px;
  font-size: 24px;
}
.component-logo{
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 1vh;
  margin-bottom: 2vh;
}

.input-field {
  width: 300px; /* Ajusta el ancho según tus preferencias */
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
}

.custom-button {
  padding: 10px 20px; /* Ajusta el padding según tus preferencias */
  background-color: #6FB84B; /* Color de fondo */
  color: #fff; /* Color del texto */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease; /* Transición suave */
}

.custom-button:hover {
  background-color: #5a9e3f; /* Cambia el color de fondo al pasar el ratón */
}
.decoration-line {
  height: 40px; /* Grosor de la línea */
  width: 100%; /* Ancho completo */
  background-color: #093b59; /* Color azul */
}

</style>
