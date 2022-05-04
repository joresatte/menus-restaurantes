<template>
  <div class="home">
    <img alt="menu logo" src="@/assets/img/imagen_de_bienbenida_menu.png" />
    <h1>Bienvenido</h1>
  </div>

  <select v-model="selectedRestaurant">
    <option :value="null" disabled>Selecciona un restaurante</option>
    <option v-for="restaurant in restaurants" :value="restaurant" :key="restaurant.id_restaurant">{{restaurant.name}}</option>
    </select>
<button @click="onButtonClicked()">Ver los menus</button> 
</template>

<script>
import config from "@/config.js"
export default {
  name: 'Home',
  data(){
    return{
      restaurants:[],
      selectedRestaurant:null,
    }
  },
  mounted(){
    this.loadData()
  },
  methods:{
    async loadData(){
      var response = await fetch(`${config.API_PATH}/restaurants`)
      this.restaurants = await response.json()
    },
  onButtonClicked(){
      localStorage.id_restaurant=this.selectedRestaurant.id_restaurant
      localStorage.name=this.selectedRestaurant.name
      this.$router.push('/menus')
    }
  }
}
</script>

<style scoped>
h1 {
  font-style: italic;
}
img{
  width: 30vw;

}
</style>
