class Card:
    def __init__(self, suit: str, rank: int):
        self.suit = suit
        self.rank = rank

    def print_card(self):
        print(f"{self.rank} of {self.suit}")

sample1 = Card("Spades", 8)
sample1.print_card()

    
