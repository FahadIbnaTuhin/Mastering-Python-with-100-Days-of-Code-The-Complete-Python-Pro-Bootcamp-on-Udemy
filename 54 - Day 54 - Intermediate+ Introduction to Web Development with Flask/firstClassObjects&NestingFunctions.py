# def add(n1, n2):
#     return n1 + n2
#
#
# def substract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
# Functions are first-class-objects, can be passed around as arguments e.g. int/string/float etc.
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# result = calculate(multiply, 5, 10)
# print(result)

# Nested Function
# def outer_function():
#     print("I am outer")
#
#     def inner_function():
#         print("I am inner")
#
#     inner_function()
# outer_function()

# Functions can be returned from other functions
# def outer_function():
#     print("I am outer")
#
#     def inner_function():
#         print("I am inner")
#
#     return inner_function
# # This will give this output: "I am outer"
# inner_function = outer_function()
# # This will give this output: "I am inner"
# inner_function()


# Decorator Function
import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")


# say_hello()
# say_greeting()
# without using '@delay_decorator', can use this also but not recommend
decorated_function = delay_decorator(say_greeting)
decorated_function()
