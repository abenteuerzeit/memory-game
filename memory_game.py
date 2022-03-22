import os
import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_board(rows, columns):
    try:
        if rows <= 0 or columns <= 0:
            raise ValueError
        ammount_of_letters = rows * columns
        pairs = []
        for letter in range(int(ammount_of_letters/2)):
            pair = random.choice(alphabet)
            pairs.append(pair)
            pairs.append(pair)
        if ammount_of_letters > len(alphabet)*2 or ammount_of_letters % 2 != 0 or ammount_of_letters <= 0:
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
        print("")
        error = "\n"+"    FATALITY! "*5 + "\n"
        print(error)
        print("\tEither the height or width is an odd number,")
        print("\tor not enough letters in the latin alphabet to generate the board.")
        print("\n\tEither way, these dimensions are crap since I can't generate pairs!")
        print("\tTry harder!")
        print(error)
        print("\n\n\t\t(╯°□°)╯︵ ┻━┻ \n\n")


def is_position_correct(user_position):
    is_empty = user_position == ""
    is_first_char_in_alphabet = str.upper(user_position[0]) not in alphabet
    is_second_char_digit = user_position[1:].strip().isdigit() is not True
    return is_empty and is_first_char_in_alphabet and is_second_char_digit

def get_user_field_position(board):
    while True:
        height = len(board)
        try:
            user_position = input("Select field coordinates (such as B2): ")
            if is_position_correct(user_position):
                raise ValueError
            if user_position[1:]:
                row = int(user_position[1:])
                if row <= 0 and row > height:
                    raise ValueError
            if user_position[0]:
                if str.upper(user_position[0]) > alphabet[len(board[0])-1]:
                    raise ValueError
            for count, letter in enumerate(alphabet):
                if letter == str.upper(user_position[0]):
                    column = count + 1
            return row - 1, column - 1
        except ValueError:
            print("Invalid input! Try again... ")
            continue


def display_menu():
    tekst = '''
        Select a difficulty level. Enter the corresponding number. 
            0. Noob
            1. Easy
            2. Medium
            3. Hard
            4. Custom board size...
    '''
    print(tekst)


def get_difficulty():
    difficulties = {1: [5,4], 2: [5,6], 3: [5,10], 0: [2,2]}
    while True:
        display_menu()
        try:
            user_input = int(input("Enter level: "))

            if user_input in difficulties.keys():
                return difficulties[user_input]
            elif user_input == 4:
                while True:
                    try:
                        height = int(input("Enter how many rows you want as a whole number: "))
                        width = int(input("Enter how many columns you want as a whole number: "))
                        return height, width
                    except ValueError:
                        continue
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
        hidden.append(["#"]*rowlength)
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
            raise ValueError
        except ValueError:
            print("\nDon't choose the same position!")
            second_guess = get_user_field_position(board)
            row2, col2 = second_guess
            continue


def cont():
    press_enter = input("\tPress Enter to continue...")
    while press_enter != "":
        press_enter = input("\tPress Enter to continue")
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
    row1, col1 = guess1
    row2, col2 = guess2

    # match
    if board[row1][col1] == board[row2][col2]:
        gameboard[row1][col1] = board[row1][col1]
        gameboard[row2][col2] = board[row2][col2]
        return True
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
            # TODO move condition to separate def
            if pair[attempt] in matches and attempt == 2 and pair[2] == pair[1]:
                raise ValueError
            elif attempt == 2:
                console_clear()
                draw_board(show_letter(gameboard, board, guess))
            elif guess in pair:
                raise ValueError
            else:
                console_clear()
                draw_board(show_letter(gameboard, board, guess))
        except ValueError:
            if attempt == 2:
                print("\nTry again! That field is already revealed...")
                attempt = 1
            if pair[attempt] in matches:
                print("\nTry again! That field is already revealed...")
                attempt = 0
    match = set_board(gameboard, board, pair[1], pair[2])
    if match:
        print("\n\t"+":"*10)
        print("\t  Match!")
        print("\t"+":"*10+"\n")
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
    print("\n\tWelcome to Memory Game! \n")
    board_size = get_difficulty()
    console_clear()
    board = generate_board(board_size[0], board_size[1])
    if board:
        gameboard = hide(board)
        draw_board(hide(board))
        run_game(gameboard, board)


if __name__ == "__main__":
    main()
