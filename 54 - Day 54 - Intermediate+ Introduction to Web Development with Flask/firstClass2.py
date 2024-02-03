def get_details(function):
    def get_input():
        name = input("Enter a name? ")
        function(name)
    return get_input


@get_details
def greeting(name):
    print("Welcome " + name)


greeting()
