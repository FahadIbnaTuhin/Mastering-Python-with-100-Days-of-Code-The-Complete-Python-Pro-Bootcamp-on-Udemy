# FileNotFoundError
# with open("need.txt", "r") as file:
#     file.read()

# KeyError
# hello = {"Hi": "asldf"}
# print(hello["ji"])

# IndexError
# fruits = ["Apple", "Banana"]
# print(fruits[2])

# TypeError
# a = "hello"
# print(a + 5)

# if you use only "except:", it will work for every error
# try:
#     file = open("nek.txt", "r")
#     dicccc = {"name": "Fahad"}
#     print(dicccc["age"])
# except FileNotFoundError:
#     file = open("nek.txt", "w")
#     file.write("Something")
# except KeyError as error_msg:
#     print(f"That key {error_msg} doesn't exist")
# the first error that will be found by try will go inside that error except. That error except will only execute

try:
    file = open("nek.txt", "r")
    dicccc = {"name": "Fahad"}
    print(dicccc["name"])
except FileNotFoundError:
    file = open("nek.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"That key {error_msg} doesn't exist")
else:
    # else will only occur if there is no error happened
    print("Success")
finally:
    # it will always execute no matter if there are any error or not
    file.close()
    print("Closed")
