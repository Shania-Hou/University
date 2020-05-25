<template>
<!-- 展示全部专业 -->
    <div class="container">
        <router-view></router-view>
        <div style="margin:20px 0 0 12%">
            <img src="../icon/1.png">
            <img src="../icon/2.png">
            <img src="../icon/3.png">
            <img src="../icon/4.png">
            <img src="../icon/5.png">
            <img src="../icon/6.png">
            <img src="../icon/7.png">
            <img src="../icon/8.png">
            <img src="../icon/9.png">
            <img src="../icon/10.png">
            <img src="../icon/11.png">
            <img src="../icon/12.png">
            <img src="../icon/13.png">
            <img src="../icon/14.png">
            <img src="../icon/15.png">
            <img src="../icon/16.png">
            <img src="../icon/17.png">
            <img src="../icon/18.png">
            <img src="../icon/19.png">
            <img src="../icon/20.png">
            <img src="../icon/21.png">
            <img src="../icon/22.png">
            <img src="../icon/23.png">
            <img src="../icon/24.png">
            <img src="../icon/25.png">
            <img src="../icon/26.png">
            <img src="../icon/27.png">
            <img src="../icon/28.png">
            <img src="../icon/29.png">
            <img src="../icon/30.png">
            <img src="../icon/31.png">
            <img src="../icon/32.png">
            <img src="../icon/33.png">
            <img src="../icon/34.png">
        </div>
    </div>
</template>
<script>
    import NavHeader from '../components/NavHeader.vue'
    export default {
        name:'speciality',
        data(){
            return{
                //  List:[
                //     {
                //         'dep':'哲学',
                
                //         child1:[
                //             {
                //                 'lei':'哲学类',
                //                 child2:[{
                //                     'spName':'哲学',
                //                     'spId':'010101'
                //                 },{
                //                     'spName':'逻辑学',
                //                     'spId':'01010'
                //                 },{
                //                     'spName':'宗教学',
                //                     'spId':'010103'
                //                 },{
                //                     'spName':'伦理学',
                //                     'spId':'010104'
                //                 },
                                    

                //                 ]
                //             },{
                //                 'lei':'人文科学试验班',
                //             }
                //         ]
                //     },{
                //         'dep':'经济学',
                //         child1:[
                //             {
                //                 'lei':'经济学类',
                //                 child2:[{
                //                     'spName':'哲学',
                //                     'spId':'010101'
                //                 },{
                //                     'spName':'逻辑学',
                //                     'spId':'01010'
                //                 },{
                //                     'spName':'宗教学',
                //                     'spId':'010103'
                //                 },{
                //                     'spName':'伦理学',
                //                     'spId':'010104'
                //                 },
                                    

                //                 ]
                //             },
                //     },{
                //         'dep':'哲学',
                //         child1:[
                //             {
                //                 'lei':'哲学类',
                //                 'id':'1-1',
                //                 child2
                //             }
                //         ]
                //     },{
                //         'dep':'哲学',
                //         'id':1,
                //         child1:[
                //             {
                //                 'lei':'哲学类',
                //                 'id':'1-1',
                //                 child2
                //             }
                //         ]
                //     },{
                //         'dep':'哲学',
                //         'id':1,
                //         child1:[
                //             {
                //                 'lei':'哲学类',
                //                 'id':'1-1',
                //                 child2
                //             }
                //         ]
                //     },{
                //         'dep':'哲学',
                //         'id':1,
                //         child1:[
                //             {
                //                 'lei':'哲学类',
                //                 'id':'1-1',
                //                 child2
                //             }
                //         ]
                //     },{
                //         'dep':'哲学',
                //         'id':1,
                //         child1:[
                //             {
                //                 'lei':'哲学类',
                //                 'id':'1-1',
                //                 child2
                //             }
                //         ]
                //     },{
                //         'dep':'哲学',
                //         'id':1,
                //         child1:[
                //             {
                //                 'lei':'哲学类',
                //                 'id':'1-1',
                //                 child2
                //             }
                //         ]
                //     },{
                //         'dep':'哲学',
                //         'id':1,
                //         child1:[
                //             {
                //                 'lei':'哲学类',
                //                 'id':'1-1',
                //                 child2
                //             }
                //         ]
                //     },{
                //         'dep':'哲学',
                //         'id':1,
                //         child1:[
                //             {
                //                 'lei':'哲学类',
                //                 'id':'1-1',
                //                 child2
                //             }
                //         ]
                //     },{
                //         'dep':'哲学',
                //         'id':1,
                //         child1:[
                //             {
                //                 'lei':'哲学类',
                //                 'id':'1-1',
                //                 child2
                //             }
                //         ]
                //     },{
                //         'dep':'哲学',
                //         'id':1,
                //         child1:[
                //             {
                //                 'lei':'哲学类',
                //                 'id':'1-1',
                //                 child2
                //             }
                //         ]
                //     }
                // ]
            }
        },
        components:{
            'nav-header':NavHeader
        },
        methods:{
            handleOpen(key, keyPath) {
                    console.log(key, keyPath);
                },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            }
        }
    }
</script>
<style lang="scss">
    @import '../assets/scss/reset.scss';
</style>