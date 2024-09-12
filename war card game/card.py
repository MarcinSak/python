"""
Defines the Card class, representing a single card in the deck. Each card has a rank, 
suit, and value. The module also provides a method for string representation of the card.
"""
import data

class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    @property
    def value(self) -> int:
        return int(data.values[self.rank])

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit} ({self.value})"
