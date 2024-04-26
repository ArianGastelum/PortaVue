<template>

    <head>
        <title>PORTA Soluciones Inmobiliarias</title>
    </head>

    <body>
        <div class="logo">
            <img src="@/assets/portaLogo.png" alt="Porta Logo" width="100" height="100" />
        </div>

        <div class="container">
            <div class="menu">
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

            </div>
            <div class="content">
                <div class="Construccion">
                    <h1 class="texto-Construccion">Sitio Web En Construcción</h1>
                    <img src="https://w7.pngwing.com/pngs/82/473/png-transparent-building-site-construction-crane-under-website-builder-site-whcompare-isometric-web-hosting-servers-icon-thumbnail.png"
                        alt="Sitio web en contruccion">
                        <h3>¡Estamos trabajando en este sitio para mejorar tu experiencia!</h3>
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

const enterPropriety = () => {
    router.push("/bienesraices")
}

const enterContructionSite = () => {
    router.push("/contruccion")
}
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
    margin: 0;
    /* Elimina el margen entre los elementos li */
}

.menu-items :hover {
    background-color: #093b59;
    /* Blue */
}

.menu-items li:hover {
    color: #4caf50;
    /* Green */
}

.texto-bienvenida {
    color: #093b59;
}

.nombre-usuario {
    color: #4caf50;
}
.content{
    margin-top: 200px;
    margin-left: 100px;
}

</style>