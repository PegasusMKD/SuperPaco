import requests
import json

payload = {"id" : "¸3=>C38,3<38,3<38,3=3i4", "good_choices" : "3", "neutral_choices" : "5", "bad_choices" : "1" }
url = 'http://127.0.0.1:8000/back-end/id-check/'
headers = {'Content-Type' : 'application/json'}

r = requests.post(url, headers=headers, data = json.dumps(payload))