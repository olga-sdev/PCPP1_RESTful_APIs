"""
Deserialization -> converts serialized data back into Python objects for reading saved data or receiving it over a network: json.loads(data)
"""
import json


jstr = '"\\"Python Tricks\\" by Dan Bader"'
book = json.loads(jstr)
print(type(book))
print(book)

# <class 'str'>
# "Python Tricks" by Dan Bader
