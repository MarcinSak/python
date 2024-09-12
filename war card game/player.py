import card
class Player():
    def __init__(self, name: str):
        print(f"Player {name} created")
        self.name = name
        self.all_cards = []
    def remove_one(self) -> card.Card:
        return self.all_cards.pop(0)
        
    def add_one(self, card) -> None:
        if type(card) == type([]):
            self.all_cards.extend(card)
        else:
            self.all_cards.append(card)
    def __str__(self) -> str:
        return f"Player: {self.name}, has {len(self.all_cards)} cards"
    def __len__(self) -> int:
        return len(self.all_cards)
