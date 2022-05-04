import { createRouter, createWebHistory } from 'vue-router'
import menu from '../pages/menu/MenuPage.vue'
import home from '../pages/home/HomePage.vue'
import menus from '../pages/menus/MenusPage.vue'
import MenuAddPage from '../pages/menu-add/MenuAddPage.vue'
import MenuModifyPage from '../pages/menu-modify/MenuModifyPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: home
  },
  {
    path :'/menus/by-date/:date',
    name : 'Menu',
    component: menu
  },
  {
    path :'/menus',
    name : 'Menus',
    component: menus
  },
  {
    path: '/menu/add',
    name: 'MenuAddPage',
    component: MenuAddPage
  },
  {
    path: '/menu/modify',
    name: 'MenuModifyPage',
    component: MenuModifyPage
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
