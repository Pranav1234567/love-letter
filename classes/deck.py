from typing import List
from interface.card import Card

class Deck:
    def __init__(self):
        self.deck: List[Card] = []
        self.disard: List[Card] = []

    def pick(self):
        pass

    # optional lol
    def shuffle(self):
        pass