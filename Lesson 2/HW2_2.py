# _____ task #2 ______
import requests
print('---- LESSON 2 ----')
print ('_____ task #2 ______')
response = requests.get('https://playground.learnqa.ru/api/long_redirect')
last_response = response
history = response.history

print('Last redirect url is: ', last_response.url)
print('Redirect count: ', len(history)+1)

