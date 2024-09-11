import os

def display_board(board):
    """Clears the screen and displays the current state of the game board."""
    os.system('cls' if os.name == 'nt' else 'clear')
    spacing = "-"*11
    print(f"+{spacing}+")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"|{spacing}|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"|{spacing}|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print(f"+{spacing}+")


def get_available_fields(board):
    """Returns a list of available fields on the board where players can make a move."""
    return [str(i) for i, e in enumerate(board) if e == "_"]


def ask_for_next_move(available_fields, player, sign):
    """Prompts the current player to choose a valid move from the available fields."""
    next_move = None
    while next_move not in available_fields:
        next_move = input(f"{player}, where would you place {sign} next from (0-8): ")

        if next_move not in available_fields:
            print(f"Invalid move: {next_move}. Available moves are: {available_fields}.")
    return int(next_move)


def check_win(last_move, board):
    """Checks if the last move resulted in a win by comparing it to possible winning combinations."""
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combination in winning_combinations:
        if last_move in combination:
            if board[combination[0]] == board[combination[1]] == board[combination[2]]:
                return True
    return False
