import random
import sys
from statistics import mode, median, mean

# The main game function
def start_game(random_number):
    attempts = 0
    player_choice = []

    while True:
        try:
            choice = input("Choose a number from 1 to 100 or type 'exit' to quit: ")

            if choice == 'exit':
                sys.exit()

            attempts += 1

            if int(choice) < 1 or int(choice) > 100:
                print("Please guess a number within the specified range.")
            elif int(choice) < random_number:
                print("It's higher! Try once again!")
            elif int(choice) > random_number:
                print("It's lower! Try once again!")
            else:
                total_attempts.append(attempts)
                mode_test = mode(total_attempts)
                mean_test = round(mean(total_attempts))
                median_test = round(mean(total_attempts))
                print(
                    f"You won in {attempts} attempts! Mean is {mean_test}, Mode is {mode_test}, Median is {median_test}, The correct number is {random_number}.")
                total_attempts.append(attempts)

                # Track the best score and display it
                best_score = min(total_attempts)
                print(f"Best score: {best_score}")

                over_or_finish = input("Would you like to finish or start once again? 'Y' or 'N': ").strip().lower()
                if over_or_finish in ['n', 'exit']:
                    print("Good Bye")
                    sys.exit()
                elif over_or_finish == 'y':
                    random_number = random.randint(1, 100)
                    attempts = 0
                    player_choice = []

        except ValueError:
            print("Please enter a valid number.")

# Main part of the program
welcome = input("Press 'Y' to start or 'N' to exit: ").strip().lower()
total_attempts = []

if welcome == 'y':
    print("Welcome to the guessing game!")
    random_number = random.randint(1, 100)
    start_game(random_number)
elif welcome in ['n', 'exit']:
    print("Good Bye")
    sys.exit()
else:
    print("Please type only 'y' or 'n'")