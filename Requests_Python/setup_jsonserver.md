Downlaod Node.js from https://nodejs.org/en/download
Install it and check version:

```
npm -v
```

Install json-server

```
npm install -g json-server
```

![image](https://github.com/user-attachments/assets/e4bfd7ea-7aee-4f21-8427-aaeb2ca5f931)


Open the link in browser:

![image](https://github.com/user-attachments/assets/6c3f4da2-90c2-42db-af44-5fa65d561247)


Check the assertions for requests lib in python -> expected successfull result:

```
import requests

reply = requests.get('http://localhost:3000')
assert reply.status_code == 200
```
