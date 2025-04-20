import json
import requests


h_content = {'Content-Type': 'application/json'}
new_analys = {
               "id": 4,
               "title": "DNA",
               "price": 80
             }

try:
    post_reply = requests.post('http://localhost:3000/analysis', headers=h_content, data=json.dumps(new_analys))
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + post_reply.headers['Connection'])
    if post_reply.status_code == requests.codes.created:
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
    "title": "ABC",
    "price": 40
  },
  {
    "id": 4,
    "title": "DNA",
    "price": 80
  }
]
"""
