#Convert a Python dictionary to JSON and write to a file.
import json 

data = {
    "Name" : "Mayur",
    "EmpID" : 101,
    "City" : "Vadodara",
    "Age" : 21
}

with open("abc.json",'w') as file:
    json.dump(data, file)

with open("abc.json", "r") as file:
    content = json.load(file)