from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.Menu import MenuRepository


def test_should_return_forbidden():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()

    body = {
        "id": "01",
        "date": "2022-03-03",
        "desc": {
            "id_dish": "01",
            "name_dish": "Ensalada mixta",
            "desc_dish": "Ensalada con cebolla",
        },
        "id_restaurant": "11",
    }

    wrong_headers = {"Authorization": "12121212"}
    forbidden_response = client.post("/api/menus", headers=wrong_headers, json=body)

    assert forbidden_response.status_code == 403
