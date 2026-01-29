# Write a decorator that logs the execution time of a function.

import time 
def timer(func):
    def function():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return function
@timer
def my_function():
    time.sleep(2)
    print("Hello!")

my_function()
