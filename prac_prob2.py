# Ask the user to input age:
#- If age < 18 → print 'Minor'
#- If 18–59 → print 'Adult'
#- If 60+ → print 'Senior Citizen'

age = int(input("Enter your age: "))
if age < 18:
    print("Minor")
elif 18 <= age <= 59:
    print("Adult")
else:
    print("Senior Citizen")

# Sample Output :
# Enter your age: 21
# Adult

#2
# Enter your age: 62
# Senior Citizen