from src.lib.utils import temp_file
from src.webserver import create_app


from src.domain.Restaurant import Restaurant, RestaurantRepository


def test_should_return_empty_list():
    restaurant_repository = RestaurantRepository(temp_file())
    app = create_app(repositories={"restaurant": restaurant_repository})
    client = app.test_client()
    response = client.get("/api/restaurants")
    assert response.json == []


# ----------------------------------------------------------------


def test_should_return_list_of_restaurants():
    restaurant_repository = RestaurantRepository(temp_file())
    app = create_app(repositories={"restaurant": restaurant_repository})
    client = app.test_client()
    restaurant = Restaurant("restaurant_01", "Tía Maruca")
    restaurant1 = Restaurant(id_restaurant="restaurant_02", name="Don Satur")

    restaurant_repository.save_restaurants(restaurant)
    restaurant_repository.save_restaurants(restaurant1)

    response = client.get("/api/restaurants")

    assert response.json == [
        {"id_restaurant": "restaurant_01", "name": "Tía Maruca"},
        {"id_restaurant": "restaurant_02", "name": "Don Satur"},
    ]
