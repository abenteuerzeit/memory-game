import os
import random
from re import I

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


def get_user_field_position():
    board_fields = {}
    
# The user can select a field on the board, by typing in its coordinates, such as B2. 
# The letter denotes the column (A is 0, B is 1, and so on...) and the number denotes the row. Do not forget that 1 actually refers to 0 index.
# The program checks whether the user input is in the LETTERNUMBER format, such as B2 or C4.
# The program checks whether the input number is positive and does not exceed the number of rows on the board.
# The program checks whether the position of the input letter in the alphabet does not exceed the number of columns on the board.
# The program keeps asking the user for a field until receiving valid input.
# After the input is validated, coordinates of the selected field are passed further into the program logic as an integer tuple (row, column).
    pass 

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


def draw_board(board):
    width = len(board)
    columns = [letter for letter in alphabet[:width-1]]
    print("\n     " + " ".join(columns) + "\n")
    for count, row in enumerate(board):
        print(f"{count + 1}    " + " ".join(row))
    print("")

# During the game, the fields can be either concealed or revealed. 
# The letter of the field is displayed only when the field is revealed. 
# When the field is concealed, # is displayed.
# The terminal window is cleaned every time the board is redrawn.

def main():
    print("Welcome to Memory Game!")
    board_size = get_difficulty()
    console_clear()
    board = generate_board(height=board_size[0], width=board_size[1])
    draw_board(board)


# The fields of the letter board are all concealed by default.
# The board is displayed to the user.
# The game asks asked to select a field, which is then revealed (its letter is being shown on the redrawn board).
# The game asks to select another field, which is then revealed (its letter is being shown on the redrawn board).
# If the two selected fields are a match (have the same letter), they remain revealed for the rest of the game.
# If the two selected fields are not a match (do not have the same letters), the user is asked to press Enter. After that, the fields are concealed again.
# The game ends when all fields are revealed.
# The game counts the number of steps taken to complete the game and displays this number after winning the game.
if __name__ == "__main__":
   main()
