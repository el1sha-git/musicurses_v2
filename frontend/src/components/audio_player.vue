<template>
    <div class="audio_player">
        <div class="main_container">
            <div class="audio__controls">
                <span class="fa fa-backward"></span>
                <span class="fa fa-play"></span>
                <span class="fa fa-forward"></span>
            </div>
            <div class="audio__avatar">
                <img src="../assets/song.png" alt="">
            </div>
            <div class="audio__song_title">
                <p class="audio__song_name">Won't Run Away</p>
                <p class="audio__song_authors">Klass</p>
            </div>
        </div>
    </div>
</template>

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
</style>