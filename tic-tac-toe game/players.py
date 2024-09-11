
"""Module for handling player creation and player switching logic in a Tic-Tac-Toe game."""
def get_player_name(player_no):
    """Prompts the player to enter their name based on player number."""
    return input(f"Player {player_no}, please enter your name: ")


def get_player_sign():
    """Asks the player to choose between 'X' or 'O'. Keeps prompting until a valid choice is made."""
    char = None
    accepted_chars = ['X', 'O']
    while char not in accepted_chars:
        char = input("Which sign do you prefer? 'X' or 'O'? ").upper()
        if char not in accepted_chars:
            print("Invalid choice. Please choose 'X' or 'O'.")
    return char


def create_players():
    """Creates two players, assigning one the 'X' sign and the other 'O'."""
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
    """Switches between player1 and player2."""
    return players['player2'] if current_player == players['player1'] else players['player1']
