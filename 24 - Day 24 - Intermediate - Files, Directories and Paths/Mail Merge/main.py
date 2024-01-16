names = []
with open("Input/Names/invited_names.txt", "r") as all_names:
    for name in all_names.readlines():
        names.append(name.replace('\n', ''))
print(names)

with open("Input/Letters/starting_letter.txt", "r") as letter:
    text = letter.read()
print(text)

for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as send:
        new_text = text.replace('[name]', name)
        send.write(new_text)
