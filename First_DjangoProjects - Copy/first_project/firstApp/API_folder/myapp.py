import requests
import json

"""""
URL = "http://127.0.0.1:8000/att/stuinfo/5"
r = requests.get(url = URL)
data = r.json()
print(data)
"""""
def get_Data():  #sending json data to api
    URL = "http://127.0.0.1:8000/att/stuapi/"
    data = {'id':7}  #this dictionary 
    jsondata = json.dumps(data)  # dict converts into jsondata
    print("$$$$",jsondata)
    r = requests.get(url=URL,data=jsondata)
    data = r.json()
    print(data)
#get_Data()

def post_Data():
    URL = "http://127.0.0.1:8000/att/stuapi/"
    data = {'stuid':200,'stuname':'enter','stumail':'enter@gmail.com','stuclass':'1'}
    jsondata = json.dumps(data)
    print("&&&&",jsondata)
    r = requests.post(url=URL,data=jsondata)
    data = r.json()
    print(data)
#post_Data()

def put_Data():   #complete update , patch update parsel
    URL = "http://127.0.0.1:8000/att/stuapi/"
    data = {'stuid':200,'stuname':'enter','stumail':"enter@gmail.com",'stuclass':"1"}
    jsondata = json.dumps(data)
    print("&&&&",jsondata)
    r = requests.post(url=URL,data=jsondata)
    data = r.json()
    print(data)
#put_Data()

def delete_Data():  #sending json data to api
    URL = "http://127.0.0.1:8000/att/stuapi/"
    data = {'id':1}  #this dictionary 
    jsondata = json.dumps(data)  # dict converts into jsondata
    print("$$$$",jsondata)
    r = requests.delete(url=URL,data=jsondata)
    data = r.json()
    print(data)
delete_Data()