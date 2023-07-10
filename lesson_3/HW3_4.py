'''---Ex13: User Agent---'''
''' Без обращения к классам BaseCase и Assertions '''

import requests
import pytest
import json

class TestCheckUserAgent:           # Определяем массив значений 'User Agent', которые удут передаватсья в запросе

    agents = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]
    @pytest.mark.parametrize('agent', agents)
    def test_get_headers(self, agent):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        data = {"User-Agent": agent}

        response = requests.get(url, headers = data)

        assert response.status_code == 200, "Wrong response code"       # Проверяем не упал ли запрос

        response_obj = json.loads(response.text)                        # Парсим respone_body и далее выбираем нужные параметры

        response_platform = response_obj['platform']
        response_browser = response_obj['browser']
        response_device = response_obj['device']

                                                                        # Проверяем значения возвращаетмых параметров
        if agent == "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30":
            print(agent)
            assert response_platform == "Mobile", f"'Platform' header is incorrect. Expected value is 'Mobile'"
            assert response_browser == "No", f"'Browser' header is incorrect. Expected value is 'No'"
            assert response_device == "Android", f"'Device' header is incorrect. Expected value is 'Android'"
        elif agent == "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1":
            print(agent)
            assert response_platform == "Mobile", f"'Platform' header is incorrect. Expected value is 'Mobile'"
            assert response_browser == "Chrome", f"'Browser' header is incorrect. Expected value is 'Chrome'"
            assert response_device == "iOS", f"'Device' header is incorrect. Expected value is 'iOS'"
        elif agent == "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)":
            print(agent)
            assert response_platform == "Googlebot", f"'Platform' header is incorrect. Expected value is 'Googlebot'"
            assert response_browser == "Unknown", f"'Browser' header is incorrect. Expected value is 'Unknown'"
            assert response_device == "Unknown", f"'Device' header is incorrect. Expected value is 'Unknown'"
        elif agent == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0":
            print(agent)
            assert response_platform == "Web", f"'Platform' header is incorrect. Expected value is 'Web'"
            assert response_browser == "Chrome", f"'Browser' header is incorrect. Expected value is 'Chrome'"
            assert response_device == "No", f"'Device' header is incorrect. Expected value is 'No'"
        elif agent == "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1":
            print(agent)
            assert response_platform == "Mobile", f"'Platform' header is incorrect. Expected value is 'Mobile'"
            assert response_browser == "No", f"'Browser' header is incorrect. Expected value is 'No'"
            assert response_device == "iPhone", f"'Device' header is incorrect. Expected value is 'iPhone'"