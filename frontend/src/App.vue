<template>
  <v-app>
    <v-main class="fill-background">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
<style>
html,
body,
#app {
  height: 100%;
  margin: 0;
}
</style>
