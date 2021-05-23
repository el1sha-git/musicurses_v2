<template>
    <div class="audio_player">
        <div class="main_container">
            <div class="audio__controls">
                <span class="fa fa-backward"></span>
                <span v-if="!playing" class="fa fa-play" v-on:click="play"></span>
                <span v-else class="fa fa-pause" v-on:click="play"></span>
                <span class="fa fa-forward"></span>
            </div>
            <div class="audio__avatar">
                <img src="../assets/song.png" alt="">
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
        this.audio_element = document.querySelector('audio');
        this.track = this.audio_context.createMediaElementSource(this.audio_element);
        this.track.connect(this.audio_context.destination);
 
    },
    data() {
        return {
            audio_context: window.AudioContext || window.webkitAudioContext,
            audio_element: undefined,
            gain: null,
            track: undefined,
            playing: false
        }
    },
    methods: {
        play(){

            if (this.audio_context.state === 'suspended') {
                this.audio_context.resume();
            }

            if (this.playing === false){
                this.audio_element.play()
                this.playing = true
            }else{
                this.audio_element.pause()
                this.playing = false
            }
        },
        change_volume(){
            const gainNode = this.audio_context.createGain();
            this.track.connect(gainNode).connect(this.audio_context.destination);
            const volumeControl = document.querySelector('#volume');
            this.gain.gain.value = volumeControl.value;
        }
        
    },
}
</script>


<style scoped>
.audio_player{
    height: 70px;
    width: 100%;
    border-top: 2px solid white;
    position: fixed;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

.main_container{
    display: flex;
    align-items: center;
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