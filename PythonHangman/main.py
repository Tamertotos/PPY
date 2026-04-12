import random
import hangman_words as HW
import hangman_art as HA

chosen_word = random.choice(HW.words)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(placeholder)


game_over = False
lst = []
lives = 6
while not game_over and lives > 0:
    print(f"***********{lives}/6 LIVES LEFT*********************************")
    guess = input("Guess a letter: ").lower()

    if guess in lst:
        print(f"You already guessed this letter: {guess}")
        continue

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += guess
            lst.append(guess)
        elif letter in lst:
            display += letter
        else:
            display += "_"


    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.\nYou lose a life.")
        lives -=1
        print(HA.stage[lives])
    else:
        print(HA.stage[lives])


    if "_" not in display:
        game_over = True
        print("Congrats you found the word!")
    print(display)

    if lives == 0:
        print(f"***********************You lost! It was: {chosen_word}***************")