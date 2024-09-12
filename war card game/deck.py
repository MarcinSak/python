'''Deck operations'''
from random import shuffle
import data, card

class Deck():
    def __init__(self):
        print("New deck created")
        self.all_cards = []
        for rank in data.ranks:
            for suit in data.suits:
                card_created = card.Card(rank=rank, suit=suit)
                self.all_cards.append(card_created)
        print(f"{len(self.all_cards)} cards created.")

    def shuffle_deck(self) -> None:
        shuffle(self.all_cards)

    def deal_one(self) -> card.Card:
        return self.all_cards.pop()
