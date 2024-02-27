import pandas

data = pandas.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
# print(len(gray), len(cinnamon), len(black))

dataset = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [gray_count, cinnamon_count, black_count]
}
data_csv = pandas.DataFrame(dataset)
data_csv.to_csv("squirrel_count.csv")


