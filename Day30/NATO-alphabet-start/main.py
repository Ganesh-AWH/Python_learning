import pandas as pd


df = pd.read_csv(r"Day30\NATO-alphabet-start\nato_phonetic_alphabet.csv")
code = {row.letter: row.code for (index, row) in df.iterrows()}
print(code)

def generate_phonetic():
    word = input("Enter a word: ")
    try:
        phonetic_code = [code[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_code)


generate_phonetic()