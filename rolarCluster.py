print("Welcome Rolar Coaster")
height = int(input("Height: "))
price = 0

if height > 120:
    age = int(input("Age: "))
    if age < 12:
        price += 5
        print("Child tickets are $5")
    elif age < 18:
        price += 7
        print("Youth tickets are $7")
    else:
        price += 12
        print("Adult tickets are $12")

    want_pic = input("Want Photos for $3 (y/n)? ").lower()
    if want_pic == "y":
        price += 3

    print(f"Your bill is {price}")
else:
    print("Can't ride")
