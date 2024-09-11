import card
class Game():
    '''ask for move, check if win'''
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    two_of_hearts = card.Card("Two", "Hearts")
    five_of_spades = card.Card(rank="Five", suit="Spades")
    print(two_of_hearts.value < five_of_spades.value)