<template>
<h2>-{{loggedRestaurant}}-</h2>
  <h3>
    Menú del día 
  </h3>
  <p>{{ dateParsed }}</p>
  <div class="modify_div_btn">
    <router-link :to="{name: 'MenuModifyPage', params: {date: this.$route.params.date}}">
    <button>Modificar menu</button>
    </router-link>
  </div> 
  <h3>Primeros</h3>
  <section v-for="menu in this.firsts" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>{{ menu.name_dish }}</li>
      <li class="menu_detail">{{ menu.desc_dish }}</li>
    </ul>
  </section>
  <h3>Segundos</h3>
  <section v-for="menu in this.seconds" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>{{ menu.name_dish }}</li>
      <li class="menu_detail">{{ menu.desc_dish }}</li>
    </ul>
  </section>
  <h3>Postres</h3>
  <section v-for="menu in this.desserts" :key="menu.id_dish">
    <ul class="split_the_dishes">
      <li>{{ menu.name_dish }}</li>
      <li class="menu_detail">{{ menu.desc_dish }}</li>
    </ul>
  </section>
</template>

<script>
import config from "@/config.js"
export default {
  
  data() {
    return {
      firsts: [],
      seconds: [],
      desserts: [],
      date: this.$route.params.date,
      parsedDate:'',
      loggedRestaurant:localStorage.name
    };
  },

  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const settings = {
        method: "GET",
        headers: {
          Authorization: localStorage.id_restaurant,
        },
      }
      const response = await fetch(`${config.API_PATH}/menus/by-date/` + this.$route.params.date,settings);
      let menus = await response.json();
      console.log('Headers', settings.headers)
      this.firsts = menus.desc.firsts;
      this.seconds = menus.desc.seconds;
      this.desserts = menus.desc.desserts;
    },
  },
  computed:{
    dateParsed() {
      let year=this.date.slice(0,4)
      let day=this.date.slice(8,10)
      let month=this.date.slice(5,7)
      let months={'01':'Enero','02':'Febrero','03':'Marzo','04':'Abril','05':'Mayo','06':'Junio','07':'Julio','08':'Agosto','09':'Septiembre','10':'Octubre','11':'Noviembre','12':'Diciembre'}
      let fullDate=day+' de '+months[month]+' de '+year
      return fullDate
    }
  }
};
</script>

<style scoped>
* {
  padding: 0;
  margin: 0;
}

li {
  text-align: center;
  margin: 0.3em;
  list-style: none;
  font-style: bold;
}

.split_the_dishes {
  margin: 0.8em;
}
.menu_detail{
  font-size:11px;
  font-style: italic;
}
.modify_div_btn{
  display:flex;
  justify-content: flex-end
}
</style>
