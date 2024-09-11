'''Assume 52-cards option'''
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Joker", "Queen", "King", "Ace"]
values = {f"{rank}": f"{index+2}" for index, rank in enumerate(ranks)}  

class Card():
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit} ({self.value})"
