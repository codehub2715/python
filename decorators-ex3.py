#create a decorator that converts the result of a function to uppercase if it's a string.

def upper(func):
    def funtion():
        result = func()
        if isinstance(result, str):
            result = result.upper()
        return result
    return funtion

@upper
def get_string():
    return "123 v-ex tech solutions"
print(get_string())


