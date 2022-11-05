<template>
  <header>
    <nav class="navbar navbar-expand-md navbar-dark bg-dark">
      <div class="container">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul class="navbar-nav me-auto mb-2 mb-md-0">
            <li class="nav-item">
              <router-link class="nav-link" to="/devices">Devices</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/detectors">Detectors</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/setups">Setups</router-link>
            </li>

          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'NavBar',
  computed: {
    isLoggedIn: function() {
      return true;
    }
  },
  methods: {
    async logout () {
      await this.$store.dispatch('logOut');
      this.$router.push('/login');
    }
  },
}
</script>

<style scoped>
a {
  cursor: pointer;
}
</style>
