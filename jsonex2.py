#Read a JSON file and display specific keys.

import json

with open("abc.json", "r") as file:
    content = json.load(file)
    print("Name:", content["Name"])
    print("Age:", content["Age"])
    print("City:", content["City"])
   

