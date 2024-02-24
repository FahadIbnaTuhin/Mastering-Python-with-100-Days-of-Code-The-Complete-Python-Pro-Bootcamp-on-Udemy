
import random
from higher_lower_data import data
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \\/ _ \\/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\\__, /_/ /_/\\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \\ | /| / / _ \\/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\\____/|__/|__/\\___/_/     
"""
print(logo)
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
score = 0
continue_game = True
lpick = random.choice(data)


def format_name(pick):
    return f"{pick["name"]}, {pick["description"]}, {pick["country"]}"


def check_ans(guess, first_pick, last_pick):
    if first_pick > last_pick:
        return guess == "a"
    else:
        return guess == "b"


while continue_game:
    fpick = lpick
    lpick = random.choice(data)
    while fpick == lpick:
        lpick = random.choice(data)

    # print(fpick["follower_count"], lpick["follower_count"])
    print(f"Choice A: {format_name(fpick)}.")
    print(vs)
    print(f"Against B: {format_name(lpick)}.")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_ans(choice, fpick["follower_count"], lpick["follower_count"])

    if is_correct:
        score += 1
        print(f"You're right. Current Score: {score}")
    else:
        continue_game = False
        print(f"Sorry, That's wrong. Final Score: {score}")
