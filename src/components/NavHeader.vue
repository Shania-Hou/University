<template>
    <div class='nav-header'>
        <div class='container1'>
            <div class="nav-menu">
                <span>University</span>
                <img src="../icon/对勾.png">
            </div>
            <div class="user" style="width:75px;margin-right:0">
                <router-link to="/login" v-if="showLoginPage"><span style="font-size:13px;color:white">点击登陆</span></router-link>
                <el-dropdown v-if="showLogined" style="width:75px;"> 
                    <el-button type="primary" style="background-color:#41b883;border:0 solid;width:75px">
                        <!-- 个人信息显示 -->
                        <span style="font-size:13px;color:#ebebeb">{{username}}</span>
                        <i class="el-icon-arrow-down el-icon--right"></i>
                    </el-button>

                    <el-dropdown-menu slot="dropdown" >
                        <el-dropdown-item>
                            <router-link to="/user_self" style="font-size:13px;color:#41b883;">个人信息</router-link>
                        </el-dropdown-item>
                        <hr style="width:80%;height:1px;border:none;border-top:1px solid;color:#dbdada">
                        <el-dropdown-item style="font-size:13px;color:#41b883" @click.native="exit_self">退出登陆</el-dropdown-item>
                    </el-dropdown-menu>
                </el-dropdown>
            </div>
        </div>    
    </div>
</template>

<script>
import {setCookie,getCookie, delCookie} from '../assets/js/cookie'
export default {
    name:'nav-header',
    data(){
        return {
            username:getCookie('username'),
            showLoginPage:'',
            showLogined:'',
            

      };
    },
    mounted(){
        /*页面挂载获取cookie，如果存在username的cookie，则跳转到主页，不需登录*/
        if(getCookie('username')){
            this.showLoginPage = false
            this.showLogined = true
        }else{
            this.showLoginPage = true
            this.showLogined = false
        }
        

    },
    methods: {
        
        //退出登陆
        exit_self(){
            delCookie('username',this.username)
            // this.reload()
            // this.$router.go(0);
            this.$router.push('/index')
        },

    }
}
</script>
<style lang="scss">
    @import '../assets/scss/config.scss';
    @import '../assets/scss/mixin.scss';
    @import '../assets/scss/reset.scss';
    .nav-header{
        height:75px;
        line-height: 75px;
        background-color: #41b883;
        .container1{
            @include flex();
            color:#fcf9f9;
            height:75px;
            img,span{
                display: inline-block;
                font-size:25px
            }
            .nav-menu{
                margin-left:20px;
                font-size:20px;
                height:75px;
            }
            a {
                color:#ebebeb
            }
            .router-link-active {
                color:#ebebeb
            }
            
        }
    } 
    .el-dropdown-link {
        cursor: pointer;
        color: #ebebeb;
    }
    .el-icon-arrow-down {   
        font-size: 12px;
    }
    
</style>