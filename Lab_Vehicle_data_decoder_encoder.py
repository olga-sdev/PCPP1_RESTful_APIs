"""
Objectives
Learn how to:
use the json module and its basic facilities;
encode and decode JSON strings from/to Python objects.

Scenario
task is to write a code which has exactly the same conversation with the user and:

defines a class named Vehicle, whose objects can carry the vehicle data shown above (the structure of the class should be deducted from the above dialog — call it "reverse engineering" if you want)
defines a class able to encode the Vehicle object into an equivalent JSON string;
defines a class able to decode the JSON string into the newly created Vehicle object.

"""

import json


class Vehicle:
    def __init__(self, reg_number, prod_year, passenger, mass):
        self.reg_number = reg_number
        self.prod_year = prod_year
        self.passenger = passenger
        self.mass = mass


class VehicleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Vehicle):
            return {"reg_number": obj.reg_number,
                    "prod_year": obj.prod_year,
                    "passenger": obj.passenger,
                    "mass": obj.mass}
        # Call the base class method for other types
        return super().default(obj)


def decode_vehicle(obj):
    return Vehicle(obj['reg_number'], obj['prod_year'], obj['passenger'], obj['mass'])


if __name__ == "__main__":
    print('Select options:\n'
          '1 - data encoding\n'
          '2 - data decoding')
    choice = input("Your choice: ")

    if choice == "1":
        reg_number = input("Registration number: ")
        prod_year = input("Year of production: ")
        passenger = input("Passenger [y/n]: ")
        mass = input("Vehicle mass: ")
        data = Vehicle(reg_number, prod_year, passenger, mass)
        json_data = json.dumps(data, cls=VehicleEncoder, indent=2)
        print(f"Resulting JSON is:\n {json_data}")
    elif choice == "2":
        json_data = input("Enter JSON for decoding: ")
        new_data = json.loads(json_data, object_hook=decode_vehicle)
        print(new_data.__dict__)


"""
> python lab2.py
Select options:
1 - data encoding
2 - data decoding
Your choice: 1
Registration number: Bus1234
Year of production: 2020
Passenger [y/n]: n
Vehicle mass: 34
Resulting JSON is:
 {
  "reg_number": "Bus1234",
  "prod_year": "2020",
  "passenger": "n",
  "mass": "34"
}


> python lab2.py
Select options:
1 - data encoding
2 - data decoding
Your choice: 2
Enter JSON for decoding: {"reg_number": "Bus2345", "prod_year": 2020, "passenger": "n", "mass": 36}
{'reg_number': 'Bus2345', 'prod_year': 2020, 'passenger': 'n', 'mass': 36}

