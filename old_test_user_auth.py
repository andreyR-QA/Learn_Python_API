import requests
import pytest
import allure

@allure.epic("Authorisation caese")
class TestUserAuth:
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]
    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response1.cookies, "No cookies"
        assert "x-csrf-token" in response1.headers, "No CSRF token"
        assert "user_id" in response1.json(), "Тo user_id in JSON"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_from_auth_method = response1.json()["user_id"]

    @allure.description("This test successfully authorise user by email and password")
    def test_auth_user(self):

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers = {"x-csrf-token": self.token},
            cookies = {"auth_sid": self.auth_sid}
        )

        assert "user_id" in response2.json(), "No user_id in 2nd response"
        user_id_from_check_method = response2.json()["user_id"]
        print("user_id_from_check_method:", user_id_from_check_method)

        assert self.user_id_from_auth_method == user_id_from_check_method, "User_id from auth is not equal to check"

    @allure.description("Checks authorisation status w/o sending auth cookie or token")
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_test(self, condition):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        if condition == "no_cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers = {"x-csrf-token": self.token}
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies= {"auth_sid": self.auth_sid}
            )

        assert "user_id" in response2.json(), "No user_id in 2nd response"

        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_check_method == 0, f"User is authorized with condition {condition}"
