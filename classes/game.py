# Implement as a state machine
class LoveLetter:

    def __init__(self, players: List[Player]):
        # set players from user as input
        self.players = players
        # create the Deck: List[Card]
        # Positions: List[Player] --> inherent by user input
        # Dealer: Player, random player --> helps to start turns since player to left starts first
