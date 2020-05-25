<template>
    <div class="container">
        <router-view></router-view>
        <h3>专业排名</h3>
        <template>
            <el-select v-model="value" placeholder="请选择年份" 
            value-key="id" style="margin-top:20px;width:120px" >
                <el-option
                v-for="item in options1"
                :key="item.id"
                :label="item.label"
                :value="{'id':item.id,'year':item.label}">
                </el-option>
            </el-select>
        </template>
        <template>
            <el-cascader
                placeholder="搜索门类"
                :options="options"
                :props="{ expandTrigger: 'hover' }"
                style="margin-top:20px;width:170px"
                ref="getLabel"
                filterable>
            </el-cascader>
        </template>
        <el-button type="primary" icon="el-icon-search" @click="getAll" ></el-button>
        <span style="margin-left:330px;color:#99a9bf">tip：默认显示2017年 <strong style="color:black">哲学 </strong>的前10名~</span>
        <sp_echarts1 v-show="show1"></sp_echarts1>
        <sp_echarts2 v-show="show2"></sp_echarts2>
        
    </div>
    
</template>
<script>
    import echarts from 'echarts'
    import Sp_echarts1 from '../components/splist_echarts'
    import Sp_echarts2 from '../components/splist_echarts2'

    export default {
        name:'speciality-detail',
        data () {
            return {
                show1:true,
                show2:false,
                tableData:[],
                value:[],
                //年份
                options1: [{
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
                
                //门类与专业
                options:[{
                    value:'zhexue',
                    label:'哲学'
                },{
                    value:'jingjixue',
                    label:'经济学',
                    children:[{
                        value:'lilunjingjixue',
                        label:'理论经济学'
                    },{
                        value:'yingyongjingjixue',
                        label:'应用经济学'
                    }]
                },{
                    value:'faxue',
                    label:'法学',
                    children:[{
                        value:'faxue',
                        label:'法学'
                    },{
                        value:'zhengzhixue',
                        label:'政治学'
                    },{
                        value:'shehuixue',
                        label:'社会学'
                    },{
                        value:'minzuxue',
                        label:'民族学'
                    },{
                        value:'makesizhuyililun',
                        label:'马克思主义理论'
                    }]
                },{
                    value:'jiaoyuxue',
                    label:'教育学',
                    children:[{
                        value:'jiaoyuxue',
                        label:'教育学'
                    },{
                        value:'xinlixue',
                        label:'心理学'
                    },{
                        value:'tiyuxue',
                        label:'体育学'
                    }]
                },{
                    value:'wenxue',
                    label:'文学',
                    children:[{
                        value:'zhongguoyuyanwenxue',
                        label:'中国语言文学'
                    },{
                        value:'waiguoyuyanwenxue',
                        label:'外国语言文学'
                    },{
                        value:'xinwenchuanboxue',
                        label:'新闻传播学'
                    }]
                },{
                    value:'lishixue',
                    label:'历史学',
                    children:[{
                        value:'kaoguxue',
                        label:'考古学'
                    },{
                        value:'zhongguoshi',
                        label:'中国史'
                    },{
                        value:'shijieshi',
                        label:'世界史'
                    }]
                },{
                    value:'lixue',
                    label:'理学',
                    children:[{
                        value:'shuxue',
                        label:'数学'
                    },{
                        value:'wulixue',
                        label:'物理学'
                    },{
                        value:'huaxue',
                        label:'化学'
                    },{
                        value:'tianwenxue',
                        label:'天文学'
                    },{
                        value:'dilixue',
                        label:'地理学'
                    },{
                        value:'daqikexue',
                        label:'大气科学'
                    },{
                        value:'haiyangkexue',
                        label:'海洋科学'
                    },{
                        value:'diqiuwulixue',
                        label:'地球物理学'
                    },{
                        value:'dizhixue',
                        label:'地质学'
                    },{
                        value:'shengwuxue',
                        label:'生物学'
                    },{
                        value:'shengtaixue',
                        label:'生态学'
                    },{
                        value:'tongjixue',
                        label:'统计学'
                    },]
                },{
                    value:'gongxue',
                    label:'工学',
                    children:[{
                        value:'lixue',
                        label:'力学'
                    },{
                        value:'jixiegongcheng',
                        label:'机械工程'
                    },{
                        value:'yiqikexueyujishu',
                        label:'仪器科学与技术'
                    },
                    {
                        value:'cailiaokexueyugongcheng',
                        label:'材料科学与工程'
                    },{
                        value:'yejingongcheng',
                        label:'冶金工程'
                    },{
                        value:'dongligongchengjigongchengrewuli',
                        label:'动力工程及工程热物理'
                    },
                    {
                        value:'dianqigongcheng',
                        label:'电气工程'
                    },{
                        value:'dianzikexueyujishu',
                        label:'电子科学与技术'
                    },{
                        value:'xinxiyutongxingongcheng',
                        label:'信息与通信工程'
                    },
                    {
                        value:'kongzhikexueyugongcheng',
                        label:'控制科学与工程'
                    },{
                        value:'jisuanjikexueyujishu',
                        label:'计算机科学与技术'
                    },{
                        value:'jianzhuxue',
                        label:'建筑学'
                    },{
                        value:'tumugongcheng',
                        label:'土木工程'
                    },{
                        value:'shuiligongcheng',
                        label:'水利工程'
                    },{
                        value:'cehuikexueyujishu',
                        label:'测绘科学与技术'
                    },{
                        value:'huaxuegongchengyujishu',
                        label:'化学工程与技术'
                    },{
                        value:'dizhiziyuanyudizhigongcheng',
                        label:'地质资源与地质工程'
                    },{
                        value:'kuangyegongcheng',
                        label:'矿业工程'
                    },{
                        value:'shiyouyutianranqigongcheng',
                        label:'石油与天然气工程'
                    },{
                        value:'fangzhikexueyugongcheng',
                        label:'纺织科学与工程'
                    },{
                        value:'qinggongjishuyugongcheng',
                        label:'轻工技术与工程'
                    },
                    {
                        value:'jiaotongyunshugongcheng',
                        label:'交通运输工程'
                    },{
                        value:'chuanboyuhaiyanggongcheng',
                        label:'船舶与海洋工程'
                    },{
                        value:'hangkongyuhangkexueyujishu',
                        label:'航空宇航科学与技术'
                    },{
                        value:'hekexueyujishu',
                        label:'核科学与技术'
                    },{
                        value:'nongyegongcheng',
                        label:'农业工程'
                    },{
                        value:'huanjingkexueyugongcheng',
                        label:'环境科学与工程'
                    },{
                        value:'shengwuyixuegongcheng',
                        label:'生物医学工程'
                    },{
                        value:'shipinkexueyugongcheng',
                        label:'食品科学与工程'
                    },{
                        value:'chengxiangguihuaxue',
                        label:'城乡规划学'
                    },{
                        value:'ruanjiangongcheng',
                        label:'软件工程'
                    },{
                        value:'anquankexueyugongcheng',
                        label:'安全科学与工程'
                    }]
                },{
                    value:'nongxue',
                    label:'农学',
                    children:[{
                        value:'zuowuxue',
                        label:'作物学'
                    },{
                        value:'yuanyixue',
                        label:'园艺学'
                    },{
                        value:'nongyeziyuanyuhuanjing',
                        label:'农业资源与环境'
                    },{
                        value:'zhiwubaohu',
                        label:'植物保护'
                    },{
                        value:'chumuxue',
                        label:'畜牧学'
                    },{
                        value:'shouyixue',
                        label:'兽医学'
                    },{
                        value:'linxue',
                        label:'林学'
                    },{
                        value:'shuichan',
                        label:'水产'
                    },{
                        value:'caoxue',
                        label:'草学'
                    },]
                },{
                    value:'guanlixue',
                    label:'管理学',
                    children:[{
                        value:'guanlikexueyugongcheng',
                        label:'管理科学与工程'
                    },{
                        value:'gongshangguanli',
                        label:'工商管理'
                    },{
                        value:'nonglinjingjiguanli',
                        label:'农林经济管理'
                    },{
                        value:'gonggongguanli',
                        label:'公共管理'
                    },{
                        value:'tushuqingbaoyudanganguanli',
                        label:'图书情报与档案管理'
                    }]
                },{
                    value:'yixue',
                    label:'医学',
                    children:[{
                        value:'jichuyixue',
                        label:'基础医学'
                    },{
                        value:'linchuangyixue',
                        label:'临床医学'
                    },{
                        value:'kouqiangyixue',
                        label:'口腔医学'
                    },{
                        value:'gonggongweishengyuyufangyixue',
                        label:'公共卫生与预防医学'
                    },{
                        value:'zhongyixue',
                        label:'中医学'
                    },{
                        value:'zhongxiyijiehe',
                        label:'中西医结合'
                    },{
                        value:'yaoxue',
                        label:'药学'
                    },{
                        value:'zhongyaoxue',
                        label:'中药学'
                    },{
                        value:'tezhongyixue',
                        label:'特种医学'
                    },{
                        value:'hulixue',
                        label:'护理学'
                    }]
                },{
                    value:'yishuxue',
                    label:'艺术学',
                    children:[{
                        value:'yishuxuelilun',
                        label:'艺术学理论'
                    },{
                        value:'yinyueyuwudaoxue',
                        label:'音乐与舞蹈学'
                    },{
                        value:'xijuyuyingshixue',
                        label:'戏剧与影视学'
                    },{
                        value:'meishuxue',
                        label:'美术学'
                    },{
                        value:'shejixue',
                        label:'设计学'
                    }]
                }
                ]
            }
        },
        components:{
            'sp_echarts1':Sp_echarts1,
            'sp_echarts2':Sp_echarts2
        },
        mounted () {
            
        },
        
        methods: {
           
            getAll(){
                // var _self = this
                // var data2 = {
                //     year:this.value.year,
                //     speciality:this.$refs['getLabel'].getCheckedNodes()[0].label
                // }
                // this.$http.get('/api/user/getUniversityByYearAndSpeciality',{
                //     params:{
                //         year:data2.year,
                //         speciality:data2.speciality
                //     }
                // }).then(function(res) {
                //     let newData = {'year':'','ranking':[],'uname':[]}
                //     for(let i = 0;i < res.data.length; i ++){
                //         let year = res.data[0].sp_year 
                //         let ranking = res.data[i].ranking
                //         let uname=res.data[i].u_name
                //         newData.year=year
                //         newData.ranking.push(ranking)
                //         newData.uname.push(uname)

                //     }
                //     // console.log(newData)
				// 	// console.log(res.data[0].u_name)
                //     this.$data.tableData = newData
                //     // this.ifChild=true
                
                // })
                // this.$refs.child.getParent()


                this.show1=false
                this.show2=true
                console.log(this.show1+'   '+this.show2)
            },
        }
    }
</script>
<style lang="scss">
    @import '../assets/scss/reset.scss';
    #selectCity{
        margin:0px 4px 5px 0px !important;
        border:gray 1px solid !important;
    }
    h2{
        text-align: center;
        padding: 30px;
        font-size: 18px;
    }
</style>