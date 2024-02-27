# If you declare datatype for a variable, later on when you work with the variable, it will only take
# the same data type that you declared using ":". If you choose wrong datatype that time, it will show you
# yellow color as a hint. Hover over the yellow, get the answer
# For long code, it is helpful.
number: int

# number = "twelve"
# number = 12

# name: str
# height: float
# is_human = bool


# def police_check(age: int):
#     if age >= 18:
#         can_drive = True
#     else:
#         can_drive = False
#     return can_drive
#
#
# if police_check("twelve"):
#     print("You may pass")
# else:
#     print("Pay a fine")


# "-> bool" means it will return bool and if you return other thing, then it will highlight
# error when you return other things
def police_check(age: int) -> bool:
    if age >= 18:
        can_drive = True
    else:
        can_drive = False
    return "Umbrella"


# Means: name parameters data type will be string and this function will return str at the end
def greeting(name: str) -> str:
    return "Hello" + name
