import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv(r"Day26\NATO-alphabet-start\nato_phonetic_alphabet.csv")
code = {row.letter: row.code for (index, row) in df.iterrows()}
# print(code)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
phonetic_code = [code[letter.upper()] for letter in word]
print(phonetic_code)