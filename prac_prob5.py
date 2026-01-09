#Create a login system with stored username and password. Ask for input, check, and print 'Welcome' or 'Access Denied'.

username = "mayur"
password = "12345"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username == username and input_password == password:
    print("Welcome")
else:
    print("Access Denied")

#Output :
#Enter username: mayur
#Enter password: 12345
#Welcome

#Enter username: mayur
#Enter password: 54321
#Access Denied