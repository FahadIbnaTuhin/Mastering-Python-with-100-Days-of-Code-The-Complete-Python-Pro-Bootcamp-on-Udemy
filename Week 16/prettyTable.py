from prettytable import PrettyTable

table = PrettyTable()

# Read the documentation to learn and use easily from pypi
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charamander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
table.field_names = ["ID", "Name", "Roll"]
# table.add_row(["1", "MD. Fahad Ibna Tuhin", 60])
# table.add_row(["2", "Sima Sarkar", 20])
table.add_rows(
    [
        ["1", "MD. Fahad Ibna Tuhin", 60],
        ["2", "Sima Sarkar", 20]
    ]
)

print(table)