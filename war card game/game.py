import card, deck, data, player

if __name__ == "__main__":
   # game set-up
   player_one = player.Player("One")
   player_two = player.Player("Two")
   new_deck = deck.Deck()
   new_deck.shuffle_deck()
   
   # start game