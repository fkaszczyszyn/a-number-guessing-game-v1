import random
import sys
from statistics import mode, median, mean

# Display a welcome message
def welcome_message():
    print(" *" * 50)
    print("  " * 8 + "* " * 10 + "     WELCOME TO GUESS GAME!     " + "* " * 10)
    print(" *" * 50)

# Display a goodbye message
def good_bye():
    print(" *" * 50)
    print("  " * 10 + "* " * 10 + "     GOODBYE     " + "* " * 10)
    print(" *" * 50)

# The main game function
def start_game(random_number):
    attempts = 0
    player_choice = []

    while True:
        try:
            choice = input("Choose a number from 1 to 100 or type 'exit' to quit: ")

            if choice == 'exit':
                sys.exit()

            player_choice.append(int(choice))
            attempts += 1
            mode_test = mode(player_choice)
            player_choice.sort()
            median_test = median(player_choice)

            if int(choice) < 1 or int(choice) > 100:
                print("Please guess a number within the specified range.")
            elif int(choice) < random_number:
                print("It's higher! Try once again!")
            elif int(choice) > random_number:
                print("It's lower! Try once again!")
            else:
                print(
                    f"You won in {attempts} attempts! Mode is {mode_test}, Median is {median_test}, The correct number is {random_number}.")
                over_or_finish = input("Would you like to finish or start once again? 'Y' or 'N': ").strip().lower()
                if over_or_finish in ['n', 'exit']:
                    good_bye()
                    sys.exit()
                elif over_or_finish == 'y':
                    random_number = random.randint(1, 100)
        except ValueError:
            print("Please enter a valid number.")

# Main part of the program
welcome = input("Press 'Y' to start or 'N' to exit: ").strip().lower()

if welcome == 'y':
    welcome_message()
    random_number = random.randint(1, 100)
    start_game(random_number)
elif welcome in ['n', 'exit']:
    good_bye()
    sys.exit()
else:
    print("Please type only 'y' or 'n'")
