
<template>
    <div id='main'>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm"  class="demo-ruleForm">
        <div class="nav-menu">
            <span class="title">University</span>
            <img src="../icon/对勾2.png">
        </div>
        <div class="login-wrap" v-show="showLogin">
            <h1>登录</h1>
            <p v-show="showTishi">{{tishi}}</p>
            <el-input placeholder="请输入用户名" v-model="username" clearable></el-input>
            <el-input placeholder="请输入密码"  v-model="password" show-password></el-input>
            <p><el-button icon="el-icon-success" v-on:click="login">Login</el-button></p>
            <br>
            <span v-on:click="ToRegister" class="mySpan">没有账号？马上注册</span>
        </div>

        <div class="register-wrap" v-show="showRegister">
            <h1>注册</h1>
            <p v-show="showTishi">{{tishi}}</p>
            <el-input placeholder="请输入用户名" v-model="newUsername" clearable></el-input>
            <el-input placeholder="请输入密码"  v-model="newPassword" show-password></el-input>
            <el-input placeholder="请输入年龄"  v-model="newAge"></el-input>
            <el-input placeholder="请输入年级"  v-model="newGrade"></el-input>
            <el-input placeholder="请输入省份"  v-model="newPro"></el-input>
            <el-form-item  prop="buyerEmail" placeholder="请输入e-mail" required>
                <el-input v-model="ruleForm.buyerEmail"></el-input>
            </el-form-item>
            
            <!-- <el-input placeholder="请输入e-mail"  prop="buyerEmail"  v-model="newEmail"></el-input> -->
            <p><el-button icon="el-icon-success" v-on:click="register">Register</el-button></p>
            <br>
            <span v-on:click="ToLogin" class="mySpan">已有账号？马上登录</span>
        </div>
        </el-form>
    </div>

</template>
<script>
import {setCookie,getCookie} from '../assets/js/cookie'
export default{
    data(){
        var checkEmail = (rule, value, callback) => {
            const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/
            if (!value) {
              return callback(new Error('邮箱不能为空'))
            }
            setTimeout(() => {
              if (mailReg.test(value)) {
                callback()
              } else {
                callback(new Error('请输入正确的邮箱格式'))
              }
            }, 100)
        };
        
        return{
            showLogin: true,
            showRegister: false,
            showTishi: false,
            tishi: '',
            username: '',
            password: '',
            newUsername: '',
            newPassword: '',
            newAge:'',
            newGrade:'',
            ruleForm: {
                buyerEmail: 'hsn@163.com',
            },
            rules: {
                buyerEmail: [
                { validator: checkEmail, trigger: 'blur' }
                ],
            }
        }
    },
    mounted(){
  /*页面挂载获取cookie，如果存在username的cookie，则跳转到主页，不需登录*/
        if(getCookie('username')){
            this.$router.push('/index')
        }
    },
    methods:{
        login(){
            if(this.username == "" || this.password == ""){
                alert("请输入用户名或密码")
            }else{
                    let data = {'username':this.username,'password':this.password}
                    /*接口请求*/
                    this.$http.post('/api/user/checkUser',data).then((res)=>{
                        console.log(res)
                    /*接口的传值是(-1,该用户不存在),(0,密码错误)，同时还会检测管理员账号的值*/
                        if(res.data == -1){
                            this.tishi = "该用户不存在"
                            this.showTishi = true
                            setTimeout(function(){
                                this.showTishi = false
                            }.bind(this),1000)
                            
                        }else if(res.data == 0){
                            this.tishi = "密码输入错误"
                            this.showTishi = true
                            setTimeout(function(){
                                this.showTishi = false
                            }.bind(this),1000)
                        }else if(res.data == 'admin'){
                        /*路由跳转this.$router.push*/
                            this.$router.push('/main')
                        }else{
                            this.tishi = "登录成功"
                            this.showTishi = true
                            setCookie('username',this.username,1000*60)
                            setTimeout(function(){
                                this.$router.push('/index')
                            }.bind(this),1000)
                        }
                    })
                }
        },
        register(){
            if(this.newUsername == "" || this.newPassword == "" || this.newAge == "" || this.newGrade == ""){
                alert("请全部填写")
            }else{
                let data = {'username':this.newUsername,'password':this.newPassword,'age':Number(this.newAge),'grade':this.newGrade,'email':this.ruleForm.buyerEmail}
                this.$http.post('/api/user/addUser',data).then((res)=>{
                    console.log(res)
                    if(res.data == -1) {
                        this.tishi = "该账号已存在"
                        this.showTishi = true
                        setTimeout(function(){
                                this.showTishi = false
                        }.bind(this),1000)
                        this.username = ""
                        this.password = ""
                        this.grade = ""
                        this.age = ""
                        this.email = ""
                    }else{
                        this.tishi = "注册成功"
                        this.showTishi = true
                        setTimeout(function(){
                                this.showTishi = false
                        }.bind(this),1000)
                        this.username = ''
                        this.password = ''
                        this.grade = ''
                        this.age = ''
                        this.email = ""
                        /*注册成功之后再跳回登录页*/
                        setTimeout(function(){
                            this.showRegister = false
                            this.showLogin = true
                            this.showTishi = false
                        }.bind(this),1000)
                    }
                })
            }
        },
        ToRegister(){
            this.showRegister = true
            this.showLogin = false
        },
        ToLogin(){
            this.showRegister = false
            this.showLogin = true
        }
    }
        
       
}
</script>
<style>
    .el-input__inner{
        width: 300px;
    }
    .nav-menu{
        text-align: center;
        height: 120px;
    }
    #main{
        margin:3%;

    }
    .login-wrap,.register-wrap{
        text-align:center;
    }
    input{
        display:block; 
        width:250px; 
        height:40px; 
        line-height:40px; 
        margin:0 auto; 
        margin-bottom: 10px; 
        outline:none; 
        border:1px solid #888; 
        padding:10px; 
        box-sizing:border-box;
    }
    p{
        color:#41b883;
    }
    button{
        display:block; 
        width:300px; 
        height:40px; 
        line-height: 40px; 
        margin:0 auto; 
        border:none; 
        background-color:#41b883; 
        color:#fff; 
        font-size:16px; 
        margin-bottom:5px;
    }
    .mySpan{
        cursor:pointer;
        
    }
    .mySpan:hover{
        color:#41b883;
    }
    
    img{
        display: inline-block;
        font-size:25px
    }
    .title{
        margin-right: 20px;
        /* margin-bottom: 50px; */
        display: inline-block;
        font-size:30px;
        color:#41b883;
    }
    .el-form-item__error{
        width:100%;
        text-align:center;
    }
    
</style>