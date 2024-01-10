RESOURCE = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
is_continue = True


def is_resource_sufficient(ingredients):
    """Return True if there are enough resource, otherwise False with the item that is not enough"""
    # print(ingredients)
    for key in ingredients:
        if ingredients[key] >= RESOURCE[key]:
            print(f"Sorry, there is not enough {key}")
            return False
    return True


def process_coin():
    """Will process the money"""
    print("Please insert coins")
    cost = float(input("How many quarters?: ")) * 0.25
    cost += float(input("How many dimes?: ")) * 0.1
    cost += float(input("How many nickles?: ")) * 0.05
    cost += float(input("How many pennies?: ")) * 0.01
    return cost


def is_transaction_successful(product_cost, u_money):
    """Return True if the user has enough money. Otherwise false"""
    # print(product)
    if u_money >= product_cost:
        # Money Calculation
        RESOURCE["money"] += product_cost
        change = round((u_money - product_cost), 2)
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(product, menu_ingrid):
    """Reducing the ingredients from the menu"""
    # print(menu_ingrid)
    for key in menu_ingrid:
        RESOURCE[key] -= menu_ingrid[key]
    print(f"Here is your {product} ☕ Enjoy!")


while is_continue:
    choice = input("What would you like? (espresso, latte, cappuccino): ").lower()

    if choice == "off":
        is_continue = False
    elif choice == "report":
        print(f"Water: {RESOURCE["water"]}ml\nMilk: {RESOURCE["milk"]}ml\nCoffee: {RESOURCE["coffee"]}g\n"
              f"Money: ${RESOURCE["money"]}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if is_resource_sufficient(MENU[choice]["ingredients"]):
            # print("Success")
            users_money = process_coin()
            # print(users_money)
            if is_transaction_successful(MENU[choice]["cost"], users_money):
                make_coffee(choice, MENU[choice]["ingredients"])
    else:
        print("Wrong Input. Try Again.")
