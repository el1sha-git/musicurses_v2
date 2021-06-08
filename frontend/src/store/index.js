import { createStore } from 'vuex'

export default createStore({
  state: {
    backend_url: 'http://localhost:8000',
    // Audio information
    audio_id: undefined,
    audio_src: undefined,
    audio_current_time: 0,
    // Playing status 
    audio_status: false,
    audio_element: undefined,

  },
  mutations: {
    create_player(state, player){
      state.audio_element = player
    },
    change_audio_state(state, status){
      state.audio_status = status
    }
  },
  actions: {
  },
  modules: {
  }
})
