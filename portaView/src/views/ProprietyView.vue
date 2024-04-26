<template>
  <Dashboard class="dashboard">
  <div>
    <select name="Propiedades" id="propiedades">
      <option value="Todas">All</option>
      <option value="Terrenos">Terrenos</option>
      <option value="Comerciales">Comerciales</option>
      <option value="Viviendas">Viviendas</option>
    </select>

    <p><button @click="createPropriety" class="button-primary">Create</button></p>
  </div>
  </Dashboard>
</template>

<script>
import Dashboard from '../components/Menu.vue';
export default {
  name: "ProprietyView",
  components: {
    Dashboard,
  },
  setup(){
    const createPropriety = () => { 
      router.push("/bienesraices/create");
    };
  }
}
</script>
<style scoped>
  .button-primary{
    display:flex ;
    flex-direction: column;
    text-align: center;
    margin-left: 500px;
    margin-top: 500px;
  }
</style>