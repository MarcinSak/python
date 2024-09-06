from players import create_players, switch_player
from board import display_board, get_available_fields, ask_for_next_move, check_win

def play():
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
        
if __name__ == '__main__':
    play()