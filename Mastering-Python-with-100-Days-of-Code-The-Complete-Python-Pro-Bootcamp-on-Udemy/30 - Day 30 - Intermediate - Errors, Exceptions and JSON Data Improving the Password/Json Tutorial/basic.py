import json

website_inp = input("Website: ")
user_name = input("Username: ")
password = input("Password: ")

new_data = {
    website_inp: {
        "info": user_name,
        "password": password
    }
}

# For Writing: json.dump() | For Reading: json.load() | For Updating: json.update()

# Writing data as json format
# with open("data.json", "w") as file:
#     json.dump(new_data, file, indent=4)
# indent: number of spaces to indent all the json data.without this, it will not easy to read as
# a human, but you can read

# Loading data from json file
# with open("data.json", "r") as file:
#     data = json.load(file)
#     print(data)

# Loading, then updating data
# with open("data.json", "r") as file:
#     data = json.load(file)
#     data.update(new_data)
#     print(data)

# Loading, updating then writing
try:
    with open("data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    with open("data.json", "w") as file:
        json.dump(new_data, file, indent=4)
else:
    data.update(new_data)
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
