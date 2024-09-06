
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


def switch_player(current_player, players):
    return players['player2'] if current_player == players['player1'] else players['player1']