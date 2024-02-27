row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure(eg: \"23\" means 2nd collum & 3rd row)? ") # 23

map = [row1, row2, row3]
# print(map)
col, row = (int(position[0]) - 1), (int(position[1]) - 1) # 12
map[row][col] = "❌"
# print(map)

# ❌ Search emoji on google, copy the emoji you want from any website

for i in map:
    for j in i:
        print(j, end="")
    print()
