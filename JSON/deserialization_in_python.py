"""
Deserialization -> converts serialized data back into Python objects for reading saved data or receiving it over a network: json.loads(data)

In Python, the object_hook parameter in json.loads() allows to customize the deserialization of JSON objects into Python objects. 
It can be used it convert JSON dictionaries into instances of a custom class.

From https://docs.python.org/3/library/json.html#basic-usage
object_hook (callable | None) – If set, a function that is called with the result of any object literal decoded (a dict). 
The return value of this function will be used instead of the dict. 
This feature can be used to implement custom decoders, for example JSON-RPC class hinting. Default None.
"""
import json


jstr = '"\\"Python Tricks\\" by Dan Bader"'
book = json.loads(jstr)
print(type(book))
print(book)

# <class 'str'>
# "Python Tricks" by Dan Bader


# Example for deserialization
class Vehicle:
    def __init__(self, name, width, height, weight):
        self.name = name
        self.width = width
        self.height = height
        self.weight = weight


def encode_vehicle_to_dict(obj):
    if isinstance(obj, Vehicle):
        return obj.__dict__
    raise TypeError(f'Object of type {type(obj).__name__} is not JSON serializable')


def decode_vehicle(obj):
    return Vehicle(obj['name'], obj['width'], obj['height'], obj['weight'])


bus = Vehicle('Red Tourist Bus', 4, 5, 20)
json_bus = json.dumps(bus, default=encode_vehicle_to_dict)
new_bus = json.loads(json_bus, object_hook=decode_vehicle)
print(type(new_bus))
print(new_bus.__dict__)

# <class '__main__.Vehicle'>
# {'name': 'Red Tourist Bus', 'width': 4, 'height': 5, 'weight': 20}
