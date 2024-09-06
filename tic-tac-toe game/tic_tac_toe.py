players = {}
BOARD = ['_'] * 9
PLAYER = None


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
    return input(f"Player{player_no} name: ")


def get_player_sign():
    char = None
    accepted_chars = ['X', 'O']
    while char not in accepted_chars:
        char = input("Which sign do you prefer? Please choose X or O: ").upper()
        if char not in accepted_chars:
            print(f"Wrong, you have provided {char}, expected was X or O.")
    return char


def create_players():
    players["player1"] = {
        'name': get_player_name(1),
        'sign': get_player_sign()
    }

    players["player2"] = {
        'name': get_player_name(2),
        'sign': 'O' if players["player1"]['sign'] == 'X' else 'X'
    }


def switch_player(current_player):
    return players['player2'] if current_player == players['player1'] else players['player1']


def get_available_fields(board):
    return [str(i) for i, e in enumerate(board) if e == "_"]


def ask_player_for_the_next_move(availible_fields, player, sign):
    next_move = None
    while next_move not in availible_fields:
        next_move = input(f"{player}, where would you place {
                          sign} next from (0-8): ")

        if next_move not in availible_fields:
            print(f"Wrong, you have provided {
                  next_move}, but availible are: {availible_fields}.")
    return int(next_move)


def check_win(move, board):
    move = int(move)
    lista = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for l in lista:
        if move in l:
            print(l)
            if board[l[0]] == board[l[1]] == board[l[2]]:
                print(f"{board[l[0]]} WINS")
                return True
    return False


# tests

example0_board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
example1_board = ['O', 'X', '_', 'O', 'X', '_', 'O', '_', '_']
example2_board = ['O', 'X', 'X', 'O', 'X', '_', 'O', '_', '_']
example3_board = ['O', '_', '_', 'X', '_', '_', 'O', '_', '_']

BOARD = example0_board
create_players()

PLAYER = players['player1']
WIN = False
for i in range(0, 9):
    print(f"current player is {PLAYER['name']}")
    display_board(BOARD)
    available_fields = get_available_fields(BOARD)
    next_move = int(ask_player_for_the_next_move(available_fields, PLAYER['name'], PLAYER['sign']))
    BOARD[next_move] = PLAYER['sign']
    WIN = check_win(next_move, BOARD)
    print("WIN?:", WIN)
    if WIN:
        print(f'{PLAYER['name']} has win. Congratulations!')
        break
    else:
        PLAYER = switch_player(PLAYER)
else:
    print("Draw")
