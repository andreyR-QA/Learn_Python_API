'''---Ex13: User Agent---'''
''' Обращаемся  к классу Assertions '''

import requests
import pytest
from lib.assertions import Assertions

class TestCheckUserAgent:           # Определяем массив значений 'User Agent', которые удут передаватсья в запросе

    agents = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    @pytest.mark.parametrize('agent', agents)
    def test_get_params(self, agent):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        data = {"User-Agent": agent}

        response = requests.get(url, headers=data)

        assert response.status_code == 200, "Wrong response code"  # Проверяем не упал ли запрос


                # Проверяем значения возвращаетмых параметров, для компактности записи сделаны в одну строку
        if agent == "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30":
            print(agent)
            Assertions.assert_json_value_by_name(response, "platform", "Mobile", "'Platform' header is incorrect. Expected value is 'Mobile'")
            Assertions.assert_json_value_by_name(response, "browser", "No", "'Platform' header is incorrect. Expected value is 'Mobile'")
            Assertions.assert_json_value_by_name(response, "device", "Android", "'Device' header is incorrect. Expected value is 'Android'")
        elif agent == "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1":
            print(agent)
            Assertions.assert_json_value_by_name(response, "platform", "Mobile", "'Platform' header is incorrect. Expected value is 'Mobile'")
            Assertions.assert_json_value_by_name(response, "browser", "Chrome", "'Platform' header is incorrect. Expected value is 'Chrome'")
            Assertions.assert_json_value_by_name(response, "device", "iOS", "'Device' header is incorrect. Expected value is 'iOS'")
        elif agent == "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)":
            print(agent)
            Assertions.assert_json_value_by_name(response, "platform", "Googlebot", "'Platform' header is incorrect. Expected value is 'Googlebot'")
            Assertions.assert_json_value_by_name(response, "browser", "Unknown", "'Platform' header is incorrect. Expected value is 'Unknown'")
            Assertions.assert_json_value_by_name(response, "device", "Unknown", "'Device' header is incorrect. Expected value is 'Unknown'")
        elif agent == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0":
            print(agent)
            Assertions.assert_json_value_by_name(response, "platform", "Web", "'Platform' header is incorrect. Expected value is 'Web'")
            Assertions.assert_json_value_by_name(response, "browser", "Chrome", "'Platform' header is incorrect. Expected value is 'Chrome'")
            Assertions.assert_json_value_by_name(response, "device", "No", "'Device' header is incorrect. Expected value is 'No'")
        elif agent == "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1":
            print(agent)
            Assertions.assert_json_value_by_name(response, "platform", "Mobile", "'Platform' header is incorrect. Expected value is 'Mobile'")
            Assertions.assert_json_value_by_name(response, "browser", "No", "'Platform' header is incorrect. Expected value is 'Mobile'")
            Assertions.assert_json_value_by_name(response, "device", "iPhone", "'Device' header is incorrect. Expected value is 'iPhone'")
