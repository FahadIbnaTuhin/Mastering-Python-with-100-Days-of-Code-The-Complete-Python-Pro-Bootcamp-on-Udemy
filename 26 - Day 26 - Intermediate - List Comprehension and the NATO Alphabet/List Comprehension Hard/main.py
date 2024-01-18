# Task: see file1 and file2. Now make a list of the items that are same both in file1 and file2

with open("file1.txt", "r") as file1:
    file1_data = file1.readlines()

with open("file2.txt", "r") as file2:
    file2_data = file2.readlines()

# int(): this converts string to number and at the same time, ignore any newline character
same_data = [int(num) for num in file1_data if num in file2_data]

print(same_data)
