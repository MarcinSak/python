import card, deck, data

class Game():
    '''ask for move, check if win'''
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
   new_deck = deck.Deck()
   print(new_deck.all_cards[3])
   new_deck.shuffle_deck()
   print(new_deck.all_cards[3])