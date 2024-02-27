# try:
#     file = open("nek.txt", "r")
#     dicccc = {"name": "Fahad"}
#     print(dicccc["name"])
# except FileNotFoundError:
#     file = open("nek.txt", "w")
#     file.write("Something")
# except KeyError as error_msg:
#     print(f"That key {error_msg} doesn't exist")
# else:
#     print("Success")
# finally:
#     file.close()
#     # raise FileNotFoundError("not found")
#     raise KeyError("This is the error that I made myself")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
    # ValueError: Whoever value is entered as the argument probably wrong

bmi = weight / height ** 2
print(bmi)

