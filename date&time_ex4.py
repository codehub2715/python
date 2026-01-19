#Find how many days are left until a given future date (e.g., New Year).
from datetime import datetime
future_date_str = input("Enter a future date (DD-MM-YYYY): ")
future_date = datetime.strptime(future_date_str, "%d-%m-%Y")
today = datetime.today()
days_left = (future_date - today).days
print("Days left until", future_date.date(), ":", days_left)

#Output:
#Enter a future date (DD-MM-YYYY): 01-01-2027
#Days left until 2027-01-01 : 346#
