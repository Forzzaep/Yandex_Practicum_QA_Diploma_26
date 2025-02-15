import requests
import configuration
import data

# Функция для создания заказа
def post_new_order():
    
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.ORDER_BODY,
                         headers=data.HEADERS)

# Функция для получения заказа по трек-номеру
def get_order_by_track(track):

    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO,
                        params={'t': track},
                        headers=data.HEADERS)