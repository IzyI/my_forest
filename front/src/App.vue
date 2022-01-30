<template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>

    <v-footer>
      <v-container>
        <v-row />
      </v-container>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  })
}
</script>
