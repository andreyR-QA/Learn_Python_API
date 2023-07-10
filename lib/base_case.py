import json.decoder
from datetime import datetime
from requests import Response
import random
import string


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Can not find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Can't find header with name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON Format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON does not have key '{name}'"

        return response_as_dict[name]

    def prepare_registration_data(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }


    def prepare_incorrect_email(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}{domain}"
        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }


    def prepare_registration_data_missing_params(self, exclude_param=None, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"

        if exclude_param == 'password':
            return {'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': email}
        elif exclude_param == 'username':
            return {'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': email}
        elif exclude_param == 'firstName':
            return {'password': '123', 'username': 'learnqa', 'lastName': 'learnqa', 'email': email}
        elif exclude_param == 'lastName':
            return {'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'email': email}
        elif exclude_param == 'email':
            return {'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'}
        print(email)

    def create_shortname_user(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        user_name = random.choice(string.ascii_letters)
        return {
            'password': '123',
            'username': user_name,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
    def create_longname_user(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        letters = string.ascii_lowercase                                        # определяем используемые симвволы
        user_name = ''.join(random.choice(letters) for i in range(251))         # джоиним в рандомном порядке 251 символ
        return {
            'password': '123',
            'username': user_name,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

    def create_limited_length_name_user(self, email=None):                      # проверяем граничное значение
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        letters = string.ascii_lowercase                                        # определяем используемые симвволы
        user_name = ''.join(random.choice(letters) for i in range(250))         # джоиним в рандомном порядке 250 символ
        return {
            'password': '123',
            'username': user_name,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }