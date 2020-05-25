<template>
    <div id="echarts4" class="echarts" ></div>
</template>
<script>
    import echarts from 'echarts'
    export default {
    
        name:'ulist_31-40',
        data(){
            return{ 
            }
        },
        
        methods:{
            drawCharts() {
                var myChart = echarts.init(document.getElementById('echarts4'));
                console.log(123);
                myChart.setOption({
                    tooltip: {
                        trigger: 'item'
                    },
                    legend: {
                        data: ['华东师范大学', '南京航空航天大学', '中国石油大学(北京)','中国石油大学(华东)', '苏州大学', '湖南大学',
                            '电子科技大学', '中国农业大学', '西北工业大学', '上海大学', '北京科技大学']
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
                        min:25,
                        max:97,
                        inverse:true,
                        
                    },
                    series: [
                        {
                            name: '华东师范大学',
                            type: 'line',
                            data: [31,34,32,32,32]
                        },
                        {
                            name: '南京航空航天大学',
                            type: 'line',
                            data: [32,29,36,35,33]
                        },
                        {
                            name: '中国石油大学(北京)',
                            type: 'line',
                            data: [32,38,74,97,87]
                        },
                        {
                            name: '中国石油大学(华东)',
                            type: 'line',
                            data: [,,80,80,82]
                        },
                        {
                            name: '苏州大学',
                            type: 'line',
                            data: [34,26,28,27,29]
                        },
                        {
                            name: '湖南大学',
                            type: 'line',
                            data: [35,31,31,31,28]
                        },
                        {
                            name: '电子科技大学',
                            type: 'line',
                            data: [35,36,34,33,27]
                        },
                        {
                            name: '中国农业大学',
                            type: 'line',
                            data: [35,38,39,40,42]
                        },
                        {
                            name: '西北工业大学',
                            type: 'line',
                            data: [38,36,30,29,30]
                        },
                        {
                            name: '上海大学',
                            type: 'line',
                            data: [39,46,50,41,41]
                        },
                        {
                            name: '北京科技大学',
                            type: 'line',
                            data: [39,28,37,37,39]
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