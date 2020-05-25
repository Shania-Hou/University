<template>
<!-- 展示全部大学  可通过省份条件来获取相应信息 -->
    <div class="container">
        <router-view></router-view>
        <!-- 城市选择 -->
        <div style="margin-top: 20px;font-size:16px;">
            <el-radio-group  size="small" class="el-group">
                <el-radio-button id="selectCity"
                    v-for="(item, index) in ['全部','北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江',
                    '上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西',
                    '海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆','香港','澳门','台湾']" 
                    :key="index" 
                     @click.native.prevent="clickitem(item)"
                    :label="item">
                </el-radio-button>
                
            </el-radio-group>
        </div>
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
            :total="universityList.length">
        </el-pagination>
    </div>
    
</template>
<script>
    import NavHeader from '../components/NavHeader.vue'
    import axios from 'axios'
    import VueResource from 'vue-resource'
    export default {
        name:'university',
        components:{
            'nav-header':NavHeader
        },
        data(){
            return{
                currentPage:1,//初始页码
                pagesize:10,
                universityList: [],//当前页码表格数据
            }
        },
        created(){
            this.getUniversityList()
        },
        
        methods:{
            // 初始页currentPage、初始每页数据数pagesize和数据data
            handleSizeChange: function (size) {
                    this.pagesize = size;
                    console.log(this.pagesize)  //每页下拉显示数据
            },
            handleCurrentChange: function(currentPage){
                    this.currentPage = currentPage;
                    console.log(this.currentPage)  //点击第几页
            },
            getUniversityList() {
                var _this=this;
				this.$http.get('/api/user/university').then(function(res) {
					// console.log(res.data)
					this.$data.universityList = res.data
                })
            },
            clickitem(item){
                this.pro = item
                console.log(this.pro)
                if (this.pro === "全部") {
                    this.$http.get('/api/user/university').then(function(res) {
					    // console.log(res.data)
					    this.$data.universityList = res.data
                    })
                } else {
                    this.$http.get('/api/user/getUniversityByPro',{
                        params:{
                            pro:this.pro
                        }
                    }).then(function(res) {
                        // console.log(res.data)
                        this.$data.universityList = res.data
                    })
                }  
            },
            openUrl(url){
                // window.location.href="http://"+url;
                return "http://"+url
            }
        }
    }
</script>
<style lang="scss">
    @import '../assets/scss/reset.scss';
    .el-group{
        /deep/{
            #selectCity{
                margin:0px 4px 5px 0px !important;
                border:#41b883 1px solid !important;
                .el-radio-button__inner{
                    &:hover{
                        border-color:#2CCF2A !important;
                    }
                }
                
            }
            
        
        }
    }
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