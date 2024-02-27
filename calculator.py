logo = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def subs(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subs,
    "*": mult,
    "/": divide
}


def calculate():
    print(logo)
    num1 = int(input("What's the first number?: "))
    for key in operations:
        print(key)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick a symbol: ")
        num2 = int(input("What's the next number?: "))
        operation_function_name = operations[operation_symbol]
        result = operation_function_name(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            num1 = result
        else:
            should_continue = False
            calculate()


calculate()
