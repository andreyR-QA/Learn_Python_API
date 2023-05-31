# _____ task #3 ______
import requests
print('---- LESSON 2 ----')
print ('_____ task #3 ______')
methods = ['GET', 'POST', 'PUT', 'DELETE']
response1 = requests.put(" https://playground.learnqa.ru/ajax/api/compare_query_type") # статус 200 и сообщение "Wrong method provided"
response2 = requests.head(" https://playground.learnqa.ru/ajax/api/compare_query_type", data = {'method':'HEAD'}) # статус 400, т.к. метод некорректный
response3 = requests.post(" https://playground.learnqa.ru/ajax/api/compare_query_type", data = {'method': 'POST'}) # статус 200 и сообщение {"success":"!"}

print(response1, response1.text)
print(response2, response2.text)
print(response3, response3.text)

i=0
while i < len(methods) :
        response_get = requests.get(" https://playground.learnqa.ru/ajax/api/compare_query_type", params = {'method': methods[i]})
        response_post = requests.post(" https://playground.learnqa.ru/ajax/api/compare_query_type", data = {'method' : methods[i]} )
        response_put = requests.put(" https://playground.learnqa.ru/ajax/api/compare_query_type", data = {'method' : methods[i]} )
        response_delete = requests.put(" https://playground.learnqa.ru/ajax/api/compare_query_type", data = {'method' : methods[i]})
        # print(i)
        #print(methods[i])
        #print(response_get, response_get.text,  response_post, response_post.text, response_put, response_put.text, response_delete, response_delete.text)

        if methods[i] != 'GET' and response_get.text == '{"success":"!"}':
                print ('Parameter "method" is', methods[i], ' and URL method is GET, but result is "', response_get.text,'"')
        elif methods[i] != 'POST' and response_post.text == '{"success":"!"}':
                print ('Parameter "method" is', methods[i], ' and URL method is POST, but result is "', response_post.text,'"')
        elif methods[i] != 'PUT' and response_put.text == '{"success":"!"}':
                print ('Parameter "method" is', methods[i], ' and URL method is PUT, but result is "', response_put.text,'"')
        elif methods[i] != 'DELETE' and response_delete.text == '{"success":"!"}':
                print('Parameter "method" is', methods[i], ' and URL method is DELETE, but result is "', response_delete.text,'"')

        if methods[i] == 'GET' and response_get.text != '{"success":"!"}':
                print ('Parameter "method" is', methods[i], ' and URL method is GET, but result is "', response_get.text,'"')
        elif methods[i] == 'POST' and response_post.text != '{"success":"!"}':
                print ('Parameter "method" is', methods[i], ' and URL method is POST, but result is "', response_post.text,'"')
        elif methods[i] == 'PUT' and response_put.text != '{"success":"!"}':
                print ('Parameter "method" is', methods[i], ' and URL method is PUT, but result is "', response_put.text,'"')
        elif methods[i] == 'DELETE' and response_delete.text != '{"success":"!"}':
                print('Parameter "method" is', methods[i], ' and URL method is DELETE, but result is "', response_delete.text,'"')
        i = i+1


