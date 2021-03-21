import json
import requests
from django.http import HttpResponse
from django.db import models
from uposts.models import Posts
from uposts.models import Company
from uposts.models import Geo
from uposts.models import Address
from uposts.models import Users



'''
#импорт тестовых данных с помощью python-request
url = 'http://jsonplaceholder.typicode.com/users'
data = requests.get(url)
#print(type(data.json()), data.json())

for x in data:
    b = (x)
    t1 = b["id"]
    t2 = b["name"]
    t3 = b["username"]
    t4 = b["email"]
    t5 = b["address"]
    t5_1 = b["address"]["street"]
    t5_2 = b["address"]["suite"]
    t5_3 = b["address"]["city"]
    t5_4 = b["address"]["zipcode"]
    t5_5 = b["address"]["geo"]
    t5_5_1 = b["address"]["geo"]["lat"]
    t5_5_2 = b["address"]["geo"]["lng"]
    t6 = b["phone"]
    t7 = b["website"]
    t8 = b["company"]
    t8_1 = b["company"]["name"]
    t8_2 = b["company"]["catchPhrase"]
    t8_3 = b["company"]["bs"]
    c = Company(name=t8_1, catchPhrase=t8_2, bs=t8_3)
    c.save()
    c_id=c.id
    g = Geo(lat=t5_5_1, lng=t5_5_2)
    g.save()
    g_id=g.id
    a = Address(street=t5_1, suite=t5_2, city=t5_3, zipcode=t5_4, geo_id=g_id)
    a.save()
    a_id=a.id
    u = Users(id=t1, name=t2, username=t3, email=t4, address_id=a_id, phone=t6, website=t7, company_id=c_id)
    u.save()




'''
'''
#импорт файла posts.json (локальный)
with open('C:/ddd/userpost/uposts/static/posts.json', 'r', encoding='utf-8') as fh:
	data = json.load(fh)

for x in data:
   b = (x)
   t1 = b["userId"]
   t2 = b["id"]
   t3 = b["title"]
   t4 = b["body"]
   p = Posts(id=t2,userId=t1,title=t3,body=t4)
   p.save()




#импорт users.json выполнен (локальный)
with open('C:/ddd/userpost/uposts/static/users.json', 'r', encoding='utf-8') as fh:
	data = json.load(fh)
	#print (type(data), data[1]) # class list

for x in data:
    b = (x)
   t1 = b["id"]
   t2 = b["name"]
   t3 = b["username"]
   t4 = b["email"]
   t5 = b["address"]
   t5_1 = b["address"]["street"]
   t5_2 = b["address"]["suite"]
   t5_3 = b["address"]["city"]
   t5_4 = b["address"]["zipcode"]
   t5_5 = b["address"]["geo"]
   t5_5_1 = b["address"]["geo"]["lat"]
   t5_5_2 = b["address"]["geo"]["lng"]
   t6 = b["phone"]
   t7 = b["website"]
   t8 = b["company"]
   t8_1 = b["company"]["name"]
   t8_2 = b["company"]["catchPhrase"]
   t8_3 = b["company"]["bs"]
   c = Company(name=t8_1, catchPhrase=t8_2, bs=t8_3)
   c.save()
   c_id=c.id
   g = Geo(lat=t5_5_1, lng=t5_5_2)
   g.save()
   g_id=g.id
   a = Address(street=t5_1, suite=t5_2, city=t5_3, zipcode=t5_4, geo_id=g_id)
   a.save()
   a_id=a.id
   u = Users(id=t1, name=t2, username=t3, email=t4, address_id=a_id, phone=t6, website=t7, company_id=c_id)
   u.save()

'''