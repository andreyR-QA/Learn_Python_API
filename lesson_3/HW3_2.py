'''---Ex11: Тест запроса на метод cookie---'''
import requests

class TestCheckCookies:

    def test_get_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookies = response.cookies
        print('Сookies:', cookies)
        cookie_name = 'HomeWork'
        cookie_value = response.cookies.get(cookie_name)
        print('Cookie name', cookie_name)
        print('Cookie value:', cookie_value)
        assert cookie_name in response.cookies, f"Can not find cookie with name {cookie_name} in the last response"
        assert cookie_value == 'hw_value', f'Cookie value is incorrect. Expected cookie value is {cookie_value}'