import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter:row.code for (index, row) in df.iterrows()}


while True:
    text = input("Enter a word: ").upper()
    try:
        nato_alphabet_transition = [nato_alphabet[letter] for letter in text]
    except KeyError as error_message:
        print(f"Given {error_message} is not a valid key. Enter a word using Latin alphabet")
    else:
        print(nato_alphabet_transition)
        break
