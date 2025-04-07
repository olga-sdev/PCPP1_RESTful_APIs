"""
Serialization and deserialization are processes used to:
1. transform Python objects into a format that can be saved to a file, 
2. transferred over a network, or stored in a database, and then 
3. reconstruct them back into their original form.

Serialization -> converts Python objects into a byte stream or a text format (such as JSON or pickle) for saving data or sending it over a network: json.dumps(data)

Deserialization -> converts serialized data back into Python objects for reading saved data or receiving it over a network: json.loads(data)

TypeError when converting objects to JSON in Python usually happens in case of serializing an unsupported data type.
The json module can handle dictionaries, lists, strings, numbers, booleans, and None, 
but complex objects like custom classes require special handling.
"""
import json


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


bus = Vehicle('Red Tourist Bus', 4, 5, 20)
print(json.dumps(bus, default=encode_vehicle_to_dict))
