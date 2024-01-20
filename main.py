# records = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     records.append([name, score])
# print(records)

records = [["Fahad", 15], ["Sima", 10], ["Mala", 15]]

names, scores = [], []
for info in records:
    names.append(info[0])
    scores.append(info[1])

print(names, scores)
indexes = [i for i, x in enumerate(scores) if max(scores) == x]
print(indexes)
