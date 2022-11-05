import Vue from 'vue';
import VueRouter from 'vue-router';

// import Home from '@/views/Home.vue';
import Devices from '@/views/Devices.vue';

Vue.use(VueRouter);

const routes = [
  // {
  //   path: '/',
  //   name: "Home",
  //   component: Home,
  // },
  {
    path: '/devices',
    name: "Devices",
    component: Devices,
  },
  // {
  //   path: '/detectors',
  //   name: "Setups",
  //   component: Home,
  // },
  // {
  //   path: '/setups',
  //   name: "Setups",
  //   component: Home,
  // },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;