<template>
    <div class="navbar">
        <div class="main_container">
            <p class="navbar__logo" v-on:click="$router.push('/')">Musicurses</p>
            <div class="navbar__menu">
                <router-link class="navbar__link" to="account"><span class="fa fa-user-circle-o"></span></router-link>
                <router-link class="navbar__link" to="learning">Учиться</router-link>
                <router-link class="navbar__link" to="search">Поиск</router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Gochi+Hand&display=swap');
.navbar{
    position: sticky;
    top: 0;
    width: 100%;
    height: 70px;
    display: flex;
    justify-content: center;
    border-bottom: 2px solid rgb(211, 211, 211);
    background-color: #242424;
    box-shadow: 0px 1px 5px 1px rgba(240, 240, 240, 0.5);
    }
/* Main declare in App.vue */
.main_container{
    align-items: center;
    justify-content: space-between;
}

.navbar__logo{
    color: rgb(211, 211, 211);
    font-size: 35px;
    font-family: 'Gochi Hand', cursive;
}
.navbar__logo:hover{
    cursor: pointer;
}


.navbar__menu{
    display: flex;
    flex-direction: row-reverse;
}
.navbar__link{
    padding-left: 20px;
}
</style>