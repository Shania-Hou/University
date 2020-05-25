<template>
    <div id="echarts2" class="echarts" ></div>
</template>
<script>
    import echarts from 'echarts'
    export default {
    
        name:'ulist_11-20',
        data(){
            return{
                    
                
            }
        },
        mounted () {
            let myChart = echarts.init(document.getElementById('echarts2'));
            let option = {
                title: {
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['中山大学', '北京航空航天大学', '同济大学', '武汉大学', '四川大学',
                        '南开大学', '西安交通大学', '大连理工大学', '天津大学', '山东大学']
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
                    min:5,
                    max:30,
                    inverse:true,
                    
                },
                series: [
                    {
                        name: '中山大学',
                        type: 'line',
                        data: [11,10,9,9,9]
                    },
                    {
                        name: '北京航空航天大学',
                        type: 'line',
                        data: [12,14,14,15,11]
                    },
                    {
                        name: '同济大学',
                        type: 'line',
                        data: [13,13,11,11,13]
                    },
                    {
                        name: '武汉大学',
                        type: 'line',
                        data: [14,16,13,12,12]
                    },
                    {
                        name: '四川大学',
                        type: 'line',
                        data: [14,15,16,17,15]
                    },
                    {
                        name: '南开大学',
                        type: 'line',
                        data: [16,18,15,16,18]
                    },
                    {
                        name: '南京大学',
                        type: 'line',
                        data: [12,14,14,15,11]
                    },
                    {
                        name: '西安交通大学',
                        type: 'line',
                        data: [17,17,16,14,14]
                    },
                    {
                        name: '大连理工大学',
                        type: 'line',
                        data: [18,19,23,25,26]
                    },
                    {
                        name: '天津大学',
                        type: 'line',
                        data: [19,12,18,18,19]
                    },
                    {
                        name: '山东大学',
                        type: 'line',
                        data: [20,20,22,24,23]
                    }
                ]
            };
            myChart.setOption(option);
        }
    }
</script>
<style>
    .chart{
        width: 750px;
        height: 500px;
        margin: 0 auto;
    }
</style>