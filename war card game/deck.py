"""
This module handles the creation and management of a deck of cards. It includes methods 
for shuffling the deck and dealing cards to players.
"""

from random import shuffle
import data, card

class Deck:
    def __init__(self):
        print("New deck created")
        self.all_cards = []
        for rank in data.ranks:
            for suit in data.suits:
                card_created = card.Card(rank=rank, suit=suit)
                self.all_cards.append(card_created)
        if len(self.all_cards) != 52:
            raise ValueError("Deck should contain exactly 52 cards.")
        print(f"{len(self.all_cards)} cards created.")

    def shuffle_deck(self) -> None:
        if not self.all_cards:
            raise ValueError("Cannot shuffle an empty deck.")
        shuffle(self.all_cards)

    def deal_one(self) -> card.Card:
        if not self.all_cards:
            raise ValueError("Cannot deal from an empty deck.")
        return self.all_cards.pop()
