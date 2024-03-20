<template>
    <h1>Crear Nuevo Usuario</h1>
    <p> <input type="text" placeholder="Email" v-model="email"> </p>
    <p> <input type="password" placeholder="Password" v-model="password"> </p>
    <p> <button @click="register">Guardar</button></p>
    <p> <button @click="signInWithGoogle">Iniciar con Google</button></p>

    <component :is='"script"' >
        import { ref } from "vue";
        import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
        import { useRouter } from 'vue-router';
        const email = ref("");
        const password = ref("");
        const router = useRouter()

        const register = () => {
            createUserWithEmailAndPassword(getAuth(), email.value, password.value)
            .then((data) => {
                console.log("Registrado exitosamente");
            })
            .catch((error) => {
                console.log(error.code);
                alert(error.message);
            });
        };

        const signInWithGoogle = () => {

        }

    </component>
</template> 