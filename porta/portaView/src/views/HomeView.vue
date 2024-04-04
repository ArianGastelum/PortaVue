<template>
  <head>
    <title>PORTA Soluciones Inmobiliarias</title>
  </head>
  <body>
    <div class="logo">
      <img
        src="@/assets/portaLogo.png"
        alt="Porta Logo"
        width="100"
        height="100"
      />
    </div>

    <div class="container">
      <div class="menu">
        <ul class="menu-items">
          <li>Home</li>
          <li>Avalúos</li>
          <li>Bienes Raíces</li>
          <li>Créditos</li>
          <li>Construcciones</li>
          <li>Marketing</li>
          <li>Jurídico/Legal</li>
          <li>Inversiones</li>
          <li>Intranet</li>
          <li>Administración</li>
          <li> 
            <base-button @click="handleSignOut" v-if="isLoggedIn">Cerrar sesión</base-button>
          </li>
        </ul>
      </div>
      <div class="content">
        <div class="user-info">
          <h1 class="texto-bienvenida">Bienvenido</h1>
          <h1 class="nombre-usuario">Gerardo Ramírez</h1>
          <div>
            <span>Iniciaste sesión como: </span>
            <span style="font-weight: bold">Administrador</span>
          </div>
        </div>
      </div>
    </div>
  </body>
</template>
<script setup>
import { ref } from "vue";
import { onMounted } from "vue";
import { getAuth, onAuthStateChanged, signOut } from "firebase/auth";
import { useRouter } from "vue-router";

const router = useRouter();
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
const handleSignOut = () => {
  signOut(auth).then(() => {
    router.push("/");
  });
};
</script>

<style scoped>
.container {
  display: flex;
  height: 100vh;
  text-align: center;
}

.menu {
  width: 210px;
  height: 100%;
  background-color: #093b59;
  padding: 10px;
  position: fixed;
  left: 0;
}

.content {
  flex: 1;
  padding: 20px;
}

@media (max-width: 768px) {
  .menu {
    width: 100%;
    position: relative;
  }

  .content {
    margin-top: 80px;
  }
}

.menu ul {
  height: 100%;
}
.menu li {
  font-family: Arial, Helvetica, sans-serif;
  font-size: x-large;
  color: white;
  padding: 0px;
}

.logo {
  position: fixed;
  right: 0;
  margin-right: 10px;
  top: 10px;
}

.menu-items {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-self: center;
  text-align: left;
  height: auto;
  padding: 0;
  margin-left: 5px;
}

.menu-items li {
  height: 100%;
  display: block;
  padding: 10px;
  list-style-type: none;
  margin: 0; /* Elimina el margen entre los elementos li */
}

.menu-items :hover {
  background-color: #093b59; /* Blue */
}

.menu-items li:hover {
  color: #4caf50; /* Green */
}

.texto-bienvenida {
  color: #093b59;
}

.nombre-usuario {
  color: #4caf50;
}
</style>
