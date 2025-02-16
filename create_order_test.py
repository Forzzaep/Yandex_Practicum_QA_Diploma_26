# Валентин Мельников, 26-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

def test_create_order_and_retrieve_order_info():
 
    create_order_response = sender_stand_request.post_new_order()

    assert create_order_response.status_code == 201

    order_track = create_order_response.json().get("track")

    retrieve_order_response = sender_stand_request.get_order_by_track(order_track)

    assert retrieve_order_response.status_code == 200