suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Joker", "Queen", "King", "Ace"]
values = {f"{rank}": f"{index+2}" for index, rank in enumerate(ranks)}

cards = [
    {"rank": rank, "suit": suit, "value": index + 2}
    for index, rank in enumerate(ranks)
    for suit in suits
]