def add(*args):
    # print(args)
    # Tuple
    # print(args[-1])

    count = 0
    for n in args:
        count += n
    print(count)


add(2, 5, 7)


def calculate(**kwargs):
    print(kwargs)
    # Dictionary

    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["mult"])


calculate(add=3, mult=5)


def calculate2(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["mult"]
    return n


print(calculate2(2, add=5, mult=10))


class Car:

    def __init__(self, **kwargs):
        # get() : if the key doesn't exist in the dictionary, it will return None instead of a error
        self.make = kwargs["make"]
        self.model = kwargs.get("model")


my_car = Car(make="Ronald")
print(my_car.make, my_car.model)
