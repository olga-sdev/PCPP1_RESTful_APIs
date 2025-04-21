Downlaod Node.js from https://nodejs.org/en/download
Install it and check version:

```
npm -v
```

Install json-server

```
npm install -g json-server
```

Run a command for prepared _analys.json_ file:

```
json-server --watch analys.json
```

Open the link in browser:

![image](https://github.com/user-attachments/assets/a3b71247-feda-47db-b537-96552f4a450e)



Check the assertions for requests lib in python -> expected successfull result:

```
import requests
import pprint

reply = requests.get('http://localhost:3000')
assert reply.status_code == requests.codes.ok
```

The list of codes:
```
pprint.pprint(requests.codes.__dict__)
```

The server's response consists of two parts: the header and the contents.

```
print(reply.headers)
```

```
print(reply.text)
```


