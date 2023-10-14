import random
import sys


def start_game(random_number, player_choice):
    attempts = 0

    while True:
        try:
            player_choice = int(input("Once again!    "))
            attempts += 1

            if player_choice < 1 or player_choice > 100:
                print("Please guess a number within the specified range.")
            elif player_choice < random_number:
                print("It's higher!")
            elif player_choice > random_number:
                print("It's lower")
            else:
                print(f"You won in {attempts} attempts! The correct number is {random_number}.")
                sys.exit()
        except ValueError:
            print("Please enter a valid number.")


welcome = input("Welcome to the number guessing game. Press 'Y' to start or 'N' to exit: ").strip().lower()

if welcome == 'y':
    print("Let's start")
    random_number = random.randint(1, 100)
    player_choice = input("Please choose a number from 1-100: ")
    player_choice = int(player_choice)
    start_game(random_number, player_choice)
elif welcome == 'n':
    print("Goodbye")
else:
    print("Please type only 'y' or 'n'")