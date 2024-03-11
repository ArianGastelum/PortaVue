<script setup>
import App from "@/App.vue";
</script>

<template>
  <div class="container">
    <router-link class="navbar-brand" to="/">
      <img
        src="@/assets/portaLogo.png"
        alt=""
        width="200"
        height="200"
        class="d-inline-block align-text-top"
      />
    </router-link>
    <h1>Bienvendo</h1>

    <div class="mb-3">
        <label for="" class="form-label">Email</label>
        <input
          type="email"
          class="form-control"
          name=""
          id=""
          aria-describedby="emailHelpId"
          placeholder="ejemplo123@portasi.com"
        />
      </div>
      <br>
      <div class="mb-3">
        <label for="" class="form-label">Password</label>
        <input
          type="password"
          class="form-control"
          name=""
          id=""
          placeholder="**********"
        />
      </div>
      <button type="button" class="btn btn-outline-success">Aceptar</button>
      <div class="d-grid gap-2">
      </div>
      
  </div>
      
</template>

<style>
.container {
  min-height: 100vh;
  position: static;
  align-items: center;
}
</style>
