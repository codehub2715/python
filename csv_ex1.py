#Create a CSV file with employee details and write rows using csv.writer.

import csv

with open("abc.csv",'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Mayur", 21, "Vadodara"])
    writer.writerow(["Kirtan", 21, "Vadodara"])
    writer.writerow(["Raj", 21, "Vadodara"])

