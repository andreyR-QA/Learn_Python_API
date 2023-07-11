import allure
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

@allure.epic("Get user details cases")
class TestUserGet(BaseCase):
    @allure.title("Get user details without authorisation")
    @allure.description("This test checks response user attributes without authorisation")
    @allure.link("https://github.com/andreyR-QA/Learn_Python_API/blob/main/tests/test_user_get.py",
                 name="<--Click to view code on GitHub")
    def test_get_user_details_if_not_auth(self):
        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    @allure.title("Get user details with authorisation")
    @allure.description("This test checks authorised user attributes")
    @allure.link("https://github.com/andreyR-QA/Learn_Python_API/blob/main/tests/test_user_get.py",
                 name="<--Click to view code on GitHub")
    def test_get_user_details_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data = data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                 headers={"x-csrf-token": token},
                                 cookies = {"auth_sid": auth_sid}
                                 )

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)


    #  ---- Ex16: Запрос данных другого пользователя ----
    # Запрос данных пользователя с данными другого
    @allure.title("Get user details with wrong authorisation parameters")
    @allure.description("This test checks user attributes making request with another user authorisation parameters")
    @allure.link("https://github.com/andreyR-QA/Learn_Python_API/blob/main/tests/test_user_get.py",
                 name="<--Click to view code on GitHub")
    def test_get_user_data_without_auth(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response3 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")
                # тянем куки и хедэры из запроса авторизации
        cookies = {'auth_sid': auth_sid}
        headers = {'x-csrf-token': token}
        # передаем куки и хедэры из запроса авторизации в запрос данных другого пользователя

        response4 = MyRequests.get("/user/1", cookies=cookies, headers=headers)

        Assertions.assert_code_status(response4, 200)               # сначала проверяем, что такой пользователь существует
        Assertions.assert_json_has_key(response4, "username")
        Assertions.assert_json_has_not_key(response4, "id")
        Assertions.assert_json_has_not_key(response4, "email")
        Assertions.assert_json_has_not_key(response4, "firstName")
        Assertions.assert_json_has_not_key(response4, "lastName")