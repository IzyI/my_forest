import { createStore } from 'vuex'
import { pinStore } from './pinStore'

export default createStore({
  modules: {
    pinstore: pinStore
  }
})
