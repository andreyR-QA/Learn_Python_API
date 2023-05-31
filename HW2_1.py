# _____ task #1 ______
import json

print('---- LESSON 2 ----')
json_text= '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)
messages = obj["messages"]

print ('_____ task #1 ______')
print(messages[1])
