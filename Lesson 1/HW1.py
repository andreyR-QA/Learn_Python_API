from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")

print(response.text)        #выводим текстовый ответ
try:
    parsed_response_text = response.json()
    print(parsed_response_text['answer'])          # пробуем распарсить ответ если он json
except JSONDecodeError:
    #print("Response is not a JSON format")      # если отрабатывает JSONDecodeError, то выводим ошибку
    print(response.text)