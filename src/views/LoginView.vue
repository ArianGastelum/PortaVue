<template>
  <div class="container">
    <div class="component-logo">
      <router-link class="navbar-brand" to="/">
        <img src="@/assets/portaLogo.png" alt="" width="200" height="200" />
      </router-link>
    </div>
    <h1>Bienvenido</h1>
    <br />
    <div class="card mb-3">
      <div class="form-details">
        <div class="mb-3">
          <label for="" class="form-label">E-mail</label>
          <input
            v-model="email"
            type="email"
            class="form-control"
            name=""
            id="idEmail"
            placeholder="ejemplo123@portasi.com"
          />
        </div>
        <div class="mb-3">
          <label for="" class="form-label">Contraseña</label>
          <input
            v-model="password"
            type="password"
            class="form-control"
            name=""
            id="idPassword"
            placeholder="**********"
          />
          <h5>
            <router-link class="password-forgotten" to="/">
              ¿Olvidaste la contraseña?
            </router-link>
          </h5>
        </div>
      </div>
      <!-- <router-link id="Access" class="btn btn-outline-primary" to="/home">Aceptar</router-link> -->
      <p v-if="errMsg">{{ errMsg }}</p>
      <p><button id="Access" @click="register">Aceptar</button></p>
      <p>
        <button id="Access" @click="signInWithGoogle">
          Iniciar con Google
        </button>
      </p>
      <br />
      <h3>
        ¿No tienes cuenta aún?
        <router-link class="register" to="/register"> Registrate</router-link>
        con nosotros
      </h3>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import {
  getAuth,
  signInWithEmailAndPassword,
  GoogleAuthProvider,
  signInWithPopup,
} from "firebase/auth";
import { useRouter } from "vue-router";
const email = ref("");
const password = ref("");
const errMsg = ref();
const router = useRouter();

const register = () => {
  signInWithEmailAndPassword(getAuth(), email.value, password.value)
    .then((data) => {
      console.log("Registrado exitosamente");
    })
    .catch((error) => {
      console.log(error.code);
      switch (error.code) {
        case "auth/invalid-email":
          errMsg.value = "Invalid email";
          break;
        case "auth/user-not-found":
          errMsg.value = "No account with that email was found";
        case "auth/invalid-email":
          errMsg.value = "Invalid email";
        case "auth/wrong-password":
          errMsg.value = "Incorrect password";
        default:
          errMsg.value = "Email or password was incorrect";
          break;
      }
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
    .catch((error) => {});
};
</script>

<style scoped>
.container {
  min-height: 100%;
  margin-bottom: auto;
  text-align: center;
}

.component-logo {
  min-height: 0vh;
  align-items: center;
}

.form-control {
  padding: 0.375rem 1rem;
  width: 400;
}

.password-forgotten {
  color: #70b94b;
}

.register {
  color: #70b94b;
}

#Access {
  margin: auto;
  width: 400px;
  border-radius: 1rem;
  background-color: #70b94b;
  color: white;
}
</style>
