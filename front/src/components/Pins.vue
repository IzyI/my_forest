<template>
  <v-col
    cols="12"
    xl="4"
    lg="4"
    md="6"
    sm="8"
  >
    <v-card
      class="mx-auto"
      outlined
    >
      <v-list-item>
        <div class="w100">
          <div>{{ pin.name }}</div>
          <div class="d-flex">
            <v-switch
              v-model="status"
              color="green"
              label="Включить"
              hide-details="true"
            />
            <v-switch
              v-model="lock"
              color="red"
              label="Ручное управление"
              hide-details="true"
            />
          </div>
          <div class="d-flex justify-lg-space-between">
            <v-text-field
              v-model="time_on"
              label="Time on"
              color="red lighten-2"
              class="mr-2"
            />
            <v-text-field
              v-model="time_off"
              label="Time off"
              color="red lighten-2"
            />
          </div>
          <v-progress-linear
            color="red lighten-2"
            :indeterminate="$store.state.pinstore.isPinsLoading"
          />

          <div class=" row d-flex mt-3 ">
            <v-text-field
              v-model="days"
              label="Days"
              color="red lighten-2"
            />

            <v-btn
              color="red"
              icon
              size="large"
              class="ml-16 mr-12 mt-5"
              :disabled="status_button"
              @click="sendPins"
            >
              <v-icon dark>
                mdi-send
              </v-icon>
            </v-btn>
          </div>
        </div>
      </v-list-item>
    </v-card>
  </v-col>
</template>
<style scoped>

.hsfwwrt {
  font-size: 1.5em;
}

.v-selection-control .v-label {
  width: 0 !important;
  height: 0 !important;
}

.sdfr45 {
  flex: initial;
}

.w100 {
  width: 100%;
}
</style>
<script>

import axios from 'axios'
import info from '../info'
import { mapActions, mapMutations } from 'vuex'

export default {
  name: 'Pins',
  props: {
    pin: {
      type: Object,
      required: true
    }

  },
  data () {
    return {
      lock: 1,
      status: 1,
      time_on: '',
      time_off: '',
      days: '',
      status_button: false,
      name: ''
    }
  },
  watch: {
    pin: {
      immediate: true,
      deep: true,
      handler (val, oldVal) {
        console.log('watch PIN')
        this.lock = !!val.lock
        this.status = !!val.status
        var cron = val.cron.split('/')
        this.time_on = cron[0]
        this.time_off = cron[1]
        this.days = cron[2]
        this.name = val.name
      }
    }
  },
  methods: {
    ...mapMutations({
      setLoading: 'pinstore/setLoading'
    }),
    ...mapActions({
      simpleGetPins: 'pinstore/simpleGetPins'
    }),
    async sendPins () {
      this.status_button = true
      this.setLoading(true)
      var data = {
        name: this.name,
        status: this.status | 0,
        cron: this.time_on + '/' + this.time_off + '/' + this.days,
        lock: this.lock | 0
      }
      try {
        const response = await axios.put(info.pinserver + '/status', data, {
          auth: {
            username: info.pinuser,
            password: info.pinpassword
          }
        })
        if (response.data.result) {
          this.simpleGetPins()
        } else {
          alert(response.data)
        }
      } catch (e) {
        console.log(e)
        alert('Error: ' + e)
      } finally {
        this.setLoading(false)
        this.status_button = false
      }
    }
  }

}
</script>
