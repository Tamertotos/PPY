import random

moves = ["rock","paper","scissors"]
user_moves = []
computer_moves = []
art = ['''ROCK
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        ''',
 '''PAPER
     _______
 ---'   ____)____
            ______)
            _______)
           _______)
 ---.__________)
     ''',
 '''SCISSORS
      _______
  ---'   ____)____
            ______)
        __________)
      (____)
---.__(___)
      ''']

wins_against = {0: 2, 1: 0, 2: 1}


user_score = 0
computer_score = 0
rounds = 0
while rounds < 3:
    try:
        user_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
        if user_move not in (0,1,2):
            print("Please enter 0, 1, or 2.")
            continue
    except ValueError:
        print("Invalid input. Enter a number!")
        continue


    computer_move = random.randint(0,2)

    user_moves.append(moves[user_move])
    computer_moves.append(moves[computer_move])

    print(art[user_move])
    print(art[computer_move])

    if user_move == computer_move:
        print("draw")
    elif user_move == 0 and computer_move == 2:
        print("User wins")
        user_score += 1
    elif user_move == 0 and computer_move == 1:
        print("Computer wins")
        computer_score += 1
    elif user_move == 1 and computer_move == 0:
        print("User wins")
        user_score += 1
    elif user_move == 1 and computer_move == 2:
        print("Computer wins")
        computer_score += 1
    elif user_move == 2 and computer_move == 0:
        print("Computer wins")
        computer_score += 1
    elif user_move == 2 and computer_move == 1:
        print("User wins")
        user_score += 1

    if user_score == 2 or computer_score == 2:
        print("Consecutive wins!")
        break


    print (f"Current user score is: {user_score}, current computer score is: {computer_score}")
    rounds += 1

print(f"All user moves: {user_moves}")
print(f"All computer moves: {computer_moves}")