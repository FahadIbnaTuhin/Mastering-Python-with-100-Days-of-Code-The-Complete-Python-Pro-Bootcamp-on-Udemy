gavel = """
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
"""
print(gavel)
print("Welcome to the secret auction program.")
continueOrNot = True
bidders = {}
max_key, max_value = None, None


def find_highest_bidder(bidders_info):
    # bidders_info = {"Fahad": 20, "Sima": 200}

    # Using max function to get the highest key value from a dictionary
    # winner = max(bidders_info, key=bidders.get)
    # highest_bid = bidders[winner]

    winner = ""
    highest_bid = 0
    for bidder in bidders_info:
        highest = bidders_info[bidder]
        if highest_bid < highest:
            highest_bid = highest
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while continueOrNot:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == 'no':
        find_highest_bidder(bidders)
        continueOrNot = False
# print(bidders)


