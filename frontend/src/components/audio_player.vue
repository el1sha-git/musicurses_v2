<template>
    <div class="audio_player">
        <div class="progress_bar" v-on:click="force_update_time">
            <p class="time">{{ current_time_str }}</p>
            <div v-bind:style="{width: progress_bar_width + 'px'}" class="progress_now"></div>
        </div>
        <audio v-bind:ontimeupdate="current_time_update" 
        src="http://localhost:8000/api/song/song"
        >
        </audio>
        <div class="main_container">
            <div class="audio__controls">
                <span class="fa fa-backward"></span>
                <span id="play" v-if="!$store.state.audio_status" class="fa fa-play" v-on:click="play"></span>
                <span v-else class="fa fa-pause" v-on:click="play"></span>
                <span class="fa fa-forward"></span>
            </div>
            <div class="audio__avatar">
                <img src="" alt="">
            </div>
            <div class="audio__title_events_wrapper">
                <div class="audio__song_title">
                    <p class="audio__song_name">Won't Run Away</p>
                    <p class="audio__song_authors">Klass</p>
                </div>
                <div class="audio__actions">
                    <span class="fa fa-heart"></span>
                    <span class="fa fa-list"></span>
                    <span class="fa fa-volume-up">
                    </span>                    
                </div>
            </div>

        </div>
    </div>
</template>


<script>
export default {
    created() {
        
    },
    mounted() {
        let player = document.querySelector('audio')
        this.$store.commit('create_player', player)
        this.audio_element = player;
    },
    data() {
        return {
            current_time: 0,
            current_time_str: '',
            progress_bar_width: 0,
        }
    },
    methods: {
        
        play(){
            console.log(this.audio_element)
            if (this.$store.state.audio_status){
                this.audio_element.pause();
                this.$store.commit('change_audio_state', false)
            }else{
                // this.audio_element.play()
                this.$store.state.audio_element.play()
                this.audio_element.volume = 0.2
                this.$store.commit('change_audio_state', true)
            }
        },
        current_time_update(){
            // Упадет если будет больше часа!!!
            this.current_time = this.$store.state.audio_element.currentTime
            let minutes = Math.floor(this.current_time / 60) 
            
            if (minutes < 10){
                minutes = '0'+minutes
            }
            let seconds = this.current_time - 60 * minutes
            if (seconds < 10){
                seconds = '0'+seconds

            }
            this.current_time_str = minutes+":"+seconds.toString().split('.')[0]
            this.update_progress_bar()
        },
        update_progress_bar(){
            let duration = this.$store.state.audio_element.duration
            let current_time = this.$store.state.audio_element.currentTime
            let screen_width = window.screen.width
            this.progress_bar_width = current_time / duration * screen_width
        },
        force_update_time(){
            let mouse_x = window.event.offsetX
            let screen_width = window.screen.width
            let duration = this.$store.state.audio_element.duration 

            this.$store.state.audio_element.currentTime  = mouse_x / screen_width * duration

            this.progress_bar_width = mouse_x / screen_width * screen_width
        }
        
    },
    computed:{
        
    }
}
</script>


<style scoped>
.audio_player{
    height: 90px;
    width: 100%;
    position: fixed;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.progress_bar{
    width: 100%;
    background-color: #242424;
    border-bottom: 1px solid grey;
    height: 20px;
}
.progress_bar::selection{
    color: inherit;
    background-color: inherit;
}
.progress_bar:hover{
    cursor: pointer;
}
.time{
    position: absolute;
    z-index: 9999;
    height: 20px;
    display: flex;
    align-items: center;
    padding-left: 20px;
}
.progress_now{
    width: 50%;
    height: 20px;
    background-color: #cd5334;
    position: absolute;
    z-index: 8888;
    transition: .3s;
}


.main_container{
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    margin-top:10px;
}

.audio__avatar{
    height: 50px;
    margin-left: 10px;
}
.audio__avatar img{
    height: 100%;
}

.audio__controls span{
    padding: 0px 15px 0px 15px;
    font-size: 20px;
}
.audio__controls span:hover{
    color: #cd5334;
    cursor: pointer
}
.audio__title_events_wrapper{
    width: auto;
    display: flex;
    flex: 1;
    justify-content: space-between;
}
.audio__song_title{
    display: flex;
    flex-direction: column;
    margin-left: 15px;
}
.audio__song_name{
    font-size: 22px;
}
.audio__song_authors{
    font-size: 12px;
}
.audio__actions{
    display: flex;
    align-items: center;
}
.audio__actions span{
    padding: 0 0 0 15px;
}
.audio__actions span:hover{
    color:#cd5334;
    cursor: pointer;
}
.audio__actions .fa-heart{
    color: #81ae9d;
}
</style>