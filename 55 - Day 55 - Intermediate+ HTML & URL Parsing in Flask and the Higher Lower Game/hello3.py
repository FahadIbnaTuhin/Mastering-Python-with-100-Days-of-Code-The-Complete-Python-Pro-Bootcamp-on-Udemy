class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.permission = False


def is_age_ok(function):
    def wrapper(*args, **kwargs):
        if args[0].age >= 18:
            args[0].permission = True
        if args[0].permission == True:
            function(args[0])
    return wrapper


@is_age_ok
def enjoy_ride(user):
    print(f"Enjoy your ride {user.name}! Happy Ride!")


new_user = User("Fahad", 18)
enjoy_ride(new_user)
