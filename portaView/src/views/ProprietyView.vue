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
.dashboard{
z-index: -1;
}

.content {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 0;
  margin-bottom: 0;
}
</style>