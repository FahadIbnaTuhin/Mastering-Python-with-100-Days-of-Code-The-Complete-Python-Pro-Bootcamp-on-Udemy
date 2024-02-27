# This is created based on the international standard alphabet.

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

print('Text to Morse Code Converter')
inp = input('Enter the text to convert: ').strip().upper()

print('Morse Code:', end=' ')
for i in inp:
    if i.upper() in MORSE_CODE_DICT:
        print(MORSE_CODE_DICT[i], end=' ')
    elif i == ' ':
        print('|', end=' ')
    else:
        print(i, end=' ')

print()
