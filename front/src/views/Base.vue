<template>
  <div>
    <v-container>
      <v-row class="text-center">
        <v-col cols="12">
          <h1 class="display-2 font-weight-bold mb-3 hsfwwrt">
            <div>Блок управления</div>
          </h1>
        </v-col>
      </v-row>
    </v-container>
    <listPins/>
  </div>
</template>

<script>
import listPins from '../components/listPins.vue'

export default {
  name: 'Base',

  components: {
    listPins
  }
}
</script>
