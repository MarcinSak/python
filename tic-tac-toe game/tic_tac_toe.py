def display_board(board):
    spacing = "-"*11
    print(f"+{spacing}+")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"|{spacing}|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"|{spacing}|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print(f"+{spacing}+")

def count_X_or_O_in_board_line(board):
    occupied = 0
    for i in range(3,9,3):
        check = 3 - board[:i].count('')
        if check > occupied:
            occupied = check
    return occupied

def replace_in_list(to_be_replaced, replace_for, list_to_proceed):
    new_list = list_to_proceed
    for index, element in enumerate(list_to_proceed):
        if element == to_be_replaced:
            new_list[index] = replace_for
    return new_list
    

example0_board = ['_','_','_','_','_','_','_','_','_']
example1_board = ['O', 'X', '_', 'O', 'X', '_', 'O', '_', '_']
example2_board = ['O', 'X', 'X', 'O', 'X', '_', 'O', '_', '_']
example3_board = ['O', '_', '_', 'O', '_', '_', 'O', '_', '_']

display_board(example0_board)


players = {}

def get_player_name(player_no):
    return input(f"Player{player_no} name: ")

def get_player_sign():
    char = None
    accepted_chars = ['X', 'O']
    while char not in accepted_chars:
        char = input("Which sigh do you prefer? Please choose X or O: ").upper()
        if char not in accepted_chars:
            print(f"Wrong, you have provided {char}, expected was X or O.")
    return char

players["player1"] = {'name': f'{get_player_name(1)}', 'sign': f'{get_player_sign()}'}
players["player2"] = {
    'name': get_player_name(2),
    'sign': 'O' if players["player1"]['sign'] == 'X' else 'X'
}
print(players)