#Write a decorator that checks if a user is authenticated before running a function (simulate with a boolean).

def authenticated(func):
    def function():
        authenticated = True
        if authenticated:
            func()
        else:
            print("User is not authenticated.")
    return function

@authenticated
def secure_function():
    print("This function is secure and can only be accessed by authenticated users.")

secure_function()