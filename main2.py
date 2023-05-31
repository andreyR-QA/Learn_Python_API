import requests

response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
#print(response1.text)
#print("Код ответа: ", response1.status_code)

first_response = response.history[0]
second_response = response

print(first_response.url)
print(second_response.url)
print(response.status_code)
print(response.text)