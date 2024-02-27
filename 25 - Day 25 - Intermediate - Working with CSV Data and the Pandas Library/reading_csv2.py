import pandas

data = pandas.read_csv("dhakaWeather.csv")
# print(type(data))
# Datafram: everything inside a datasheet in excel or any other software

# print(type(data["temp"]))
# print(type(data.temp))
# Series: every colloum is a series which is like a list, you can say. Two of them are same above

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].tolist()
# print(sum(temp_list) / len(temp_list))
# print(data["temp"].mean())

# Get Data in Row. Both are same
# print(data[data.day == "Monday"])
# print(data[data["day"] == "Monday"])

# Print the line that has the highest temp
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp_c = monday.temp
# monday_temp_f = (monday_temp_c * 9 / 5) + 32
# print(monday_temp_f)

# Create a datafram from scratch and save that into another csv file
data1 = {
    "students": ["Fahad", "Sima", "Munna"],
    "scores": [30, 15, 25]
}
data_d = pandas.DataFrame(data1)
# print(data_d)
data_d.to_csv("new_data.csv")
