print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = (name1 + name2).lower()
count1 = 0
count2 = 0

for i in combined_name:
    if i.isalpha() and i in ['t', 'r', 'u', 'e']:
        count1 += 1

for i in combined_name:
    if i.isalpha() and i in ['l', 'o', 'v', 'e']:
        count2 += 1

score = str(count1) + str(count2)
score = int(score)

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
