import card, deck, data, player

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
        player_one.add_one(card=new_deck.deal_one())
        player_two.add_one(card=new_deck.deal_one())
    
    # Set counter
    round_no = 0
    game_on = True

    # Game
    while game_on:
        if round_no > 50: break

        # Check if players still have cards to play
        if len(player_one) == 0 or len(player_two) == 0:
            game_on = False
            if len(player_one) > len(player_two):
                print(f"Player {player_one.name} WON!")
            else:
                print(f"Player {player_two.name} WON!")
            break

        round_no += 1
        print(f"Round {round_no}")
        # print(f"{str(player_one)}  |  {player_one.all_cards[0]}")
        # print(f"{str(player_two)}  |  {player_two.all_cards[0]}")

        cards = []

        while True:
            print(f"{str(player_one)}  |  {player_one.all_cards[0]}")
            print(f"{str(player_two)}  |  {player_two.all_cards[0]}")
            # Card comparsion
            if player_one.all_cards[0].value > player_two.all_cards[0].value:
                print("Player ONE takes the cards")
                cards.extend([player_one.remove_one(), player_two.remove_one()])
                print(f"DEBUG: pl 1 cards number before add: {len(player_one)}")
                player_one.add_one(cards)
                print(f"DEBUG: pl 1 cards number after  add: {len(player_one)}")
                break
            elif player_one.all_cards[0].value < player_two.all_cards[0].value:
                print("Player TWO takes the cards")
                cards.extend([player_one.remove_one(), player_two.remove_one()])
                print(f"DEBUG: pl 2 cards number before add: {len(player_two)}")
                player_two.add_one(cards)
                print(f"DEBUG: pl 2 cards number after  add: {len(player_two)}")
                break
            else:
                print("-------")
                print("- WAR -")
                print("-------")
                print("DEBUG:", player_one, player_two)
                # each player draw 5 extra cards
                # checking the 5th card only
                # if player do not have 5 cards, he loose
                # if non of the players has 5 cards, there is a draw, game over
                if len(player_one) < 6 and len(player_two) < 6:
                    print("Non of the players can declare a war. This is a Draw!")
                    game_on = False
                    break
                elif len(player_one) < 6:
                    print(f"Plyer {player_one.name} is unable to declare a war. Player: {player_two.name} is a WINNER")
                    game_on = False
                    break
                elif len(player_two) < 6:
                    print(f"Plyer {player_two.name} is unable to declare a war. Player: {player_one.name} is a WINNER")
                    game_on = False
                    break
                else:
                    print("Each player draw 5 extra cards")
                    for _ in range(5):
                        cards.append(player_one.remove_one())
                        cards.append(player_two.remove_one())
            for c in cards: print(str(c))
                    
