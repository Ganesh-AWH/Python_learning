# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def encrypt(message):
    cipher = ''
    for letter in message.upper():
        if letter in MORSE_CODE_DICT:
            # We add a space after every morse character to separate them
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # If a character isn't in our dictionary, skip it or add a placeholder
            cipher += ''
    return cipher

def main():
    print("--- Text to Morse Code Converter ---")
    user_input = input("Enter the message you want to convert: ")
    
    result = encrypt(user_input)
    
    print("\nEncoded Message:")
    print(result)

if __name__ == "__main__":
    main()