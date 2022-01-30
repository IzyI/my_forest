import axios from 'axios'
import info from '../info'

export const pinStore = {

  state: {
    l: 'test',
    arrayPins: [],
    isPinsLoading: false
  },
  mutations: {
    setLoading (state, bool) {
      state.isPinsLoading = bool
    },
    setPins (state, posts) {
      state.arrayPins = posts
    }

  },

  actions: {
    async simpleGetPins (
      { state, commit }
    ) {
      try {
        const response = await axios.get(info.pinserver + '/status', {
          auth: {
            username: info.pinuser,
            password: info.pinpassword
          }
        })
        if (response.data.result) {
          commit('setPins', response.data.status)
        } else {
          console.log(response.data)
          alert(response.data)
        }
      } catch (e) {
        console.log(e)
        alert('Error: ' + e)
      }
    },
    async getPins (
      { state, commit }
    ) {
      try {
        commit('setLoading', true)
        const response = await axios.get(info.pinserver + '/status', {
          auth: {
            username: info.pinuser,
            password: info.pinpassword
          }
        })
        if (response.data.result) {
          commit('setPins', response.data.status)
        } else {
          console.log(response.data)
          alert(response.data)
        }
      } catch (e) {
        console.log(e)
        alert('Error: ' + e)
      } finally {
        commit('setLoading', false)
      }
    }
  },
  modules: {},
  getters: {
    getresArrayPins (state) {
      return state.arrayPins
    }
  },
  namespaced: true
}
