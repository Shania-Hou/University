<template>
        <!-- <nav-header></nav-header> -->
        <div class="container">
            <el-form :inline="true" :model="formInline" class="demo-form-inline" style="margin:30px 0 0 5%">
                <el-form-item label="考生省份" >
                    <el-select v-model="formInline.pro" placeholder="请选择省份">
                    <el-option label="北京" value="beijing"></el-option>
                    <el-option label="天津" value="tianjin"></el-option>
                    <el-option label="河北" value="hebei"></el-option>
                    <el-option label="山西" value="shanxi"></el-option>
                    <el-option label="内蒙古" value="neimenggu"></el-option>
                    <el-option label="辽宁" value="liaoning"></el-option>
                    <el-option label="吉林" value="jilin"></el-option>
                    <el-option label="黑龙江" value="heilongjiang"></el-option>
                    <el-option label="上海" value="shanghai"></el-option>
                    <el-option label="江苏" value="jiangsu"></el-option>
                    <el-option label="浙江" value="zhejiang"></el-option>
                    <el-option label="安徽" value="anhui"></el-option>
                    <el-option label="福建" value="fujian"></el-option>
                    <el-option label="江西" value="jiangxi"></el-option>
                    <el-option label="山东" value="shandong"></el-option>
                    <el-option label="河南" value="henan"></el-option>
                    <el-option label="河北" value="hebei"></el-option>
                    <el-option label="湖北" value="hubei"></el-option>
                    <el-option label="湖南" value="hunan"></el-option>
                    <el-option label="广东" value="guangdong"></el-option>
                    <el-option label="广西" value="guangxi"></el-option>
                    <el-option label="海南" value="hainan"></el-option>
                    <el-option label="重庆" value="chongqin"></el-option>
                    <el-option label="四川" value="sichuan"></el-option>
                    <el-option label="贵州" value="guizhou"></el-option>
                    <el-option label="云南" value="yunnan"></el-option>
                    <el-option label="西藏" value="xizang"></el-option>
                    <el-option label="陕西" value="shanxi"></el-option>
                    <el-option label="甘肃" value="gansu"></el-option>
                    <el-option label="青海" value="qinghai"></el-option>
                    <el-option label="宁夏" value="ningxia"></el-option>
                    <el-option label="新疆" value="xinjiang"></el-option>
                    <el-option label="澳门" value="aomen"></el-option>
                    <el-option label="香港" value="xianggang"></el-option>
                    <el-option label="台湾" value="taiwan"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="学科类别" >
                    <el-select v-model="formInline.type" placeholder="文/理科">
                    <el-option label="文科" value="文科"></el-option>
                    <el-option label="理科" value="理科"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="预估分数" >
                    <el-input v-model="formInline.score" placeholder="预估分数"></el-input>
                </el-form-item>
                
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">查询</el-button>
                </el-form-item>
                
            </el-form>
            <!-- 数据展示 -->
            <el-table  :data="universityList.slice((currentPage-1)*pagesize,currentPage*pagesize)" stripe >
                <el-table-column type="expand">
                    <template slot-scope="props">
                        <el-form label-position="left" inline class="table-expand">
                        <el-form-item label="主管部门">
                            <span>{{ props.row.u_administration }}</span>
                        </el-form-item>
                        <el-form-item label="985">
                            <span>{{ props.row.if985 }}</span>
                        </el-form-item>
                        <el-form-item label="211">
                            <span>{{ props.row.if211 }}</span>
                        </el-form-item>
                        <el-form-item label="学历">
                            <span>{{ props.row.u_level }}</span>
                        </el-form-item>
                        <el-form-item label="地址">
                            <span>{{ props.row.u_local }}</span>
                        </el-form-item>
                        <el-form-item label="招生电话">
                            <span>{{ props.row.u_phone }}</span>
                        </el-form-item>
                        <el-form-item label="招生网站">
                            <a class="openUrl" target="_blank" :href="openUrl(props.row.u_url)">{{ props.row.u_url }}</a>
                        </el-form-item>
                        </el-form>
                    </template>
                </el-table-column>
                <el-table-column
                    prop="u_name"
                    label="大学"
                    width="358"
                    >
                </el-table-column>
                <el-table-column
                    prop="u_pro"
                    label="所属省份"
                    width="358"
                    >
                </el-table-column>
                <el-table-column
                    prop="u_type"
                    label="院校类型"
                    width="358"
                    >
                </el-table-column>
            </el-table>
            <!-- 分页展示 -->
            <el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page.sync="currentPage"
                :page-size="10"
                layout="total, sizes, prev, pager, next, jumper"
                :total="universityList.length"
                v-if="ifshow">
            </el-pagination>
        </div>
    
    
</template>
<script>
import axios from 'axios'
import {setCookie,getCookie} from '../assets/js/cookie';
import NavHeader from '../components/NavHeader';
export default {
    name:'tuijian',
    components: {
        'nav-header':NavHeader
    },
    data(){
        return{
        formInline: {
            pro:'',
            type: '',
            score: '',
            ifshow:false
        },
        currentPage:1,//初始页码
        pagesize:10,
        universityList: [],//当前页码表格数据
    }
    },
    methods:{
        onSubmit(item) {
        var _self = this
        var data2={
            pro:this.formInline.pro,
            type:this.formInline.type,
            score:this.formInline.score
        }
        console.log(data2);
        this.$http.get('/api/user/tuijian',{
            params:{
                type:data2.type,
                score:data2.score
            }
        }).then(function(res) {
			console.log(res.data)
            this.$data.universityList = res.data
            this.ifshow=true
        })

      },
      // 初始页currentPage、初始每页数据数pagesize和数据data
        handleSizeChange: function (size) {
            this.pagesize = size;
            console.log(this.pagesize)  //每页下拉显示数据
        },
        handleCurrentChange: function(currentPage){
            this.currentPage = currentPage;
            console.log(this.currentPage)  //点击第几页
        },
        openUrl(url){
                return "http://"+url
            }
    }
    
}
</script>
<style lang="scss">
    @import '../assets/scss/reset.scss';
    .table-expand {
        font-size: 0;
    }
    .table-expand label {
        width: 90px;
        color: #99a9bf;
    }
    .table-expand .el-form-item {
        margin-right: 0;
        margin-bottom: 0;
        width: 50%;
    }
    .el-pagination{
        margin-top: 15px;
        margin-left:20%;
    }
    
    .openUrl{
        color:#3f3d3d
    }
    .openUrl:hover{
        color:#41b883;
    }
</style>