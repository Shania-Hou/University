<template>
<!-- 展示大学的排名趋势折线图 -->
    <div class="container">
        <router-view></router-view>
        <h3>十所高校2015-2019排名</h3>
        <el-select v-model="value" placeholder="请选择" style="width:120px" >
            <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value" @click.native.prevent="check(value)">
            </el-option>
        </el-select>
        <span style="margin-left:570px;color:#99a9bf">tip：默认显示前10名~</span>

        <ulist_echarts1 v-show="ifshow1"></ulist_echarts1>
        <ulist_echarts2 v-show="ifshow2"></ulist_echarts2>
        <ulist_echarts3 v-show="ifshow3"></ulist_echarts3>
        <ulist_echarts4 v-show="ifshow4"></ulist_echarts4>
        <ulist_echarts5 v-show="ifshow5"></ulist_echarts5>
    </div>
    
</template>
<script>
    import UlistEcharts1 from '../components/ulist_echarts1.vue'
    import UlistEcharts2 from '../components/ulist_echarts2.vue'
    import UlistEcharts3 from '../components/ulist_echarts3.vue'
    import UlistEcharts4 from '../components/ulist_echarts4.vue'
    import UlistEcharts5 from '../components/ulist_echarts5.vue'

    import echarts from 'echarts'
    export default {
        name:'university-detail',
        components:{
            'ulist_echarts1':UlistEcharts1,
            'ulist_echarts2':UlistEcharts2,
            'ulist_echarts3':UlistEcharts3,
            'ulist_echarts4':UlistEcharts4,
            'ulist_echarts5':UlistEcharts5,
        },
        data(){
            return{
                ifshow1:true,
                ifshow2:false,
                ifshow3:false,
                ifshow4:false,
                ifshow5:false,

                options: [{
                    value: '1',
                    label: '第1-10名'
                    }, {
                    value: '2',
                    label: '第11-20名'
                    }, {
                    value: '3',
                    label: '第21-30名'
                    }, {
                    value: '4',
                    label: '第31-40名'
                    }, {
                    value: '5',
                    label: '第41-50名'
                    }],
                value: '',
            }
        },
        
        methods: {
            check(value){
                var val=this.value
                if(val==1){
                    this.ifshow1=true;
                    this.ifshow2=false;
                    this.ifshow3=false;
                    this.ifshow4=false;
                    this.ifshow5=false;
                }
                if (val==2) {
                    this.ifshow1=false;
                    this.ifshow2=true;
                    this.ifshow3=false;
                    this.ifshow4=false;
                    this.ifshow5=false;
                }
                if (val==3) {
                    this.ifshow1=false;
                    this.ifshow2=false;
                    this.ifshow3=true;
                    this.ifshow4=false;
                    this.ifshow5=false;
                }
                if (val==4) {
                    this.ifshow1=false;
                    this.ifshow2=false;
                    this.ifshow3=false;
                    this.ifshow4=true;
                    this.ifshow5=false;
                }
                if (val==5) {
                    this.ifshow1=false;
                    this.ifshow2=false;
                    this.ifshow3=false;
                    this.ifshow4=false;
                    this.ifshow5=true;
                }
                

            }
        },
        watch: {},
        created() {
    
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