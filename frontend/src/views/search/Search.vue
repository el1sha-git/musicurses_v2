<template>
    <div class="search">
        <div class="main_container">
            <div class="search_and_results">
                <div class="search_form">
                    <input v-on:input="search" v-model="search_input" id="search_input" class="search_form__input" type="text" placeholder="Search...">
                </div>
                <div class="search_results">
                    Результаты поиска
                </div>
                <div v-for="i in data" v-bind:key="i.id" class="song">
                    <span v-on:click="play(i.id, i.path)" class="fa fa-play-circle song_play_button_small"></span>
                    <p>{{ i.title }}</p>
                </div>
            </div>
            <div class="filters">
                <span class="filters__label">Фильтры</span>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    created() {
        this.get_data()
    },
    data() {
        return {
            data: undefined,
            search_input: ''
        }
    },
    methods: {
        async get_data(){
            await axios.get('http://localhost:8000/api/song/all_songs').then(res=>{
                this.data = res.data
            })
        },
        async search(){
            await axios.get('http://localhost:8000/api/search/get_similar?text='+this.search_input).then(res=>{
                console.log(res.data)
            })
        },
        play(id, path){
            this.$store.commit('change_song', { audio_id: id, url: path })
        }
    },
}
</script>

<style scoped>
.search{
    display: flex;
    justify-content: center;

}
.main_container{
    display: flex;
    flex-direction: row;
}

.search_and_results{
    width: 70%;
}

.search_form{
    margin-top: 20px;
    width: 100%;
    display: flex;

}
.search_form__input{
    width: 100%;
    height: 40px;
    margin: 5px;
    display: flex;
    background-image: url('../../assets/icons/search.png');
    background-position: 10px ;
    background-repeat: no-repeat;
    padding-left: 40px;

    border: 2px solid #21a179;
    outline: none;
    border-radius: 15px;  

    transition: .1s;

    font-size: 18px;
}
.search_form__input:focus{
    border: 2px solid #cd5334;
    box-shadow: 2px 2px 5px 0px #cd5334;
}


.song{
    width: 100%;
    height: 60px;
    margin-top: 15px;
    border: 2px solid #1c1c1c;
    transition: 150ms;
    display: flex;
    align-items: center;
}

.song:hover{
    border: 2px solid #21a179;
    cursor: pointer;
}
.song_play_button_small{
    height: 60px;
    width: 60px;
    padding-left: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 25px;
    transition: 150ms;
}
.song_play_button_small:hover{
    color: #cd5334;
    font-size: 30px;
}


.filters{
    display: flex;
    flex-grow: 1;
    margin-top: 20px;
    margin-left: 20px;
    padding-left: 20px;
    border: 2px solid #21a179;
    border-radius: 15px;
}
.filters__label{
    width: 100%;
    display: flex;
    align-items: center;
    height: 40px;
    font-size: 25px;

}
</style>