import card
from random import shuffle

class Player():
    def __init__(self, name: str):
        print(f"Player {name} created")
        self.name = name
        self.all_cards = []
    def remove_one(self) -> card.Card:
        return self.all_cards.pop(0)
        
    def add_cards(self, cards) -> None:
        if type(cards) == type([]):
            shuffle(cards)
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)
    def __str__(self) -> str:
        return f"Player: {self.name}, has {len(self)} cards"
    def __len__(self) -> int:
        return len(self.all_cards)
