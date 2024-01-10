def is_prime_number(n):
    if n < 2:
        print("It's not a prime number")
    # It check from 2 to before n (not including n). If nothing is divisible, then it's a prime
    for i in range(2, n):
        if n % i == 0:
            print("It's not a prime number")
            return
    print("It's a prime number")


inp = int(input("Enter a number to check if it is a prime number or not: "))
is_prime_number(inp)