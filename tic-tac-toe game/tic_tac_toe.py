def display_board(board):
    spacing = "-"*11
    print(f"+{spacing}+")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"|{spacing}|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"|{spacing}|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print(f"+{spacing}+")


def get_player_name(player_no):
    return input(f"Player {player_no}, please enter your name: ")


def get_player_sign():
    char = None
    accepted_chars = ['X', 'O']
    while char not in accepted_chars:
        char = input("Which sign do you prefer? 'X' or 'O'? ").upper()
        if char not in accepted_chars:
            print("Invalid choice. Please choose 'X' or 'O'.")
    return char


def create_players():
    player1 = {
        'name': get_player_name(1),
        'sign': get_player_sign()
    }

    player2 = {
        'name': get_player_name(2),
        'sign': 'O' if player1['sign'] == 'X' else 'X'
    }
    return {'player1': player1, 'player2': player2}


def switch_player(current_player):
    return players['player2'] if current_player == players['player1'] else players['player1']


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
WIN = False
board = ['_'] * 9

display_board(board)

for i in range(9):
    available_fields = get_available_fields(board)
    next_move = ask_for_next_move(available_fields, player['name'], player['sign'])
    next_move = int(next_move)
    board[next_move] = player['sign']
    display_board(board)
    WIN = check_win(next_move, board)
    if WIN:
        print(f"{player['name']} has won. Congratulations!")
        break
    else:
        player = switch_player(player)
else:
    print("It's a draw!")
