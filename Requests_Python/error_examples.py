"""
requests.exceptions.Timeout -> raise in case of timeout exceeded

requests.exceptions.ConnectionError -> can happen due to: network issues, incorrect URL, or proxy settings

requests.exceptions.InvalidURL

The list of Errors:

RequestException
|___HTTPError
|___ConnectionError
|   |___ProxyError	
|   |___SSLError	
|___Timeout
|   |___ConnectTimeout
|   |___ReadTimeout
|___URLRequired
|___TooManyRedirects
|___MissingSchema
|___InvalidSchema
|___InvalidURL
|   |___InvalidProxyURL
|___InvalidHeader
|___ChunkedEncodingError
|___ContentDecodingError
|___StreamConsumedError
|___RetryError
|___UnrewindableBodyError

"""

# Example with Timeout
import requests


try:
    response = requests.get('http://localhost:3000/price', timeout=1)
except requests.exceptions.Timeout:
    print('Timeout was exceeded. No data will be returned')
else:
    print(f'The request returns {response.status_code}')

#  The request returns 200


# Example with ConnectionError
try:
    response = requests.get('http://localhost:3333/price', timeout=1)
except requests.exceptions.ConnectionError:
    print('Connection error has happened')
else:
    print(f'The request returns {response.status_code}')

#  Connection error has happened


# Example with 404 error
try:
    response = requests.get('http://localhost:3000/name')
except requests.exceptions.InvalidURL:
    print('Check the requested URL. It might be broken')
else:
    print(f'The request returns {response.status_code}')

# The request returns 404


# Example with InvalidURL
try:
    response = requests.get('http:///localhost:3000/name')
except requests.exceptions.InvalidURL:
    print('Check the requested URL. It might be broken')
else:
    print(f'The request returns {response.status_code}')


#  Check the requested URL. It might be broken
