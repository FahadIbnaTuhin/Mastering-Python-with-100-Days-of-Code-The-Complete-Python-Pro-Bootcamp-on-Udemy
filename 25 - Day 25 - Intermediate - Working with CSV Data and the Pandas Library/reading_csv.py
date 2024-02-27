# with open("dhakaWeather.csv", "r") as file:
#     data = file.readlines()
# print(data)

import csv

# with open("dhakaWeather.csv", "r") as file:
#     # csv.reader makes the file as a csv object
#     data = csv.reader(file)
#     # print(data)
#
#     # for line in data:
#     #     print(line)
#
#     temperatures = []
#     for line in data:
#         if line[1] != 'temp':
#             temperatures.append(int(line[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("dhakaWeather.csv")
# print(data)
print(data["temp"])
