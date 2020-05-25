<template>
<div>
    <nav-header></nav-header>
    <div class="container" style="margin-top:16px;margin-bottom:10px !important">
        <el-page-header @back="goBack" title="首页" content="个人信息">
        </el-page-header>
        <el-divider></el-divider>
        <!-- 头像 -->
        <div class="showInfo">
            <table >
                <tr>
                    <td><span>用户名：</span></td>
                    <td>
                        <el-input v-model="userData[0].username" class="self-info" disabled v-show="cannotWrite1"></el-input>
                        <el-input v-model="userData[0].username" class="self-info" id="username" v-show="canWrite1" 
                            
                            ref="uname"></el-input>
                    </td>
                    <td>
                        <i class="el-icon-edit el-input__icon"
                            slot="suffix"
                            @click="handleIconClick1">
                        </i>
                    </td>
                </tr>
                <tr>
                    <td><span>密码:</span></td>
                    <td>
                        <el-input v-model="userData[0].password" class="self-info" disabled v-show="cannotWrite2" show-password></el-input>
                        <el-input v-model="userData[0].password" class="self-info" v-show="canWrite2"  show-password
                            
                            ref="psd"></el-input>
                    </td>
                    <td>
                        <i class="el-icon-edit el-input__icon"
                            slot="suffix"
                            @click="handleIconClick2">
                        </i>
                    </td>
                </tr>
                <tr>
                    <td><span>年龄：</span></td>
                    <td>
                        <el-input v-model="userData[0].age" class="self-info" disabled v-show="cannotWrite3"></el-input>
                        <el-input v-model="userData[0].age" class="self-info" id="username" v-show="canWrite3" 
                            
                            ref="age"></el-input>
                    </td>
                    <td>
                        <i class="el-icon-edit el-input__icon"
                            slot="suffix"
                            @click="handleIconClick3">
                        </i>
                    </td>
                </tr>
                <tr>
                    <td><span>年级：</span></td>
                    <td>
                        <el-input v-model="userData[0].grade" class="self-info" disabled v-show="cannotWrite4"></el-input>
                        <el-input v-model="userData[0].grade" class="self-info" id="username" v-show="canWrite4" 
                            
                            ref="grade"></el-input>
                    </td>
                    <td>
                        <i class="el-icon-edit el-input__icon"
                            slot="suffix"
                            @click="handleIconClick4">
                        </i>
                    </td>
                </tr>
                <tr>
                    <td><span>省份：</span></td>
                    <td>
                        <el-input v-model="userData[0].username" class="self-info" disabled v-show="cannotWrite5"></el-input>
                        <el-input v-model="userData[0].username" class="self-info" id="username" v-show="canWrite5" 
                            
                            ref="u_pro"></el-input>
                    </td>
                    <td>
                        <i class="el-icon-edit el-input__icon"
                            slot="suffix"
                            @click="handleIconClick5">
                        </i>
                    </td>
                </tr>
                <tr>
                    <td><span>学科类别</span></td>
                    <td >
                        <template >
                            <el-radio v-model="radio" label="1">文科</el-radio>
                            <el-radio v-model="radio" label="2">理科</el-radio>
                        </template>
                    </td>
                </tr>
            </table>
            <el-button type="success" icon="el-icon-check" circle style="display:table;margin:0 auto"
            @click="submit"></el-button>

            
        </div>
    </div>
</div>

</template>
<script>
    import axios from 'axios'
    import {setCookie,getCookie} from '../assets/js/cookie';
    import NavHeader from '../components/NavHeader';
export default {
    
    name:'user_self',
    data(){
        return{
            radio: '1',
            url: '',
            fileList:[0],
            uploadFile:[],
            userData:[{
                username:'柯南',
                password:123,
                age:18,
                u_pro:'山西',
                u_type:'理科',
                email:'kenan@163.com'
            }],
            // userData:['柯南',123,12,'山西','文科','hsn@163.com'],
            cannotWrite1:true,
            canWrite1:false,
            cannotWrite2:true,
            canWrite2:false,
            cannotWrite3:true,
            canWrite3:false,
            cannotWrite4:true,
            canWrite4:false,
            cannotWrite5:true,
            canWrite5:false,
            cannotWrite6:true,
            canWrite6:false,
        
        }
    },
    created(){
        var username1 = getCookie('username')
        console.log(username1)
    },
    components: {
        'nav-header':NavHeader
    },
    methods:{
        goBack(){
            this.$router.push('/index')
        },
        handleIconClick1(){
            this.cannotWrite1 = false;
            this.canWrite1 = true;
        },
        handleIconClick2(){
            this.cannotWrite2 = false;
            this.canWrite2 = true;
        },
        handleIconClick3(){
            this.cannotWrite3 = false;
            this.canWrite3 = true;
        },
        handleIconClick4(){
            this.cannotWrite4 = false;
            this.canWrite4 = true;
        },
        handleIconClick5(){
            this.cannotWrite5 = false;
            this.canWrite5 = true;
        },
        handleIconClick6(){
            this.cannotWrite6 = false;
            this.canWrite6 = true;
        },
        submit(){
            
        }
        
        
    }
}
</script>
<style lang="scss">
    @import '../assets/scss/reset.scss';
    .self-info{
        // width:100px;
    }
    .showInfo{
        // width: 280px;
        display: table;
        margin:0 auto;
        span{
            font-size:14px;
        }
    }
    table{
        // width:280px;
        // border:1px solid blue;

    }
    td{
        height:50px;
        margin:0 0 10px 0;
    }
</style>