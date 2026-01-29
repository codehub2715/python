def outer(x):
    def inner():
        print(f"Value: {x}")
    return inner

closure_func = outer(10)
closure_func() 
