import requests
import json
from time import sleep
#for i in range(1000):

#Create user
if input("Create user? ") == "yes":
   q = requests.post("http://127.0.0.1:8000/main_back/create/",headers = {'Content-Type' : 'application/json'}, data=json.dumps({ "user_id" : "cdf","name" : "Filip", "last_name" : "Jovanov", "lat" : "41.978837", "lon" : "21.473843", "type" : "driver" }))

   print( "%s" %(q) + " Received: %s" % (str(q.text)))

#"lon" : "41.978412", "lat" : "21.472048"

#Add Region
if input("Add Region? ") == "yes":
   p = requests.post("http://127.0.0.1:8000/main_back/find_region/",headers = {'Content-Type' : 'application/json'}, data=json.dumps({  "user_id" : "cdf","name" : "Filip", "last_name" : "Jovanov", "lat" : "42.033381", "lon" : "21.377907", "type" : "driver" }))

   print( "%s" %(p) + " Received: %s" % (str(q.text)))

#Change mode
if input("Change mode?") == "yes":
   z = requests.post("http://127.0.0.1:8000/main_back/change/",headers = {'Content-Type' : 'application/json'}, data=json.dumps({  "user_id" : "cdf","name" : "Filip", "last_name" : "Jovanov", "lat" : "42.063776", "lon" : "21.452788", "type" : "driver" }))

   print( "%s" %(z) + " Received: %s" % (str(q.text)))


'''
payload = {"id" : "%s" % (str(q.text)), "good_choices" : "3", "neutral_choices" :"2", "bad_choices" : "1" }
url = 'http://51.68.174.56:8001/back_end/id_check/'
headers = {'Content-Type' : 'application/json'}
for i in range(10000):
   r = requests.post(url, headers=headers, data = json.dumps(payload))
   print( "%s Req-num:%s" %(r,i) + '  ID: %s' % (q.text) + " Received: %s" % (str(r.text)))
'''