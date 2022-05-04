<template>
<form >
    <p>{{loggedRestaurant}}</p>
    <section class="plates_info"  >
    <p>Primeros</p>
    <div class="firsts">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.firsts[0].name_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.firsts[0].desc_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.firsts[1].name_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.firsts[1].desc_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.firsts[2].name_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.firsts[2].desc_dish">
    </div>
    <p>Segundos</p>
    <div class="seconds">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.seconds[0].name_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.seconds[0].desc_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.seconds[1].name_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.seconds[1].desc_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.seconds[2].name_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.seconds[2].desc_dish">
    </div>
    <p>Postres</p>
    <div class="desserts">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[0].name_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[0].desc_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[1].name_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[1].desc_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[2].name_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[2].desc_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[3].name_dish">
        <input class="input_plate" type="text"  v-model="dict_plates.desc.desserts[3].desc_dish">
    </div>
    </section>
    <button @click.prevent="onSaveClicked">Modificar Menú</button>
</form>
    <!-- {{$data}} -->
</template>

<script>
import config from "@/config.js"
export default {
  name: "modifymenu",
  data() {
    return {
       dateReceived:this.$route.params.date,
       idReceived:this.$route.params.id,
       dict_plates:{'desc':{'firsts':[{'name_dish':'','desc_dish':'', 'id_dish':'01'},
                              {'name_dish':'','desc_dish':'', 'id_dish':'02'},
                              {'name_dish':'','desc_dish':'', 'id_dish':'03'}],
                     'seconds':[{'name_dish':'','desc_dish':'','id_dish':'04'},
                              {'name_dish':'','desc_dish':'', 'id_dish':'05'},
                              {'name_dish':'','desc_dish':'','id_dish':'06'}],
                     'desserts':[{'name_dish':'','desc_dish':'','id_dish':'07'},
                              {'name_dish':'','desc_dish':'','id_dish':'08'},
                              {'name_dish':'','desc_dish':'','id_dish':'09'},
                              {'name_dish':'','desc_dish':'','id_dish':'10'}]          
                    }
                    },
        loggedRestaurant:localStorage.name
    };
  },

  mounted() {
      this.loadData()
  },
  computed:{
  },
  methods: {
    async loadData(){
      const response = await fetch(`${config.API_PATH}/menus/by-date/` + this.dateReceived);
      this.dict_plates = await response.json();
    },
    areValidInputsFromMenu(){
      if(this.dict_plates.desc.firsts[0].name_dish==="" || this.dict_plates.desc.firsts[0].desc_dish==="" ||
         this.dict_plates.desc.firsts[1].name_dish==="" || this.dict_plates.desc.firsts[1].desc_dish==="" ||
         this.dict_plates.desc.firsts[2].name_dish==="" || this.dict_plates.desc.firsts[2].desc_dish==="" ||
         this.dict_plates.desc.seconds[0].name_dish===""||this.dict_plates.desc.seconds[0].desc_dish==="" ||
         this.dict_plates.desc.seconds[1].name_dish===""||this.dict_plates.desc.seconds[1].desc_dish==="" ||
         this.dict_plates.desc.seconds[2].name_dish===""||this.dict_plates.desc.seconds[2].desc_dish==="" ||
         this.dict_plates.desc.desserts[0].name_dish===""|| this.dict_plates.desc.desserts[0].desc_dish===""||
         this.dict_plates.desc.desserts[1].name_dish==="" ||this.dict_plates.desc.desserts[1].desc_dish==="" ||
         this.dict_plates.desc.desserts[2].name_dish==="" ||this.dict_plates.desc.desserts[2].desc_dish==="" ||
         this.dict_plates.desc.desserts[3].name_dish==="" ||this.dict_plates.desc.desserts[3].desc_dish==="")
        {
            console.log('Inputs vacios!')
            return false
        }
      else{
            return true
        }
    },
    async onSaveClicked(){
        if (this.areValidInputsFromMenu()===true){
            let desc=this.dict_plates.desc
            this.dictToSend={'date':this.dateReceived,'desc':desc, 'id':this.dict_plates.id}
            const settings={
            method:"PUT",
            body: JSON.stringify(this.dictToSend),
            headers:{
                Authorization: localStorage.id_restaurant,
                'Content-Type':'application/json'
                }
            }
            var response = await fetch(`${config.API_PATH}/menus`,settings)
            if (response.status===200){
            alert('Menu modificado con éxito!')
            this.$router.push("/menus")
            }
        }
        else{
            if (this.areValidInputsFromMenu()===false){
                alert('Inputs vacíos!')
            }
        }
    }
  },
}

</script>
<style scoped>
body{
    padding:0;
    margin:0;
}

.date{
    display:flex;
    justify-content: flex-end;
}
.firsts,
.seconds,
.desserts{
    display:grid;
    grid-template-columns:1fr 3fr;
    margin-top:0.5em;
    padding: 0.2em
}
.input_plate{
    margin-bottom:0.3em;
    margin-right:0.1em;
}
p{
    text-align:left
}
button{
    margin-top:1em
}
</style>