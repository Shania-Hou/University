<template>
    <div id="echarts2" class="echarts" ></div>
</template>
<script>
    import echarts from 'echarts'
    export default {
        name:'splist_echarts2',
        data(){
            return{

            }
        },
        mounted () {
            this.drawCharts()
        },
        methods:{
            drawCharts(){
                var myChart = echarts.init(document.getElementById("echarts2"));
                myChart.setOption ({

                    title: {
                        text: '',
                        subtext: '',
                        left: 'center'
                    },
                    tooltip: {
                        trigger: 'item',
                        show:false
                        
                    },
                    legend: {
                        left: 'center',
                        top: 'bottom',
                        data: ['清华大学', '国防科技大学', '北京航空航天大学', '浙江大学'
                        , '华东师范大学', '北京大学', '南京大学', '大连理工大学','天津大学'
                        ,'中山大学']
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            mark: {show: true},
                            dataView: {show: true, readOnly: true},
                            magicType: {
                                show: true,
                                type: ['pie']
                            },
                            restore: {show: true},
                            saveAsImage: {show: true}
                        }
                    },
                    series: [
                        {
                            name: '面积模式',
                            type: 'pie',
                            radius: [30, 150],
                            center: ['50%', '50%'],
                            roseType: 'area',
                            data: [
                                {value: 5, name: '中山大学'},
                                {value: 6, name: '天津大学'},
                                {value: 7, name: '大连理工大学'},
                                {value: 8, name: '南京大学'},
                                {value: 9, name: '北京大学'},
                                {value: 10, name: '华东师范大学'},
                                {value: 11, name: '浙江大学'},
                                {value: 12, name: '北京航空航天大学'},
                                {value: 13, name: '国防科技大学'},
                                {value: 15, name: '清华大学'},
                                
                            ]
                        }
                    ]
                })

            }

        }
            
    }
</script>
<style>
    .echarts{
        width: 750px;
        height: 500px;
        margin: 0 auto;
        /* border:1px solid  */
    }
</style>