<script setup>
import App from "@/App.vue";
</script>

<template>
  <div class="container">
    <div class="component-logo">
      <router-link class="navbar-brand" to="/"> <img src="@/assets/portaLogo.png"
      alt="" 
      width="200" 
      height="200" />
    </router-link> 
    </div>
    <h1>Bienvendo</h1>
    <br />
    <div class="card mb-3">
      <div class="form-details">
        <div class="mb-3">
          <label for="" class="form-label">E-mail</label>
          <input
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
            type="password"
            class="form-control"
            name=""
            id="idPassword"
            placeholder="**********"
          />
            <h5> <router-link class="password-forgotten" to="/"> ¿Olvidaste la contraseña? </router-link> </h5>
        </div>
      </div>
      <button type="button" class="btn btn-success" id="Access">Aceptar</button>
      <br>
      <h3>¿No tienes cuenta aún? <router-link class="register" to="/"> Registrate</router-link> con nosotros </h3>
    </div>
    
  </div>
</template>

<style scoped>
.container {
  min-height: 100%;
  margin-bottom: auto;
}

.component-logo {
  min-height: 0vh;
  align-items: center;
}

.form-control {
  width: 50rem;
  padding: 0.375rem 1rem;
}

.password-forgotten {
  color: #70b94b;
}

.register{
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
