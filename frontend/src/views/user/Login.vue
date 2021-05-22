<template>
    <div class="login">
        <div class="login__card">
            <p class="login__title">Login</p>
            <div class="login__inputs">
                <input @keyup.enter="login" v-model="email" type="email" placeholder="E-mail">
                <input @keyup.enter="login" v-model='password' type="password" placeholder="Password">
            </div>
            <div class="login__button" v-on:click="login">
                <span class="login__text">Login</span>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            email: '',
            password: '',
        }
    },
    methods: {
        async login(){
            console.log(this.email, this.password)
            await axios({
                method: 'post',
                url: `${this.$store.state.backend_url}/auth/jwt/login`,
                headers:{
                    "accept": "application/json",
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                data: "username="+this.email+"&password="+this.password
            }).then(response => {
                localStorage.setItem("token", response.data.access_token)
                this.$router.push('/account')
            }).catch(error => {
                    return error.response
            });
        }
    },
}
</script>

<style scoped>

.login{
    width: 100%;
    display: flex;
    justify-content: center;
    position: absolute;
    top: 50%;
}
.login__card{
    height:400px;
    background-color: #161616;
    border:2px solid #21a179;
    width: 350px;
    transform: translateY(-50%);
    border-radius: 30px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    transition: .15s;
}
.login__card:hover{
    box-shadow: -10px 20px 40px 1px #2c2c2c;
}

.login__title{
    width: 100%;
    display: flex;
    justify-content: center;
    font-size: 30px;
}
.login__inputs{
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.login__inputs input{
    margin-top: 30px;
    outline: none;
    border: 0px;
    padding: 10px 5px 10px 15px;
    border-radius: 10px;
    /* border: 2px solid green */
}
.login__inputs input:focus{
    outline: 2px solid #21a179;
    /* border: 2px solid green; */
}
.login__button{
    width: 100%;
    border: 2px solid #21a179;
    bottom: 0;
    display: flex;
    height: 10px;
    align-items: center;
    justify-content: center;
    padding: 20px 0 20px 0;
    border-radius: 30px;
    transition: .45s;
    font-size: 20px;
}
.login__button:hover{
    background-color: white;
    color: #1c1c1c;
    border: 2px solid #21a179;
    cursor: pointer;
}
/* .login__text{
    visibility: hidden;
} */
</style>