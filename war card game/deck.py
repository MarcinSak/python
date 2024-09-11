'''Deck operations'''
import card
class Deck():
    def __init__(self, first_card: card.Card, second_card: card.Card) -> None:
        self.first_card = first_card
        self.second_card = second_card
    def __str__(self) -> str:
        return [self.first_card, self.second_card]
    def compare_cards(self):
        if self.first_card > self.second_card:
            print("First card is higher")
            return 1
        elif(self.first_card < self.second_card):
            print("Second card is higher")
            return 2
        else:
            print("Cards are the same")
            return 0
    