placeholder = "[name]"

with open("Input/Names/invited_names.txt", "r") as names:
    names = names.readlines()
print(names)

with open("Input/Letters/starting_letter.txt", "r") as letter:
    letter_contents = letter.read()
    for name in names:
        new_name = name.strip()
        new_letter = letter_contents.replace(placeholder, new_name)
        with open(f"Output/ReadyToSend/letter_for_{new_name}.txt", "w") as send:
            send.write(new_letter)

# print(letter_contents)
