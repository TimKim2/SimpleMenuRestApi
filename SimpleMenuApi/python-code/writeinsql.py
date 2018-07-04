import pandas as pd
from pandas import Series, DataFrame
import sqlite3
import requests
from sklearn.externals import joblib
from pprint import pprint
import json
import simplejson
from sqlobject import *






timeline_goods_list = joblib.load("timeline_goods_dump.dat")

json_list = []

print(len(timeline_goods_list))

'''
for i in timeline_goods_list:
    res = requests.get(i["img"])
    if res.status_code != 200:
        i["img"] = ''
'''

genre = []
name = []
image_url = []
product_url = []
list_start_hour = []
list_start_minute = []
org_price = []
price = []
end_time = []
list_cate = []
date = []
id_number = []

for i in timeline_goods_list:

    cate = None

    if i['cate1'] is None:
        cate = "None"
    elif i['cate1'] == "":
        cate = "None"
    else:
        cate = str(i['cate1'])

    start_time = i['start_time']
    start_hour = None
    start_minute = None

    start_hour = int(int(start_time) / 100)
    start_minute = int(start_time) % 100

    send_data = {
        "genre": str(i['genre2']),
        "name": str(i['name']),
        "image_url": str(i['img']),
        "product_url": str(i['url']),
        "start_hour": str(start_hour),
        "start_minute": str(start_minute),
        "org_price": str(i['org_price']),
        "price": str(i['price']),
        "end_time": str(i['end_time']),
        "cate": cate,
        "date": str(i['date']),
        "id_number": str(i['id']),
    }
    genre.append(send_data["genre"])
    name.append(send_data["name"])
    image_url.append(send_data["image_url"])
    product_url.append(send_data["product_url"])
    list_start_hour.append(send_data["start_hour"])
    list_start_minute.append(send_data["start_minute"])
    org_price.append(send_data["org_price"])
    price.append(send_data["price"])
    end_time.append(send_data["end_time"])
    list_cate.append(send_data["cate"])
    date.append(send_data["date"])
    id_number.append(send_data["id_number"])

    json_list.append(send_data)
    #print(simplejson.dumps(send_data))


con = sqlite3.connect("db.sqlite3")

'''
print(id)
print(genre)
raw_data = {'id': ['1'], 'genre': ['2'], 'name': ['3'], 'image_url': ['4'], 'product_url': ['4'],'start_hour': ['4'],
            'start_minute': ['4'], 'org_price': ['4'], 'price': ['4'], 'end_time': ['4'], 'cate': ['4'],
            'date': ['4'], 'id_number': ['4'], }
'''
raw_data = {'genre': genre, 'name': name, 'image_url': image_url, 'product_url': product_url, 'start_hour': list_start_hour,
            'start_minute': list_start_minute, 'org_price': org_price, 'price': price, 'end_time': end_time, 'cate': list_cate,
            'date': date, 'id_number': id_number, }

df = DataFrame(raw_data)

print(df)

df.to_sql('myapp_product', con, schema=None, if_exists='replace', index=True, index_label=None, chunksize=1000, dtype=None)

df = pd.read_sql("SELECT * FROM myapp_product", con, index_col=None)

print(df)