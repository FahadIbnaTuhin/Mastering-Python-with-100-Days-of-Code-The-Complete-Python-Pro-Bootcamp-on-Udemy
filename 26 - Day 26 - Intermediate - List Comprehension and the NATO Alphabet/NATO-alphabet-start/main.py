import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
dataset = {row.letter: row.code for (index, row) in data.iterrows()}
print(dataset)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_sen = input("Enter a word: ").upper()
user_sen_words = [dataset[letter] for letter in user_sen]

print(user_sen_words)
