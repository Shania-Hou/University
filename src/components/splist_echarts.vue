<template>
    <div id="echarts1" class="echarts" ></div>
</template>
<script>
    import echarts from 'echarts'
    export default {
        name:'sp_echarts1',
        data(){
            return{
            }
        },
        mounted () {
            
            this.drawCharts()
        },
        methods:{
            drawCharts(){
                var myChart = echarts.init(document.getElementById("echarts1"));
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
                        data: ['中国人民大学', '北京大学', '复旦大学', '武汉大学', '南京大学', '中山大学', '华东师范大学', '北京师范大学','清华大学','四川大学']
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
                            label:{
                                normal:{
                                    show:true,
                                }
                                
                            },
                            data: [
                                
                                {value: 15, name: '中国人民大学'},
                                {value: 13, name: '北京大学'},
                                {value: 12, name: '复旦大学'},
                                {value: 11, name: '武汉大学'},
                                {value: 10, name: '南京大学'},
                                {value: 9, name: '中山大学'},
                                {value: 8, name: '华东师范大学'},
                                {value: 7, name: '北京师范大学'},
                                {value: 6, name: '清华大学'},
                                {value: 5, name: '四川大学'},
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