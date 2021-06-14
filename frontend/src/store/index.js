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
    },

    change_song(state, payload){
      state.audio_element.pause();
      state.audio_element.currentTime = 0;
      state.audio_element.src = state.backend_url + "/api/song?path=" + payload.url;
      state.audio_id = payload.audio_id
      state.audio_element.play()
      state.audio_status = true
    }
  },
  actions: {
  },
  modules: {
  }
})
