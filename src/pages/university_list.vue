<template>
<!-- 大学排名 -->
    <div class="container">
        <router-view></router-view>
        <!-- 选择年份 -->
        <template>
            <el-select v-model="value" placeholder="请选择年份" 
            value-key="id" style="margin-top:20px;width:120px" @change="getYear">
                <el-option
                v-for="item in options"
                :key="item.is"
                :label="item.label"
                :value="item">
                </el-option>
            </el-select>
            <span style="margin-left:470px;color:#99a9bf">tip：默认显示2019年部分大学排名~</span>
            <i style="margin-left:70px" class="el-icon-d-arrow-right"></i>
            <span class="openView" @click="turnView">折线图显示</span>
        </template>

        <!-- 数据展示 -->
        <template>
            <el-table
                :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)" stripe
                style="width: 45%;margin-left:300px"
                class="table">
                <el-table-column
                prop="u_year"
                label="年份"
                width="160">
                </el-table-column>
                <el-table-column
                prop="ranking"
                label="名次"
                width="160">
                </el-table-column>
                <el-table-column
                prop="uname"
                label="大学">
                </el-table-column>
            </el-table>
            
            <!-- 分页展示 -->
            <el-pagination v-if="show"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page.sync="currentPage"
                :page-size="10"
                layout="total, sizes, prev, pager, next, jumper"
                :total="tableData.length">
            </el-pagination>
        </template>

        
    </div>
    
</template>
<script>

    import NavHeader from '../components/NavHeader.vue'
    export default {
        name:'university-list',
        components:{
            'nav-header':NavHeader
        },
        data(){
            return{
                currentPage:1,//初始页码
                pagesize:10,
                tableData:[],
                show:false,
                options: [{
                    value: '选项1',
                    label: '2015',
                    id:1
                    }, {
                    value: '选项2',
                    label: '2016',
                    id:2
                    }, {
                    value: '选项3',
                    label: '2017',
                    id:3
                    }, {
                    value: '选项4',
                    label: '2018',
                    id:4
                    }, {
                    value: '选项5',
                    label: '2019',
                    id:5
                    }],
                    value: ''
            }
        },
        mounted(){
            this.init()
        },
        created(){
            this.getUniversity2019();
        },
        methods:{
            init(){
                return 0
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
            //2019年默认出现
            getUniversity2019() {
                var _this=this;
				this.$http.get('/api/user/getUList',{
                    params:{
                        year:2019
                    }
                }).then(function(res) {
					// console.log(res.data)
                    this.$data.tableData = res.data
                    this.show=true
                })
            },
            getYear(val){
                this.year = val.label
                var _this=this;
				this.$http.get('/api/user/getUList',{
                    params:{
                        year:this.year
                    }
                }).then(function(res) {
					// console.log(res.data)
                    this.$data.tableData = res.data
                    this.show=true
                })
            },
            turnView(){
                this.$router.push('/1/university_detail')

            }
            
            
        }
        
    }
</script>
<style lang="scss">
    @import '../assets/scss/reset.scss';
    
    .el-pagination{
        margin-top: 15px;
        margin-left:20%;
    }
    .openView{
        color:#3f3d3d
    }
    .openView:hover{
        color:#41b883;
    }
</style>

