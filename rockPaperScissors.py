import random

# Rock Paper Scissors ASCII Art search on Google
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
rockPaperScissors = [rock, paper, scissors]
# for i in rockPaperScissors:
#     print(i)

inp = None
while True:
    try:
        inp = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    except ValueError:
        print("Input a number!")
        continue
    if inp in [0, 1, 2]:
        print(rockPaperScissors[inp])
        break
    print("Wrong Input, Any value between 0 and 2, inclusive.")

print("Computer chose: \n")
random_inp = random.randint(0, 2)
print(rockPaperScissors[random_inp])

if (inp == 0 and random_inp == 2) or (inp == 1 and random_inp == 0) or (inp == 2 and random_inp == 1):
    print("You win")
elif (inp == 0 and random_inp == 1) or (inp == 1 and random_inp == 2) or (inp == 2 and random_inp == 0):
    print("You lose")
else:
    print("Draw")

