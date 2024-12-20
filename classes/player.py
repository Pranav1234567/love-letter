from typing import List
from interface.card import Card
from errors.invalid_play_error import InvalidPlayError

class Player:
    
    def __init__(self, name: str):
        # str
        self.name = name
        # List[Card]
        self.hand: List[Card] = []
        self.is_current_player = False
    
    # getters and setters
    def set_hand(self, card: Card):
        self.hand = [card]

    def get_hand(self):
        return self.hand
    
    def get_is_current_player(self):
        return self.is_current_player
    
    def set_is_current_player(self, is_current_player):
        self.is_current_player = is_current_player

    # player operations
    def pick_from_deck(self, card: Card):
        self.hand.append(card)
    
    def play(self, card: Card, other_player: Player):
        try:
            if card not in self.hand:
                raise InvalidPlayError('bad play')

            #TODO invoke card action
            other_player

            # remove card from hand
            self.hand.remove(card)

        except InvalidPlayError as e:
            print('Error: ', e)