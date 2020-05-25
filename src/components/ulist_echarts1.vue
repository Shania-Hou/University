<template>
    <div id="echarts1" class="echarts" ></div>
</template>
<script>
    import echarts from 'echarts'
    export default {
        name:'ulist_1-10',
        data(){
            return{
            }
        },
        methods:{
            drawCharts() {
                var myChart = echarts.init(document.getElementById('echarts1'));
                // console.log(123);
                myChart.setOption({
                    tooltip: {
                        trigger: 'item'
                    },
                    legend: {
                        data: ['清华大学', '北京大学', '浙江大学', '上海交通大学', '复旦大学',
                            '中国科学技术大学', '南京大学', '哈尔滨工业大学', '华中科技大学', '东南大学']
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
                        max:20,
                        inverse:true,
                        
                    },
                    series: [
                        {
                            name: '清华大学',
                            type: 'line',
                            data: [1,1,1,1,1]
                        },
                        {
                            name: '北京大学',
                            type: 'line',
                            data: [2,2,2,2,2]
                        },
                        {
                            name: '浙江大学',
                            type: 'line',
                            data: [3,3,3,3,3]
                        },
                        {
                            name: '上海交通大学',
                            type: 'line',
                            data: [4,4,4,4,4]
                        },
                        {
                            name: '复旦大学',
                            type: 'line',
                            data: [5,5,5,5,5]
                        },
                        {
                            name: '中国科学技术大学',
                            type: 'line',
                            data: [6,7,6,6,6]
                        },
                        {
                            name: '南京大学',
                            type: 'line',
                            data: [7,6,7,7,7]
                        },
                        {
                            name: '哈尔滨工业大学',
                            type: 'line',
                            data: [8,8,10,10,10]
                        },
                        {
                            name: '华中科技大学',
                            type: 'line',
                            data: [9,9,8,8,7]
                        },
                        {
                            name: '东南大学',
                            type: 'line',
                            data: [9,11,12,13,17]
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