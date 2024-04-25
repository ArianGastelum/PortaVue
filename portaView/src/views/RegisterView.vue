<template>
 <div class="decoration-line"></div>
    <div class="component-logo">
      <router-link class="navbar-brand" to="/">
        <img src="@/assets/portaLogo.png" alt="" width="200" height="200" />
      </router-link>
    </div>
  <div class="container">
    <div class="container-text">
  <h1>Crear Nuevo Usuario</h1>
</div>
  <p><input type="text" placeholder="Email" v-model="email" class="input-field"/></p>
  <p><input type="password" placeholder="Password" v-model="password" class="input-field" /></p>
  <select name="LeaveType" @change="onChange($event)" class="form-control" v-model="key">
   <option value="1">Administrador</option>
   <option value="2">Empleado</option>
</select>
  <p><button @click="register" class="button-primary">Guardar</button></p>
  <p><button @click="signInWithGoogle" class="button-secondary">Iniciar con Google</button></p>
</div>
</template>

<script setup>
import { ref } from "vue";
import { getAuth, createUserWithEmailAndPassword,
  GoogleAuthProvider, signInWithPopup, } from "firebase/auth";
import { useRouter } from "vue-router";
const email = ref("");
const password = ref("");
const rol = ref("");
const router = useRouter();

const register = () => {
  createUserWithEmailAndPassword(getAuth(), email.value, password.value, rol.value)
    .then((data) => {
      console.log("Registrado exitosamente");
    })
    .catch((error) => {
      console.log(error.code);
      alert(error.message);
    });
};

const signInWithGoogle = () => {
  const provider = new GoogleAuthProvider();
  signInWithPopup(getAuth(), provider)
  .then((result) => {
    console.log(result.user);
    router.push("/feed");
  })
  .catch((error) => {

  });
};
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
  margin-top:20px;
  margin-bottom: 100px;
}

.input-field {
  width: 300px; /* Ajusta el ancho según tus preferencias */
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
}

.decoration-line {
  height: 40px; /* Grosor de la línea */
  width: 100%; /* Ancho completo */
  background-color: #093b59; /* Color azul */
}
.button-primary, .button-secondary {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.button-primary {
  background-color: #6FB84B;
  color: #fff;
}

.button-primary:hover {
  background-color: #5a9e3f;
}

.button-secondary {
  background-color: #093b59; /* Color del botón secundario */
  color: #fff;
}

.button-secondary:hover {
  background-color: #07283e; /* Color del botón secundario al pasar el ratón */
}

.form-control {
  width: 300px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
  appearance: none; /* Oculta la apariencia del select nativo */
  background: transparent url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'><path fill='%2377799e' d='M10 12L6 8h8l-4 4z'/></svg>") no-repeat right 10px center;
  /* Agrega un icono personalizado al select */
}
</style>