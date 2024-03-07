import random

choices = ["Rock", "Paper", "Scissors"]

user_choice = input("Enter your choice (1) Rock, (2) Paper, or (3) Scissors: ")
user_choice = int(user_choice) - 1

if user_choice < 0 or user_choice >= len(choices):
    print("Invalid choice!")
else:
    computer_choice = random.randint(0, 2)

    print("You chose:", choices[user_choice])
    print("Computer chose:", choices[computer_choice])

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins!")