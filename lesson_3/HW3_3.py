'''---Ex12: Тест запроса на метод header---'''
import requests

class TestCheckHeader:

    def test_get_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        headers = response.headers
        print(headers)
        header_name = 'x-secret-homework-header'
        header_value = response.headers.get(header_name)
        print('Header name:', header_name)
        print('Header value:', header_value)
        assert header_name in response.headers, f"Can not find cookie with name {header_name} in the last response"
        assert header_value == 'Some secret value', f'Header value is incorrect. Expected header value is {header_value}'
