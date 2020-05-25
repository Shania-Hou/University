import Vue from 'vue'
import Router from 'vue-router'
import Home from '../pages/home'
import Index from '../pages/index.vue'
import University from '../pages/university'
import Speciality from '../pages/speciality'
import University_detail from '../pages/university_detail.vue'
import Speciality_detail from '../pages/speciality_detail.vue'
import Login from '../pages/login.vue'
import User_self from '../pages/user_self.vue'
import University_list from '../pages/university_list.vue'
import Speciality_list from '../pages/speciality_list.vue'
import Tuijian from '../pages/tuijian.vue'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      redirect:'/index',
      component: Home,
      children:[
        
        {
          path: '/index',
          name: 'index',
          component: Index,
        },{
          // 所有大学
          path: '/university',
          name: 'university',
          component: University
        },
        {
          // 某大学排名走势
          path: '/:id/university_detail',
          name: 'university-detail',
          component: University_detail,
        },
        {
          // 大学排名
            path: '/university-list',
            name: 'university-list',
            component: University_list,
        }
        ,{
          // 所有专业
          path: '/speciality',
          name: 'speciality',
          component: Speciality,
          // children:[
            
          // ]
        },{
          // 专业排名
          path: '/speciality-list',
          name: 'speciality-list',
          component: Speciality_list,
        },{
          
            // 某专业排名走势
            path: '/:id/speciality_detail',
            name: 'speciality-detail',
            component: Speciality_detail,
          
        },{
          // 推荐大学
          path: '/tuijian',
          name: 'tuijian',
          component: Tuijian
        },
      ]
    },{
      path: '/login',
      name: 'login',
      component: Login
    },{
      path: '/user_self',
      name: 'user_self',
      component: User_self
    }
  ]
})
