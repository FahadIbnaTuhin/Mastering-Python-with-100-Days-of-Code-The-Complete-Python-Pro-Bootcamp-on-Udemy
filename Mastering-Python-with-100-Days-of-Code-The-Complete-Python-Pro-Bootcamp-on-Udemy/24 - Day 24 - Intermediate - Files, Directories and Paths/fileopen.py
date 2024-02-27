# file = open("fileopen.txt")
# contents = file.read()
# print(contents)

with open("fileopen.txt") as file:
    contents = file.read()
    print(contents)

# with open("fileopen.txt", "a") as file:
#     file.write("\nNew Text.")

# Creating a new file
# with open("newfile.txt", "w") as file:
#     file.write("New Text.")

# with open("newfile.txt", "w") as file:
#     file.write("\nHei fuckasf")
