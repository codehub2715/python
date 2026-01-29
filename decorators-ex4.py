#Build a decorator that repeats a function call 3 times.

def repeat(func):
    def function():
        for i in range(3):
            func()
    return function

@repeat
def funccall():
    print("DataScience")

funccall()