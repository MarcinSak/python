"""
    Each player draws one card from their deck.
    The player with the higher card value wins the round and takes both cards.
    A "war" occurs when both players draw cards of the same value. In a war:
        If either player has fewer than 5 cards, the game ends in a draw.
        If one player has fewer than 5 cards, they lose the game.
        If both players have at least 5 cards, each draws 5 additional cards.
        The winner of the war is determined by comparing the value of the 5th drawn card. 
"""
import deck, player
from random import shuffle

if __name__ == "__main__":
    # game set-up
    # Player creation
    player_one = player.Player("One")
    player_two = player.Player("Two")
    
    # Deck preparation
    new_deck = deck.Deck()
    new_deck.shuffle_deck()

    # Deal cards
    for _ in range(26): # half of 52 cards deck
        player_one.add_cards(cards=new_deck.deal_one())
        player_two.add_cards(cards=new_deck.deal_one())
    
    # Set counter
    round_no = 0
    game_on = True

    # Game
    while game_on:
        if round_no > 70: break # optional limitation

        # Check if players still have cards to play
        if len(player_one) == 0 or len(player_two) == 0:
            game_on = False
            if len(player_one) > len(player_two):
                print(f"Player {player_one.name} is a WINNER!")
            else:
                print(f"Player {player_two.name} is a WINNER!")
            break

        round_no += 1
        print()
        print(f"Round {round_no}")
        # print(f"{str(player_one)}  |  {player_one.all_cards[0]}")
        # print(f"{str(player_two)}  |  {player_two.all_cards[0]}")

        cards_on_table = []

        while True:
            print(f"{str(player_one)}  |  next card is {player_one.all_cards[0]}")
            print(f"{str(player_two)}  |  next card is {player_two.all_cards[0]}")
            print(f"{len(cards_on_table)} cards on the table")
            # Card comparsion
            if player_one.all_cards[0].value > player_two.all_cards[0].value:
                print(f"Player {player_one.name} takes the cards")
                cards_on_table.extend([player_one.remove_one(), player_two.remove_one()])
                shuffle(cards_on_table)
                player_one.add_cards(cards_on_table)
                break
            elif player_one.all_cards[0].value < player_two.all_cards[0].value:
                print(f"Player {player_two.name} takes the cards")
                cards_on_table.extend([player_one.remove_one(), player_two.remove_one()])
                shuffle(cards_on_table)
                player_two.add_cards(cards_on_table)
                break
            else:
                print("-------")
                print("- WAR -")
                print("-------")
                game_on = False
                if len(player_one) < 6 and len(player_two) < 6:
                    print("Non of the players can declare a war. This is a Draw!")
                    break
                elif len(player_one) < 6:
                    print(f"Plyer {player_one.name} is unable to declare a war. Player: {player_two.name} is a WINNER")
                    break
                elif len(player_two) < 6:
                    print(f"Plyer {player_two.name} is unable to declare a war. Player: {player_one.name} is a WINNER")
                    break
                else:
                    game_on = True
                    print("Each player draw 5 extra cards")
                    for _ in range(5):
                        cards_on_table.append(player_one.remove_one())
                        cards_on_table.append(player_two.remove_one())
                    shuffle(cards_on_table)
            print("Cards on the table: ")
            for c in cards_on_table: print(str(c))
            print("____________________")
            print()
                    

