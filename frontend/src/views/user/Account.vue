<template>
    <div class="account">
        <div class="main_container">
            <div class="account__card left_card">
                <div class="account_avatar">
                    <img src="../../assets/no-profile-pics.jpg" alt="">
                </div>
                <div class="account__info">
                    <p class="account__name">{{ user.surname }} {{ user.name }}</p>
                    <p class="account__email">{{ user.email }}</p>
                    <p class="account__birth_date">Дата рождения: {{ user.birth_date }}</p>
                    <p class="account__phone_number">Номер телефона: +{{ user.phone_number }}</p>
                </div>
            </div>
            <div class="account__card right_card">
                <div class="account__tabs">
                    <div class="account__tab stats">Статистика</div>
                    <div class="account__tab liked_songs">Сохраненные песни</div>
                    <div class="account__tab liked_files">Сохраненные файлы</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    created() {
        this.get_user_data()
    },
    data() {
        return {
            user: ''
        }
    },
    methods: {
        async get_user_data(){
            await axios({
                method: 'get',
                url: `${this.$store.state.backend_url}/api/user`,
                headers:{
                    "accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": "Bearer "+localStorage.getItem("token")
                },
            }).then(response => {
                this.user = response.data
                console.log(response.data)
            }).catch(error => {
                    if (error.response.status == 401){
                        this.$router.push('/login')
                    }
            });
        }
    },
}
</script>

<style scoped>
.account{
    display: flex;
    justify-content: center;
    margin-top: 50px;
}
.main_container{
    display: flex;
    justify-content: space-between;
}
.account__card{
    background-color: #0c0c0c;
    height: 70vh;
    border-radius: 5px;
}
.left_card{
    display: flex;
    flex-direction: column;
    width:20%
}
.right_card{
    width: 75%;
}
/* Account info */
.account_avatar{
    width: 100%;
    padding-top: 30px;
    display: flex;
    justify-content: center;
}

.account_avatar img{
    width: 70%;
    border-radius: 50%;
    border: 2px solid #21A179;
    box-shadow: -2px 2px 10px 1px #21A179;
    transition: .15s;
}
.account_avatar img:hover{
    box-shadow: 2px 2px 15px 1px #21A179;
}

.account__info{
    margin-top: 10px;
    padding-left: 20px;
    font-size: 18px;
}
.account__info p{
    margin-top: 5px;
}
.account__name{
    font-size: 25px;
}
.account__email{
    font-size: 15px;
    color: #acacac;
}

/* Rigth side info  */
.account__tabs{
    width: 100%;
    height: 50px;
    border-bottom: 1px solid #acacac;
    display: flex;
}

.account__tab{
    padding: 0 20px 0 20px;
    display: flex;
    align-items: center;    
    transition: .26s;
}
.account__tab:first-child{
    border-radius: 5px 0px 0px 0px;
}

.account__tab::selection{
    color: inherit;
    background-color: inherit;
}
.account__tab:hover{
    background-color: #353535;
    cursor: pointer;

}
.account__phone_number{
    font-size: 16px;
}
</style>