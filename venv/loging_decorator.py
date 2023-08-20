# Create the logging_decorator() function 👇
def get_func(function):
    def wrapper(*args):
        print(f"you called {function.__name__}(args)")
        result = function(args[0], args[1], args[2])
        print(f"it returned {result}")
    return wrapper


# Use the decorator 👇
@get_func
def a_function(a, b, c):
    return a+b+c


a_function(1,2,10)