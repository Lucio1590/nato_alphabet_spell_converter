import pandas as pd

alphabet_data = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = { val.letter:val.code for (_,val) in alphabet_data.iterrows()}
print(nato_dict)

word= input("Enter a word: ")
result = []
for letter in word.upper():
    result.append(nato_dict[letter])

result = ' - '.join(result)
print(result)