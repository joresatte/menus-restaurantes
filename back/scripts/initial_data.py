import sys

sys.path.insert(0, "")
from src.domain.Menu import MenuRepository, Menu
from src.example_menu import dict_menu, dict_menu_2, dict_menu_3
from src.domain.Restaurant import RestaurantRepository, Restaurant


database_path = "data/database.db"
menu_repository = MenuRepository(database_path)

menu_repository.save(
    Menu(id="MM", date="2022-01-03", desc=dict_menu, id_restaurant="0001")
)

menu_repository.save(
    Menu(id="MT", date="2022-02-03", desc=dict_menu_2, id_restaurant="0001")
)

menu_repository.save(
    Menu(id="MX", date="2022-03-03", desc=dict_menu_3, id_restaurant="0002")
)


restaurante_repository = RestaurantRepository(database_path)
restaurante_repository.save_restaurants(
    Restaurant(id_restaurant="0001", name="Tia Maruca")
)
restaurante_repository.save_restaurants(
    Restaurant(id_restaurant="0002", name="Don Satur")
)
