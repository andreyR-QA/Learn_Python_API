# _____ task #4 ______
import requests
import json
import time

print('---- LESSON 2 ----')
print ('_____ task #4 ______')
response0 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")     # создаем задачу
print(response0.text)
resp0_obj = json.loads(response0.text)
get_token = resp0_obj["token"]
get_seconds = resp0_obj["seconds"]

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params = {'token' : get_token})     # делаем запрос с токеном ДО завершения задачи
if response1.status_code == 200:
    print("It's OK, we are on time!")       # Если статус 200, то выводим сообщение, что успели
else: print('Status code is not 200')
print(response1, response1.text)
time.sleep(get_seconds+1)                   # Ждем пока завершится джоба

response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params = {'token' : get_token})
resp2_obj = json.loads(response2.text)
get_status = resp2_obj["status"]
get_result = resp2_obj["result"]
if response2.status_code == 200 and get_status == "Job is ready" and "result" in resp2_obj:     # Проверяем статус и наличие "resut" в ответе
    print(response2, response2.text)
else:
    print('No result...')



