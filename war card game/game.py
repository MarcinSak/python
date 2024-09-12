import deck, player
from random import shuffle

class Game():
    def __init__(self):
        # Game set-up
        self.player_one = player.Player("One")
        self.player_two = player.Player("Two")
        self.new_deck = deck.Deck()
        self.round_no = 0
        self.game_on = True
        
        # Shuffle and deal cards
        self.new_deck.shuffle_deck()
        for _ in range(26):
            self.player_one.add_cards(self.new_deck.deal_one())
            self.player_two.add_cards(self.new_deck.deal_one())

    def play_round(self):
        if len(self.player_one) == 0 or len(self.player_two) == 0:
            self.end_game()
            return
        
        print(f"Round {self.round_no + 1}")
        self.round_no += 1
        cards_on_table = []
        
        while True:
            print(f"{self.player_one}  |  next card is {self.player_one.all_cards[0]}")
            print(f"{self.player_two}  |  next card is {self.player_two.all_cards[0]}")
            
            if self.player_one.all_cards[0].value > self.player_two.all_cards[0].value:
                self.collect_cards(cards_on_table, self.player_one)
                break
            elif self.player_one.all_cards[0].value < self.player_two.all_cards[0].value:
                self.collect_cards(cards_on_table, self.player_two)
                break
            else:
                if not self.handle_war(cards_on_table):
                    return

    def handle_war(self, cards_on_table):
        print("-------\n- WAR -\n-------")
        if len(self.player_one) < 6 or len(self.player_two) < 6:
            self.end_game_draw_or_loss()
            return False
        else:
            print("Each player draws 5 extra cards")
            for _ in range(5):
                cards_on_table.append(self.player_one.remove_one())
                cards_on_table.append(self.player_two.remove_one())
            return True
    
    def collect_cards(self, cards_on_table, winner):
        cards_on_table.extend([self.player_one.remove_one(), self.player_two.remove_one()])
        shuffle(cards_on_table)
        winner.add_cards(cards_on_table)
        print(f"Player {winner.name} takes the cards")
        print()

    def end_game(self):
        self.game_on = False
        if len(self.player_one) > len(self.player_two):
            print(f"Player {self.player_one.name} is a WINNER!")
        else:
            print(f"Player {self.player_two.name} is a WINNER!")

    def end_game_draw_or_loss(self):
        if len(self.player_one) < 6 and len(self.player_two) < 6:
            print("Non of the players can declare a war. This is a Draw!")
        elif len(self.player_one) < 6:
            print(f"Player {self.player_one.name} cannot declare war. {self.player_two.name} is the WINNER!")
        else:
            print(f"Player {self.player_two.name} cannot declare war. {self.player_one.name} is the WINNER!")
        self.game_on = False

    def start(self):
        while self.game_on and self.round_no <= 100: # optional limitation
            self.play_round()


if __name__ == "__main__":
    game = Game()
    game.start()
