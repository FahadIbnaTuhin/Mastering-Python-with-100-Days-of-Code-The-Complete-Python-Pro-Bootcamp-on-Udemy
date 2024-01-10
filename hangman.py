import random
from hangman_word import word_list
from hangman_art import stages, logo

# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
print(logo)
end_of_game = False
lives = 6

display = ["_" for i in chosen_word]
for i in display:
    print(i, end="")
print()

while not end_of_game:
    guess = input("Enter a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}.")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    for i in display:
        print(i, end="")
    print()

    # Checking if a guess(letter) inside a string(chosen_word) or not
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose")

    if "_" not in display:
        end_of_game = True
        print("You Win")
