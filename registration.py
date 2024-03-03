from player import Player

class Registration:

    def __init__(self, player_count: int, minimum_to_start):
        self.player_count = player_count
        self.minimum_to_start = minimum_to_start
        self.players = []

    def register_user(self, player: Player):
        self.players.append(player)

    def at_capacity(self) -> bool:
        return len(self.players) == self.player_count
    
    def enough_to_start(self) -> bool:
        return len(self.players) >= self.minimum_to_start