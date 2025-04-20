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

Run a command for prepared _analysis.json_ file:

```
json-server --watch analysis.json
```

Open the link in browser:

![image](https://github.com/user-attachments/assets/6c3f4da2-90c2-42db-af44-5fa65d561247)


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
# {'X-Powered-By': 'tinyhttp', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, HEAD, PUT, PATCH, POST, DELETE', 'Access-Control-Allow-Headers': 'content-type', 'Content-Type': 'text/html; charset=utf-8', 'etag': 'W/"65a-+P0/CMY3BsvQjKCFt17lXwJJTHU"', 'Date': 'Tue, 15 Apr 2025 17:37:39 GMT', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=5', 'Content-Length': '1626'}
```

```
print(reply.text)
```
The response:
```
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    html {
      font-size: 16px;
      line-height: 1.5;
      background-color: #fff;
      color: #000;
    }

    body {
      margin: 0 auto;
      max-width: 720px;
      padding: 0 16px;
      font-family: sans-serif;
    }

    a {
      color: #db2777;
      text-decoration: none;
    }

    header {
      margin-bottom: 32px;
      padding: 16px 0;
    }

    nav {
      display: flex;
      justify-content: space-between;
    }

    nav div a {
      margin-left: 16px;
    }

    ul {
      margin: 0;
      padding: 0;
      list-style: none;
    }

    li {
      margin-bottom: 8px;
    }

    /* Dark mode styles */
    @media (prefers-color-scheme: dark) {
      html {
        background-color: #1e293b;
        color: #fff;
      }

      a {

      }
    }

  </style>
</head>

<body>
  <header>
    <nav>
      <strong>JSON Server</strong>
      <div>
        <a href="https://github.com/typicode/json-server">Docs</a>
        <a href="https://github.com/sponsors/typicode">♡ Sponsor</a>
      </div>
    </nav>
  </header>
  <main class="my-12">
    <p class="bg-gradient-to-r from-purple-500 via-pink-500 to-red-500 text-transparent bg-clip-text">✧*｡٩(ˊᗜˋ*)و✧*｡</p>
              <ul>
        <li>
          <a href="title">/title</a>
          <span>
                    </li>
      </ul>
          <ul>
        <li>
          <a href="price">/price</a>
          <span>
                    </li>
      </ul>
      </main>
</body>

</html>
```

