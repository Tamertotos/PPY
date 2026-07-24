import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter:row.code for (index, row) in df.iterrows()}

text = input("Enter a word: ").upper()
nato_alphabet_transition = [nato_alphabet[letter] for letter in text]

print(nato_alphabet_transition)