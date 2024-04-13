<template>
  <h1>Crear Nuevo Usuario</h1>
  <p><input type="text" placeholder="Email" v-model="email" /></p>
  <p><input type="password" placeholder="Password" v-model="password" /></p>
  <select name="LeaveType" @change="onChange($event)" class="form-control" v-model="key">
   <option value="1">Administrador</option>
   <option value="2">Empleado</option>
</select>
  <p><button @click="register">Guardar</button></p>
  <p><button @click="signInWithGoogle">Iniciar con Google</button></p>
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
