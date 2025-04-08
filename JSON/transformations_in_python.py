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

json.JSONEncoder class -> part of the json module, which provides methods to serialize Python objects into JSON-encoded strings. 
"""
import json


# Example for serialization
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

# Result: {"name": "Red Tourist Bus", "width": 4, "height": 5, "weight": 20}


# Example for json.JSONEncoder class
class VehicleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Vehicle):
            return {"name": obj.name,
                    "width": obj.width,
                    "height": obj.height,
                    "weight": obj.weight}
        # Call the base class method for other types
        return super().default(obj)


# Example Usage
data = [
    Vehicle("Bus", 4, 5, 20),
    Vehicle("Plane", 10, 5, 30)
]

json_data = json.dumps(data, cls=VehicleEncoder, indent=2)
print(json_data)

"""
[
  {
    "name": "Bus",
    "width": 4,
    "height": 5,
    "weight": 20
  },
  {
    "name": "Plane",
    "width": 10,
    "height": 5,
    "weight": 30
  }
]
"""
