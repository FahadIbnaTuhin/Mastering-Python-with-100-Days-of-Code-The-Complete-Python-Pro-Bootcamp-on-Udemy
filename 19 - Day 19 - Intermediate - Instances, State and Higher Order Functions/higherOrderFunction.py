# A function that can work with other function called Higher Order Function


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def calculate(n1, n2, func):
    return func(n1, n2)


result = calculate(5, 2, div)
print(result)
