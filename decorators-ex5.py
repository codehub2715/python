#Combine multiple decorators on one function and observe the order of execution.
def decorator1(func):
    def dec1():
        print("Decorator 1")
        func()
    return dec1

def decorator2(func):
    def dec2():
        print("Decorator 2")
        func()
    return dec2

@decorator1
@decorator2

def my_function():
    print("Original Function")

my_function()
