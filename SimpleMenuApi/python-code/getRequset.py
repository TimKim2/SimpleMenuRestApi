import requests
from pprint import pprint
import json

URL = 'http://127.0.0.1:8000/api/store?key_number=2'

req = requests.get(URL)

#pprint(req.text)

json_data = json.loads(req.text)

print(json_data)


#print(json_data[0]['name'])

#new_json = json.loads(json_data[16]['menu'])
'''
print(json_data)
a = []

a = (json_data[19]['menu'])

c = a.replace("'", "\"")

b = json.loads(c)

#print(b[0]['name'])
'''


