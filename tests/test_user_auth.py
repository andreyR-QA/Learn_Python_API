import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure
@allure.epic("Authorisation cases")
class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]
    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    @allure.title('Successful authorisation')
    @allure.description("This test successfully authorise user by email and password")
    @allure.link("https://github.com/andreyR-QA/Learn_Python_API/blob/main/tests/test_user_auth.py",
                 name="<--Click to view code on GitHub")
    def test_auth_user(self):

        response2 = MyRequests.get(
            "/user/auth",
            headers = {"x-csrf-token": self.token},
            cookies = {"auth_sid": self.auth_sid}
        )
        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )

    @allure.title('Negative authorisation test')
    @allure.description("This test checks authorisation status w/o sending auth cookie or token")
    @allure.link("https://github.com/andreyR-QA/Learn_Python_API/blob/main/tests/test_user_auth.py",
                 name="<--Click to view code on GitHub")
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_test(self, condition):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        if condition == "no_cookie":
            response2 = MyRequests.get(
                "/user/auth",
                headers = {"x-csrf-token": self.token}
            )
        else:
            response2 = MyRequests.get(
                "/user/auth",
                cookies= {"auth_sid": self.auth_sid}
            )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"User is authorised with conditions'{condition}"
        )
