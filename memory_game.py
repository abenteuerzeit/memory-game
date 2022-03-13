import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_board(rows, columns):
    try:
        ammount_of_letters = rows * columns
        pairs = []
        for letter in range(int(ammount_of_letters/2)):
            pair = random.choice(alphabet)
            pairs.append(pair)
            pairs.append(pair)
        if ammount_of_letters > len(alphabet)*2 or ammount_of_letters % 2 != 0:
            raise ValueError
        else:
            matrix = []
            for i in range(rows):
                row = []
                for value in range(columns):
                    select = random.choice(pairs)
                    row.append(select)
                    pairs.remove(select)
                matrix.append(row)
               # matrix.append([random.choice(pairs) for i in range(columns)])
            return matrix
    except ValueError:
        print("Error! \nEither the height or width is an odd number,")
        print("or not enough letters in the latin alphabet to generate the board.")


def get_user_field_position(board):
    valid = False
    while valid is False:
        height = len(board)
        try:
            user_position = input("Select field coordinates (such as B2): ")
            if user_position == "":
                raise ValueError
            if str.upper(user_position[0]) not in alphabet:
                raise ValueError
            if user_position[1:].strip().isdigit() is not True:
                raise ValueError
            if user_position[1:]:
                row = int(user_position[1:])
                if row <= 0:
                    raise ValueError
                if row > height:
                    raise ValueError
            if user_position[0]:
                if str.upper(user_position[0]) > alphabet[len(board[0])-1]:
                    raise ValueError
            for count, letter in enumerate(alphabet):
                if letter == str.upper(user_position[0]):
                    column = count + 1
            valid = True
            print("The input is valid, the coordinates are: ")
            print(row - 1, column - 1)
            return row - 1, column - 1
        except ValueError:
            print("Invalid input! Try again... ")
            valid = False


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
    width = len(board[0])
    columns = [letter for letter in alphabet[:width]]
    print("\n     " + " ".join(columns) + "\n")
    for count, row in enumerate(board):
        print(f"{count + 1}    " + " ".join(row))
    print("")


def hide(board):
    rowlength = len(board[0])
    hidden = []
    rows = len(board)
    for row in range(rows):
        hidden.append(["#" for i in range(rowlength)])
    return hidden

def show_letter(board):
    pass
# During the game, the fields can be either concealed or revealed.
# The letter of the field is displayed only when the field is revealed.
# When the field is concealed, # is displayed.
# The terminal window is cleaned every time the board is redrawn.


def main():
    gameboard = []
    print("Welcome to Memory Game!")
    board_size = get_difficulty()
    console_clear()
    height = board_size[0]
    width = board_size[1]
    board = generate_board(height, width)
    draw_board(hide(board))
    print(hide(board))
    print(board)
    select = get_user_field_position(board)
    # gameboard[select] = board[select]

# The board is displayed to the user.
# The game asks asked to select a field, which is then revealed (its letter is being shown on the redrawn board).
# The game asks to select another field, which is then revealed (its letter is being shown on the redrawn board).
# If the two selected fields are a match (have the same letter), they remain revealed for the rest of the game.
# If the two selected fields are not a match (do not have the same letters), the user is asked to press Enter.
# After that, the fields are concealed again.
# The game ends when all fields are revealed.
# The game counts the number of steps taken to complete the game and displays this number after winning the game.


if __name__ == "__main__":
    main()
