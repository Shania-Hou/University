<template>
    <div class="menu">
        <div class="container1">
            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal"  @select="handleSelect">
                <el-submenu index="1">
                    <template slot="title" >大学</template>
                    <el-menu-item index="1-1" >大学排名</el-menu-item>
                    <el-menu-item index="1-2" >查大学</el-menu-item>
                        
                </el-submenu>
                <el-submenu index="2">
                    <template slot="title">专业</template>
                    <el-menu-item index="2-1">专业排名</el-menu-item>
                    <el-menu-item index="2-2">查专业</el-menu-item>
                </el-submenu>
                <el-submenu index='3'>
                    <template slot="title" >推荐</template>
                    <el-menu-item index="3-1">推荐大学</el-menu-item>

                </el-submenu>
            </el-menu>
        </div>   
    </div>
</template>
<script>
import {getCookie} from '../assets/js/cookie'
export default {
    name:'nav-header2',
    data(){
        return{
            activeIndex: '1',
            activeIndex2: '1'
        }
    },
    methods: {
        //功能界面
        handleSelect(key,keyPath) {
            if(getCookie('username')){
                switch(key){
                    case "1-1":
                        this.$router.push('/university-list');
                        break;
                    case "1-2":
                        this.$router.push('/university');
                        break;
                    case "2-1":
                        this.$router.push('/speciality-list');
                        break;
                    case "2-2":
                        this.$router.push('/speciality');
                        break;
                    case "3-1":
                        this.$router.push('/tuijian');
                        break;
                }
            }else{
                alert('您还未登录，请先登录！')
                setTimeout(this.$router.push('/login'))
            }
            
        }
    }
}
</script>