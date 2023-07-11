# --- Ex18: Тесты на DELETE ----
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import time

class TestUserDelete(BaseCase):
    def test_delete_user_2_without_auth(self):                      # тест на удаление без авторизации
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = MyRequests.delete("/user/2", data=data)

        Assertions.assert_code_status(response, 400)

    def test_delete_authorised_user(self):                          # тест на удаление созданного пользователя
        data = self.prepare_registration_data()

        response1 = MyRequests.post("/user/", data=data)                    # Регистрация

        user_id = self.get_json_value(response1, 'id')
        auth_data = {
            'email': data['email'],
            'password': '123'
        }

        response2 = MyRequests.post("/user/login", data=auth_data)          # Авторизация

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
                                                                                # тянем куки и хедэры из запроса авторизации
        cookie = {'auth_sid': auth_sid}
        token = {'x-csrf-token': token}
                                                                                # передаем куки и хедэры из запроса авторизации в запрос удаления
        response3 = MyRequests.delete(f"/user/{user_id}", cookies=cookie, headers=token)

        Assertions.assert_code_status(response3, 200)                           # проверяем успешность удаления

        response4 = MyRequests.get(f"/user/{user_id}", cookies=cookie, headers=token)

        Assertions.assert_code_status(response4, 404)                           # проверяем что пользователь не найден
        Assertions.assert_response_match_content(response4, "User not found")

    def test_delete_another_authorised_user(self):                          # тест на удаление с авторизацией другого поьзователя
        data_first = self.prepare_registration_data()

        response_first = MyRequests.post("/user/", data=data_first)             # Регистрация первого пользователя
        user_first_id = self.get_json_value(response_first, 'id')
        first_auth_data = {
            'email': data_first['email'],
            'password': '123'
        }
        print(data_first['email'])
        print(response_first.text)
        print(user_first_id)

        time.sleep(1)                                                           # добавил задержку, т.к. пару раз ловил ошибку когда сгенерились одинаковые имэйлы
        data_second = self.prepare_registration_data()

        response_second = MyRequests.post("/user/", data=data_second)           # Регистрация второго пользователя
        user_second_id = self.get_json_value(response_second, 'id')

        print(response_second.text)
        print(user_second_id)

        response_auth = MyRequests.post("/user/login", data=first_auth_data)    # Авторизация первым пользователем
        auth_sid = self.get_cookie(response_auth, "auth_sid")
        token = self.get_header(response_auth, "x-csrf-token")
                                                                                # тянем куки и хедэры из запроса авторизации
        cookie = {'auth_sid': auth_sid}
        token = {'x-csrf-token': token}
                                                                                # передаем куки и хедэры из запроса авторизации в запрос удаления
        response_delete = MyRequests.delete(f"/user/{user_second_id}", cookies=cookie, headers=token)
        print(response_delete.url)
        print(response_delete.json)
        print(response_delete.status_code)
        Assertions.assert_code_status(response_delete, 400)                     # запрос должен вернуть ошибку, но удаялется тот пользователь, с чьими куками выполнен запрос и потому возвращает статус 200