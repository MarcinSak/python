from players import *

def display_board(board):
    spacing = "-"*11
    print(f"+{spacing}+")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"|{spacing}|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"|{spacing}|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print(f"+{spacing}+")


def get_available_fields(board):
    return [str(i) for i, e in enumerate(board) if e == "_"]


def ask_for_next_move(available_fields, player, sign):
    next_move = None
    while next_move not in available_fields:
        next_move = input(f"{player}, where would you place {sign} next from (0-8): ")

        if next_move not in available_fields:
            print(f"Invalid move: {next_move}. Available moves are: {available_fields}.")
    return int(next_move)


def check_win(last_move, board):
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


players = create_players()
player = players[list(players.keys())[0]]
board = ['_'] * 9

display_board(board)

for i in range(9):
    available_fields = get_available_fields(board)
    next_move = ask_for_next_move(available_fields, player['name'], player['sign'])
    next_move = int(next_move)
    board[next_move] = player['sign']
    display_board(board)
    if check_win(next_move, board):
        print(f"{player['name']} has won. Congratulations!")
        break
    else:
        player = switch_player(player, players)
else:
    print("It's a draw!")
