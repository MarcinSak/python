"""
Contains data structures related to the card game, such as the suits, ranks, and their 
corresponding values. This module provides the foundational information for creating a 
deck of cards.
"""

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Joker", "Queen", "King", "Ace"]
values = {rank: index + 2 for index, rank in enumerate(ranks)}
