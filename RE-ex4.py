#Validate if a string is a valid phone number (e.g., 10 digits).

import re

phone_no = input("Enter a phone number: ")
pattern = r'^\d{10}$'

if re.match(pattern, phone_no):
    print("Valid phone number")
else:
    print("Invalid phone number")

