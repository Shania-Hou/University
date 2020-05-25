<template>
    <div id="echarts5" class="echarts" ></div>
</template>
<script>
    import echarts from 'echarts'
    export default {
    
        name:'ulist_41-50',
        data(){
            return{ 
            }
        },
        
        methods:{
            drawCharts() {
                var myChart = echarts.init(document.getElementById('echarts5'));
                console.log(123);
                myChart.setOption({
                    tooltip: {
                        trigger: 'item'
                    },
                    legend: {
                        data: ['中国地质大学(武汉)','中国地质大学(北京)', '南京理工大学', '北京邮电大学', '北京交通大学', '北京化工大学',
                            '西安电子科技大学', '华北电力大学', '武汉理工大学', '东华大学', '华中师范大学']
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: ['2015', '2016', '2017', '2018', '2019'],
                        axisLine:{
                            onZero:false
                        }
                    },
                    yAxis: {
                        type: 'value',
                        min:35,
                        max:75,
                        inverse:true,
                        
                    },
                    series: [
                        {
                            name: '中国地质大学(武汉)',
                            type: 'line',
                            data: [41,35,65,61,63]
                        },
                        {
                            name: '中国地质大学(北京)',
                            type: 'line',
                            data: [41,63,,69,72]
                        },
                        {
                            name: '南京理工大学',
                            type: 'line',
                            data: [42,42,39,37,38]
                        },
                        {
                            name: '北京邮电大学',
                            type: 'line',
                            data: [43,44,47,48,42]
                        },
                        {
                            name: '北京交通大学',
                            type: 'line',
                            data: [44,40,41,45,46]
                        },
                        {
                            name: '北京化工大学',
                            type: 'line',
                            data: [45,40,42,48,50]
                        },
                        {
                            name: '西安电子科技大学',
                            type: 'line',
                            data: [46,45,51,54,48]
                        },
                        {
                            name: '华北电力大学',
                            type: 'line',
                            data: [46,43,54,59,56]
                        },
                        {
                            name: '武汉理工大学',
                            type: 'line',
                            data: [46,46,44,47,45]
                        },
                        {
                            name: '东华大学',
                            type: 'line',
                            data: [49,51,47,48,52]
                        },
                        {
                            name: '华中师范大学',
                            type: 'line',
                            data: [50,48,47,43,46]
                        }
                    ]
                })
        }
        
    },
    mounted () {
            this.drawCharts()
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