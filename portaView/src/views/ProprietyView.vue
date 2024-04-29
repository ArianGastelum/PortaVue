<template>
  <Dashboard/>
  <div class="content">
    <select name="Propiedades" id="propiedades">
      <option value="Todas">All</option>
      <option value="Terrenos">Terrenos</option>
      <option value="Comerciales">Comerciales</option>
      <option value="Viviendas">Viviendas</option>
    </select>

    <p><button @click="createPropriety" class="button-primary">Create</button></p>
  </div>
</template>
<script>
import { useRouter } from "vue-router";

import Dashboard from '../components/Menu.vue';
export default {
  name: "ProprietyView",
  components: {
    Dashboard,
  },
  setup() {
    const router = useRouter(); 

    const createPropriety = () => { 
      router.push("/bienesraices/create");
    };
  
    return { createPropriety}; 
  },
};
</script>
<style scoped>
.content {
  display: flex;
  flex-direction: row; /* Cambiado de column a row para alinear horizontalmente */
  align-items: center;
  justify-content: center; /* Agregado para centrar los elementos horizontalmente */
}

select {
  padding: 0.5rem;
  font-size: 1rem;
  margin-right: 1rem; /* Añadido margen derecho para separar el select del botón */
}

.button-primary {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 0.25rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-top: 1rem;
}

.button-primary:hover {
  background-color: #0056b3;
}
</style>