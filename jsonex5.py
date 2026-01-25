#Parse a JSON string representing a list of products and print each product's name and price.

import json

json_string = '[{"name": "Product 1", "price": 10}, {"name": "Product 2", "price": 20}]'

data = json.loads(json_string)

for product in data:
    print("Name:", product["name"])
    print("Price:", product["price"])
    print()
