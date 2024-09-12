suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Joker", "Queen", "King", "Ace"]
values = {f"{rank}": f"{index+2}" for index, rank in enumerate(ranks)}