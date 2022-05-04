import sqlite3
import json


class Menu:
    def __init__(self, id, date, desc, id_restaurant):
        self.id = id
        self.date = date
        self.desc = desc
        self.id_restaurant = id_restaurant

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "desc": self.desc,
            "id_restaurant": self.id_restaurant,
        }


class MenuRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE table if not exists menus (
                id varchar,
                date varchar,
                desc varchar,
                id_restaurant varchar,
                FOREIGN KEY (id_restaurant) REFERENCES restaurants(id_restaurant)
                ON DELETE  CASCADE)"""

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def search_by_id_restaurant(self, id_restaurant):
        sql = """SELECT * FROM menus WHERE id_restaurant=:id_restaurant ORDER BY date DESC"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id_restaurant": id_restaurant})
        data = cursor.fetchall()
        dict_menu = []
        for item in data:
            menu_class = Menu(
                id=item["id"],
                date=item["date"],
                desc=json.loads(item["desc"]),
                id_restaurant=item["id_restaurant"],
            )
            dict_menu.append(menu_class)
        return dict_menu

    def get_by_id(self, id):
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM menus WHERE id =?""", (id,))
        data = cursor.fetchone()
        menu_class = Menu(
            id=data["id"],
            date=data["date"],
            desc=json.loads(data["desc"]),
            id_restaurant=data["id_restaurant"],
        )
        return menu_class

    def get_by_date(self, date):
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM menus WHERE date =?""", (date,))
        data = cursor.fetchone()
        menu_class = Menu(
            id=data["id"],
            date=data["date"],
            desc=json.loads(data["desc"]),
            id_restaurant=data["id_restaurant"],
        )
        return menu_class

    def save(self, menu):
        sql = """INSERT INTO menus (id,date, desc, id_restaurant) VALUES (
            :id,:date, :desc, :id_restaurant
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "id": menu.id,
                "date": menu.date,
                "desc": json.dumps(menu.desc),
                "id_restaurant": menu.id_restaurant,
            },
        )
        conn.commit()

    def modify_a_menu(self, menu):
        sql = """UPDATE menus SET desc = :desc 
             WHERE id = :id AND id_restaurant = :id_restaurant"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "id": menu.id,
                "date": menu.date,
                "desc": json.dumps(menu.desc),
                "id_restaurant": menu.id_restaurant,
            },
        )
        conn.commit()
