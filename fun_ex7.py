def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter the find factorial of number:"))
print("Factorial :",factorial(num))

#Output:
#Enter the find factorial of number:6
#Factorial : 720