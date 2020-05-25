<template>
    <div id="echarts3" class="echarts" ></div>
</template>
<script>
    import echarts from 'echarts'
    export default {
        name:'ulist_21-30',
        data(){
            return{ 
            }
        },
        methods:{
            drawCharts() {
                var myChart = echarts.init(document.getElementById('echarts3'));
                console.log(123);
                myChart.setOption({
                    tooltip: {
                        trigger: 'item'
                    },
                    legend: {
                        data: ['吉林大学', '华南理工大学', '厦门大学', '北京师范大学', '北京理工大学',
                            '中国人民大学', '华东理工大学', '中南大学', '重庆大学', '东北大学']
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
                        min:15,
                        max:55,
                        inverse:true,
                        
                    },
                    series: [
                        {
                            name: '吉林大学',
                            type: 'line',
                            data: [21,22,24,23,25]
                        },
                        {
                            name: '华南理工大学',
                            type: 'line',
                            data: [22,21,19,19,20]
                        },
                        {
                            name: '厦门大学',
                            type: 'line',
                            data: [23,23,21,22,23]
                        },
                        {
                            name: '北京师范大学',
                            type: 'line',
                            data: [24,24,20,20,22]
                        },
                        {
                            name: '北京理工大学',
                            type: 'line',
                            data: [25,25,25,21,16]
                        },
                        {
                            name: '中国人民大学',
                            type: 'line',
                            data: [26,31,28,30,31]
                        },
                        {
                            name: '华东理工大学',
                            type: 'line',
                            data: [27,30,32,34,36]
                        },
                        {
                            name: '中南大学',
                            type: 'line',
                            data: [28,27,26,26,21]
                        },
                        {
                            name: '重庆大学',
                            type: 'line',
                            data: [28,33,35,35,37]
                        },
                        {
                            name: '东北大学',
                            type: 'line',
                            data: [30,48,55,42,40]
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