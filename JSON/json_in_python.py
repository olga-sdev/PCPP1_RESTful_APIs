"""
json.dumps() -> convert a Python object (like a dictionary, list, or other data structure) into a JSON-formatted string.


"""
import json


dict_example = {'age': 45,
               'name': "Esmerald"}
print(json.dumps(dict_example))

# {"age": 45, "name": "Esmerald"}

list_example = [45, "Coggy"]
print(json.dumps(list_example))

# [45, "Coggy"]

tuple_example = ('Arial', 'bold')
print(json.dumps(tuple_example))

# ["Arial", "bold"]
