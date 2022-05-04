from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.Menu import Menu, MenuRepository


def test_should_return_empty_list():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()
    response = client.get("/api/menus")
    assert response.json == []


# ----------------------------------------------------------------


def test_should_return_list_of_menus_by_id_restaurant():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()

    menu_restaurant_1 = Menu(
        id="01",
        date="2020-01-05",
        desc={
            "firsts": [
                {
                    "id_dish": "01",
                    "name_dish": "ensalada mixta",
                    "desc_dish": "ensalada con cebolla",
                }
            ]
        },
        id_restaurant="0001",
    )
    menu_restaurant_2 = Menu(
        id="02",
        date="2022-04-20",
        desc={
            "firsts": [
                {
                    "id_dish": "01",
                    "name_dish": "ensalada mixta",
                    "desc_dish": "ensalada con cebolla",
                }
            ]
        },
        id_restaurant="0002",
    )

    menu_repository.save(menu_restaurant_1)
    menu_repository.save(menu_restaurant_2)

    headers = {"Authorization": "0001"}
    response = client.get("/api/menus", headers={"Authorization": "0001"})

    assert response.json == [
        {
            "id": "01",
            "date": "2020-01-05",
            "desc": {
                "firsts": [
                    {
                        "id_dish": "01",
                        "name_dish": "ensalada mixta",
                        "desc_dish": "ensalada con cebolla",
                    }
                ]
            },
            "id_restaurant": "0001",
        },
    ]
