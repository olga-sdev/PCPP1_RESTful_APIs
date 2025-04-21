import json
import requests


try:
    del_reply = requests.delete('http://localhost:3000/analysis/1')
except requests.RequestException:
    print('Communication error')
else:
    print('Connection=' + del_reply.headers['Connection'])
    if del_reply.status_code == requests.codes.ok:
        get_reply = requests.get('http://localhost:3000/analysis')
        print(get_reply.text)
    elif del_reply.status_code == requests.codes.not_found:
        print("Resource not found")
    else:
        print('Server error')

"""
Connection=keep-alive
[
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
