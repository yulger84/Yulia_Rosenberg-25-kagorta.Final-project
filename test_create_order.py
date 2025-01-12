import requests
import config
import data


def create_new_order(first_name):
    response = requests.post(config.URL_SERVICE + config.CREATE_ORDER,
                                 json=get_order_body(first_name),
                                 headers=data.headers)
    assert response.status_code == 201, "Ошибка при создании нового заказа"
    return response.json()["track"]

def get_order(track):
    response = requests.get(config.URL_SERVICE + config.GET_ORDERS_BY_TRACK + str(track),
                            json={},
                            headers=data.headers)
    assert response.status_code == 200, "Ошибка при поиске заказа"
    return response

def get_order_body(first_name):
    current_body = data.create_order_body.copy()
    # изменение значения в поле firstName
    current_body["firstName"] = first_name
    return current_body

def test_create_order():
    track = create_new_order("Vadim")
    get_order(track)
