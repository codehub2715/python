#Read the CSV file and filter records (e.g., age > 30).

import csv

with open("abc.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["Age"]) > 30:
            print(row)

