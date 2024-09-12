'''Assume 52-cards option'''
import data
class Card():
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = int(data.values[rank])
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit} ({self.value})"
