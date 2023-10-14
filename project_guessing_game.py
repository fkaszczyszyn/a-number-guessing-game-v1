import random
import sys


def start_game(random_number, player_choice):
    attempts = 0

    while True:
        try:
            player_choice == int(input("Once again!    "))
            attempts += 1
            if random_number <= player_choice:
                print("I's higher!")
            elif random_number >= player_choice:
                print("I's lower!")
            else:
                print("You won!")
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