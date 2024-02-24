import cipher_art
print(cipher_art.logo)


def caesar(user_text, key_value, user_direction):
    new_text = ""
    # Formula of Plaintext to ciphertext : Ci = (Pi + K) % 26
    if user_direction == 'encode':
        for letter in user_text:
            if not letter.isalpha():
                new_text += letter
            elif letter.isupper():
                pi = ord(letter) - 65  # A = 65 to A = 0
                ci_digit = (pi + key_value) % 26  # getting ci_digit value after adding cipher formula
                ci = ci_digit + 65  # adding again 65
                # print(ci, chr(ci))
                new_text += chr(ci)  # converting digit to value
            else:
                pi = ord(letter) - 97
                ci_digit = (pi + key_value) % 26
                ci = ci_digit + 97
                new_text += chr(ci)
                # print("Lower baby", letter)
    # Formula of Cyphertext to Plaintext: Pi = (Ci - K + 26) % 26
    elif user_direction == 'decode':
        for letter in user_text:
            if not letter.isalpha():
                new_text += letter
            elif letter.isupper():
                ci = ord(letter) - 65
                pi_digit = (ci - key_value + 26) % 26
                pi = pi_digit + 65
                new_text += chr(pi)
            else:
                ci = ord(letter) - 97
                pi_digit = (ci - key_value + 26) % 26
                pi = pi_digit + 97
                new_text += chr(pi)
    print(new_text)


inp = 'yes'
while inp == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    key = int(input("Type the shift number:\n"))
    caesar(text, key, direction)
    inp = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
