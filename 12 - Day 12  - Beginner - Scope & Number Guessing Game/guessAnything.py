import random
logo = """

 $$$$$$\\                                             $$$$$$\\                     $$\\    $$\\      $$\\                  
$$  __$$\\                                           $$  __$$\\                    $$ |   $$ |     \\__|                  
$$ /  \\__$$\\   $$\\ $$$$$$\\  $$$$$$$\\ $$$$$$$\\       $$ /  $$ $$$$$$$\\ $$\\   $$\\$$$$$$\\  $$$$$$$\\ $$\\$$$$$$$\\  $$$$$$\\  
$$ |$$$$\\$$ |  $$ $$  __$$\\$$  _____$$  _____|      $$$$$$$$ $$  __$$\\$$ |  $$ \\_$$  _| $$  __$$\\$$ $$  __$$\\$$  __$$\\ 
$$ |\\_$$ $$ |  $$ $$$$$$$$ \\$$$$$$\\ \\$$$$$$\\        $$  __$$ $$ |  $$ $$ |  $$ | $$ |   $$ |  $$ $$ $$ |  $$ $$ /  $$ |
$$ |  $$ $$ |  $$ $$   ____|\\____$$\\ \\____$$\\       $$ |  $$ $$ |  $$ $$ |  $$ | $$ |$$\\$$ |  $$ $$ $$ |  $$ $$ |  $$ |
\\$$$$$$  \\$$$$$$  \\$$$$$$$\\$$$$$$$  $$$$$$$  |      $$ |  $$ $$ |  $$ \\$$$$$$$ | \\$$$$  $$ |  $$ $$ $$ |  $$ \\$$$$$$$ |
 \\______/ \\______/ \\_______\\_______/\\_______/       \\__|  \\__\\__|  \\__|\\____$$ |  \\____/\\__|  \\__\\__\\__| \\__|\\____$$ |
                                                                      $$\\   $$ |                             $$\\   $$ |
                                                                      \\$$$$$$  |                             \\$$$$$$  |
                                                                       \\______/                               \\______/ 
"""


def guess(n, lucky_num):
    for i in range(n):
        print(f"You have {n - i} attempts remaining to guess the number. ")
        guessing_input = int(input("Make a guess: "))
        if guessing_input > lucky_num:
            print("Too high.")
        elif guessing_input < lucky_num:
            print("Too low.")
        else:
            print("You win")
            return
        if i != (n - 1):
            print("Guess Again.")

    print(f"You lost. Correct Answer: {lucky_num}")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    lucky_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    difficulty_level = {
        'easy': 10,
        'hard': 5
    }
    round = difficulty_level[difficulty]
    # print(level)

    guess(round, lucky_number)


game()
