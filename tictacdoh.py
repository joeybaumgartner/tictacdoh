class TicTacDoh:

    def __init__(self):
        self.player = (("Player 1", "Player 2"))
        self.mark = (("X", "O"))
        self.current_player_turn = 0
        self.board = list((" ", " ", " ", " ", " ", " ", " ", " ", " "))
        self.game_started = False

    def player_turn(self, x: int):
        self.board[x] = self.mark[self.current_player_turn]

    def get_current_player(self) -> int:
        return self.current_player_turn

    def get_current_player_name(self) -> str:
        return self.player[self.current_player_turn]

    def check_for_win(self) -> int:

        # All possible horizontal, vertical, and diagonal win states

        win_states = ((0, 1, 2), (3, 4, 5), (6, 7, 8), \
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), \
                        (0, 4, 8), (2, 4, 7))
        for m in self.mark:
            for w in win_states:
                if self.board[w[0]] == self.board[w[1]] == self.board[w[2]] == m: 
                    return self.mark.index(m)
           
        return 2
    
    def start_game(self):
        self.game_started = True

    def next_turn(self):
        self.current_player_turn = (self.current_player_turn + 1) % 2