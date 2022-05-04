<template>
<h2>{{loggedRestaurant}}</h2>
  <router-link :to="{ name: 'Menu', params: { date: getToday } }">
    <button class="menu-day">Menú del día</button>
  </router-link>
  <article class="calendar">
    <section class="name-month">
      <button class="button-last-month" @click="prevMonth">⬅</button>
      <h2 @click="comeBackCurrentMonth()">
        {{ nameMonths[this.currentMonth] }} {{ currentYear }}
      </h2>
      <button class="button-last-month" @click="nextMonth">➡</button>
    </section>
    <ul class="name-of-week">
      <li v-for="index in nameDaysOfWeek" :key="index">{{ index }}</li>
    </ul>
    <ul class="days-of-month">
      <li
        class="empty-list"
        v-for="i in initialPositionOfFirstDay"
        :key="i"
      ></li>
      <li
        @click="onClickDay(index)"
        v-for="index in daysOfMonthSelected"
        :key="index"
        class="not-empty-list"
        :class="{
          'underline-today':
            index === this.currentDay &&
            new Date().getMonth() === this.currentMonth,
        }"
      >
        {{ index }}
      </li>
    </ul>
  </article>

  <ul class="menu-date" v-for="menu in listOfMenus" :key="menu.id">
    <router-link :to="{ name: 'Menu', params: { date: menu.date } }">
      <li>{{ menu.date }}</li>
    </router-link>
  </ul>
</template>

<script>
import config from "@/config.js";
export default {
  data() {
    return {
      currentDay: new Date().getDate(),
      currentMonth: new Date().getMonth(),
      currentYear: new Date().getFullYear(),
      nameDaysOfWeek: ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
      nameMonths: [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
      ],
      listOfMenus: [],
      loggedRestaurant: localStorage.name
    };
  },

  mounted() {
    this.loadData();
  },
  computed: {
    getToday() {
      let current = new Date();
      let year = current.getFullYear();
      let month = current.getMonth() + 1;
      let day = current.getDate();
      if (day < 10) {
        day = "0" + day;
      }
      if (month < 10) {
        month = "0" + month;
      }

      const today = year + "-" + month + "-" + day;
      return today;
    },
    initialPositionOfFirstDay() {
      let initialDayWeek = new Date(
        this.currentYear,
        this.currentMonth,
        1
      ).getDay();
      if (initialDayWeek === 0) {
        return (initialDayWeek = 6);
      }
      let currentInitialDayweek = initialDayWeek - 1;
      return currentInitialDayweek;
    },
    daysOfMonthSelected() {
      let totaldays = new Date(
        this.currentYear,
        this.currentMonth + 1,
        0
      ).getDate();
      return totaldays;
    },
  },
  methods: {
    comeBackCurrentMonth() {
      let comebackMonth = new Date().getMonth();
      this.currentMonth = comebackMonth;
    },
    nextMonth() {
      this.currentMonth = this.currentMonth + 1;
      if (this.currentMonth > 11) {
        this.currentMonth = 11;
      }
    },
    prevMonth() {
      this.currentMonth -= 1;
      if (this.currentMonth < 0) {
        this.currentMonth = 0;
      }
    },
    onClickDay(day) {
      let month = this.currentMonth + 1;
      if (day < 10) {
        day = "0" + day
      }
      if (month < 10){
        month = "0" + month
      }
      const clickedDay = this.currentYear + "-" +day + "-" + month;
      const settings = {
        method: "GET",
        headers: {
          Authorization: localStorage.id_restaurant,
        },
      } 
      this.$router.push("/menus/by-date/" + clickedDay,settings)
    },
    async loadData() {
      const settings = {
        method: "GET",
        headers: {
          Authorization: localStorage.id_restaurant,
        },
      };
      console.log('Headers:',settings.headers)
      const response = await fetch(`${config.API_PATH}/menus`, settings);
      this.listOfMenus = await response.json();
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  font-size: 16px;
  box-sizing: border-box;
}
.menu-date {
  list-style: none;
  text-align: center;
  margin: 1em;
}

.calendar {
  width: 100%;
  max-width: 300px;
  margin: 2em auto;
}

.name-of-week {
  background: rgba(173, 216, 230, 0.74);
  margin: 0.2em 0;
  padding: 0.5em;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: 10px;
  align-items: center;
}
.days-of-month {
  font-size: 1rem;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-auto-rows: 40px;
}
.days-of-month > li {
  padding: 25% 25%;
}
.days-of-month > .empty-list {
  background: none;
}
.days-of-month > .not-empty-list:hover {
  font-size: 1.07rem;
  font-weight: bolder;
  color: darkblue;
  background-color: lightblue;
  border-radius: 50%;
  cursor: pointer;
}
.name-month {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.name-month > h2 {
  text-decoration: underline;
  cursor: pointer;
}
.button-last-month,
.button-next-month {
  width: 50px;
}

.underline-today {
  text-decoration: underline double;
}
.menu-day{
  margin-top:1em
}
</style>