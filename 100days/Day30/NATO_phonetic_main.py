# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


word = input("Enter a word: ").upper()

try:
    output_list = [phonetic_dict[letter] for letter in word]
except KeyError as key_error:
    print("Only letters A-Z/a-z")
    while key_error:
        try:
            word = input("Enter a word: ").upper()
            output_list = [phonetic_dict[letter] for letter in word]
        except:
            print("Only letters A-Z/a-z")
        else:
            key_error = None
            

print(output_list)
