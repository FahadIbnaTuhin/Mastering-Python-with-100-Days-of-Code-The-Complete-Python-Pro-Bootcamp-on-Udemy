def password_generator():
    from random import choice, randint, shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    ans = [choice(letters) for _ in range(randint(8, 10))]
    ans += [choice(symbols) for _ in range(randint(2, 4))]
    ans += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(ans)

    pwd = "".join(ans)
    return pwd

# It is from previous password generator, but we shortcut a lot
