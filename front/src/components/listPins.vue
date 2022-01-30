<template>
  <v-container>
    <v-row class="justify-lg-start justify-md-start justify-sm-center">
      <pins
        v-for="pin in getresArrayPins"
        :pin="pin"
        :key="pin.name"
      />
    </v-row>
  </v-container>
</template>

<style scoped>

</style>
<script>

import pins from '../components/Pins.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ListPins',
  components: {
    pins
  },
  methods: {
    ...mapActions({
      getPins: 'pinstore/getPins'
    })
  },
  computed: {
    ...mapGetters({
      getresArrayPins: 'pinstore/getresArrayPins'
    })
  },
  mounted () {
    this.getPins()
  }
}

</script>
