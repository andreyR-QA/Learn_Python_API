import requests

payload = {"login" : "secret_login", "password":"secret_pass"}
response1 = requests.get("https://playground.learnqa.ru/api/get_auth_cookie", data = payload)

cookies_value = response1.cookies.get('auth_cookie')

cookies = {}
if cookies_value is not None:
    cookies.update ({'auth_cookie': cookies_value})

response2 = requests.get("https://playground.learnqa.ru/api/check_auth_cookie", cookies = cookies)

print(response2.text)
#print(response1.status_code)
#print(dict(response1.cookies))

#print(response1.headers)