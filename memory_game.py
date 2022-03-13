from multiprocessing.sharedctypes import Value
import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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
            return row - 1, column - 1
        except ValueError:
            print("Invalid input! Try again... ")
            valid = False


def display_menu():
    print("Select a difficulty level. Enter the corresponding number. ")
    print("0. Noob")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")


def get_difficulty():
    while True:
        display_menu()
        try:
            user_input = int(input("Select a difficulty level: "))
            if user_input == 1:
                return [5, 4]
            elif user_input == 2:
                return [5, 6]
            elif user_input == 3:
                return [5, 10]
            elif user_input == 0:
                return [2, 2]
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


def show_letter(gameboard, board, coordinates):
    row = coordinates[0]
    column = coordinates[1]
    gameboard[row][column] = board[row][column]
    return gameboard


def is_same_position(first_guess, second_guess, board):
    while True:
        try:
            if second_guess != first_guess:
                row2 = second_guess[0]
                col2 = second_guess[1]
                return row2, col2
            else:
                raise ValueError
        except ValueError:
            print("Don't choose the same position!")
            second_guess = get_user_field_position(board)
            row2 = second_guess[0]
            col2 = second_guess[1]
            continue


def cont():
    press_enter = input("Press Enter to continue...")
    while press_enter != "":
        press_enter = input("Press Enter to continue")
    console_clear()


def is_complete(gameboard):
    check = len(gameboard*len(gameboard[0]))
    hash_count = 0
    while check > 0:
        for row in gameboard:
            for item in row:
                if item == "#":
                    hash_count += 1
                check -= 1
        if hash_count == 0:
            print("YOU WIN!")
            return True


def set_board(gameboard, board, guess1, guess2):
    row1 = guess1[0]
    col1 = guess1[1]
    row2 = guess2[0]
    col2 = guess2[1]
    # match
    if board[row1][col1] == board[row2][col2]:
        gameboard[row1][col1] = board[row1][col1]
        gameboard[row2][col2] = board[row2][col2]
        return True
    else:
        gameboard[row1][col1] = "#"
        gameboard[row2][col2] = "#"
        return False


def save_guesses(guess, match):
    if match:
        return guess


def get_pair(gameboard, board, matches):
    pair = {}
    attempt = 0
    while attempt < 2:
        try:
            attempt += 1
            print(f"Enter value nr {attempt}...")
            guess = get_user_field_position(board)
            pair[attempt] = guess
            if pair[attempt] in matches:
                raise ValueError
            elif attempt == 2 and pair[2] == pair[1]:
                raise ValueError
            elif attempt == 2:
                draw_board(show_letter(gameboard, board, guess))
            elif guess in pair:
                raise ValueError
            draw_board(show_letter(gameboard, board, guess))
        except ValueError:
            if attempt == 2:
                print("Try again! That field is already revealed")
                attempt = 1
            if pair[attempt] in matches:
                print("Try again! That field is already revealed")
                attempt = 0
    match = set_board(gameboard, board, pair[1], pair[2])
    if match:
        print("Match!")
    return [pair[1], pair[2]]


def run_game(gameboard, board):
    matches = set()
    steps = 1
    while not is_complete(gameboard):
        pair = get_pair(gameboard, board, matches)
        for item in pair:
            match = set_board(gameboard, board, pair[0], pair[1])
            if match:
                matches.add(item)
        is_same_position(pair[0], pair[1], board)
        cont()
        draw_board(gameboard)
        steps += 1
    print(f"\nYou took {steps} steps to complete the game! ")


def main():
    print("Welcome to Memory Game!")
    board_size = get_difficulty()
    console_clear()
    board = generate_board(board_size[0], board_size[1])
    gameboard = hide(board)
    draw_board(hide(board))
    run_game(gameboard, board)


if __name__ == "__main__":
    main()
