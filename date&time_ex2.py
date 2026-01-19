#Calculate your age based on your birthdate.
from datetime import datetime
birthdate_str = input("Enter your birthdate (DD-MM-YYYY): ")
birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
today = datetime.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
print("Your age is:", age)


#Output:
#Enter your birthdate (DD-MM-YYYY): 27-01-2005
#Your age is: 20