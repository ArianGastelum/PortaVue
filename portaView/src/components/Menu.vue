<template>
  <div class="logo">
    <img src="@/assets/portaLogo.png" alt="Porta Logo" width="100" height="100" />
  </div>
  <nav class="menu">
    <ul class="menu-items">
      <li><base-button @click="handleHome">Home</base-button></li>
      <li><base-button @click="enterContructionSite">Avalúos</base-button></li>
      <li><base-button @click="enterPropriety">Bienes Raíces</base-button></li>
      <li><base-button @click="enterContructionSite">Créditos Hipotecarios</base-button></li>
      <li><base-button @click="enterContructionSite">Construcciones</base-button></li>
      <li><base-button @click="enterContructionSite">Marketing</base-button></li>
      <li><base-button @click="enterContructionSite">Jurídico/Legal</base-button></li>
      <li><base-button @click="enterContructionSite">Inversiones</base-button></li>
      <li><base-button @click="enterContructionSite">Intranet</base-button></li>
      <li><base-button @click="enterContructionSite">Administración</base-button></li>
      <li v-if="isLoggedIn"><base-button @click="handleSignOut">Cerrar sesión</base-button></li>
    </ul>
  </nav>
</template>


<script>
import { ref } from "vue";
import { onMounted } from "vue";
import { getAuth, onAuthStateChanged, signOut } from "firebase/auth";
import { useRouter } from "vue-router";

export default {
  name: "Menu",
  setup() {
    const router = useRouter();
    const isLoggedIn = ref(false);
    let auth = null; 

    onMounted(() => {
      auth = getAuth();
      onAuthStateChanged(auth, (user) => {
        isLoggedIn.value = !!user; 
      });
    });

    const handleSignOut = () => {
      signOut(auth).then(() => {
        router.push("/");
      });
    };

    const enterPropriety = () => { 
      router.push("/bienesraices");
    };

    const handleHome = () => { 
      router.push("/home");
    };

    const enterContructionSite = () => {
    router.push("/contruccion");
    };
  
    return { isLoggedIn, handleSignOut, enterPropriety, handleHome, enterContructionSite }; 
  },
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