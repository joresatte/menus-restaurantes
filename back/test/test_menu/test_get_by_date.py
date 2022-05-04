from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.Menu import Menu, MenuRepository


def test_should_return_one_menu_by_date():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()

    plate_01 = Menu(
        id="ML", date="2022-01-03", desc="Pollo con patatas", id_restaurant="11"
    )
    plate_02 = Menu(
        id="MM",
        date="2022-10-15",
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
    menu_repository.save(plate_01)
    menu_repository.save(plate_02)
    headers = {"Authorization": "0001"}
    # ACT (when)
    response = client.get("/api/menus/by-date/2022-10-15", headers=headers)
    # ASSERT (then)
    assert response.json == {
        "id": "MM",
        "date": "2022-10-15",
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
    }


def test_should_return_forbidden():
    menu_repository = MenuRepository(temp_file())
    app = create_app(repositories={"menu": menu_repository})
    client = app.test_client()

    plate_01 = Menu(
        id="ML", date="2022-01-03", desc="Pollo con patatas", id_restaurant="11"
    )
    plate_02 = Menu(
        id="MM",
        date="2022-10-15",
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
    menu_repository.save(plate_01)
    menu_repository.save(plate_02)
    headers = {"Authorization": "0000"}
    # ACT (when)
    response = client.get("/api/menus/by-date/2022-10-15", headers=headers)
    # ASSERT (then)
    assert response.status_code == 403
