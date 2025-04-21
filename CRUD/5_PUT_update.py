import json
import requests


h_content = {'Content-Type': 'application/json'}
analys = {
               "id": 3,
               "title": "Cortisol",
               "price": 40
             }

try:
    put_reply = requests.put('http://localhost:3000/analysis/3', headers=h_content, data=json.dumps(analys))
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + put_reply.headers['Connection'])
    if put_reply.status_code == requests.codes.ok:
        get_reply = requests.get('http://localhost:3000/analysis')
        print(get_reply.text)
    else:
        print('Server error')


"""
Connection=keep-alive
[
  {
    "id": "1",
    "title": "COVID",
    "price": 35
  },
  {
    "id": "2",
    "title": "Allergy",
    "price": 25
  },
  {
    "id": "3",
    "title": "Cortisol",
    "price": 40
  },
  {
    "id": 4,
    "title": "DNA",
    "price": 80
  }
]
"""
