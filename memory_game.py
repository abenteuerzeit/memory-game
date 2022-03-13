import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_board(height, width):
    try:
        ammount_of_letters = height * width
        if ammount_of_letters > len(alphabet) or ammount_of_letters % 2 != 0:
            raise ValueError
        else:
            matrix = []
            for i in range(height):
                matrix.append([random.choice(alphabet) for i in range(width)])
            return matrix
    except ValueError:
        print("Error! \nEither the height or width is an odd number,\nor not enough letters in the latin alphabet to generate the board.")


# Get field position from User

# The user can select a field on the board, by typing in its coordinates, such as B2. The letter denotes the column (A is 0, B is 1, and so on...) and the number denotes the row. Do not forget that 1 actually refers to 0 index.
# The program checks whether the user input is in the LETTERNUMBER format, such as B2 or C4.
# The program checks whether the input number is positive and does not exceed the number of rows on the board.
# The program checks whether the position of the input letter in the alphabet does not exceed the number of columns on the board.
# The program keeps asking the user for a field until receiving valid input.
# After the input is validated, coordinates of the selected field are passed further into the program logic as an integer tuple (row, column).
def display_menu():
    print("Select a difficulty level. Enter the corresponding number. ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")


def get_difficulty():
    while True:
        display_menu()
        try:
            user_input = int(input("Select a difficulty level: "))
            if user_input == 1:
                board_size = [5, 4]
                return board_size
            elif user_input == 2:
                board_size = [5, 6]
                return board_size
            elif user_input == 3:
                board_size = [5, 10]
                return board_size
            else:
                print("\nOption not avaialable.")
                raise ValueError
        except ValueError:
            print("\nInvalid input. Try again. ")



# Implement the board drawing mechanic, according to the following requirements.
# When drawing the board, the coordinates of fields are also be displayed (numbers of rows and letters of columns), similar to the following example:
#   A B C D E

# 1 # # # # #

# 2 # # # # #

# 3 # # # # #

# 4 # # # # #
# During the game, the fields can be either concealed or revealed. The letter of the field is displayed only when the field is revealed. When the field is concealed, # is displayed.
# The terminal window is cleaned every time the board is redrawn.


# Game logic

# Implement the game logic, to put all parts together into a functioning game.
# The game opens with Welcome to Memory Game!.
# The game asks to select a difficulty level.
# The letter board is generated, based on the selected difficulty level.
# The fields of the letter board are all concealed by default.
# The board is displayed to the user.
# The game asks asked to select a field, which is then revealed (its letter is being shown on the redrawn board).
# The game asks to select another field, which is then revealed (its letter is being shown on the redrawn board).
# If the two selected fields are a match (have the same letter), they remain revealed for the rest of the game.
# If the two selected fields are not a match (do not have the same letters), the user is asked to press Enter. After that, the fields are concealed again.
# The game ends when all fields are revealed.
# The game counts the number of steps taken to complete the game and displays this number after winning the game.
def main():
    # write your code here
    pass

if __name__ == "__main__":
   main()
