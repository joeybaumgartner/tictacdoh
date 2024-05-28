class TicTacDoh:
    
    def __init__(self):
        self.player = (("Player 1", "Player 2"))
        self.mark = (("X", "O"))
        self.current_player_turn = 0
        self.board = list((" ", " ", " ", " ", " ", " ", " ", " ", " "))
        self.game_started = False
        self.valid_move = True     # added object for screening if move is valid
        self.alert_message = ""    # created a bucket to send out a message

    def reset(self):
        self.player = (("Player 1", "Player 2"))
        self.mark = (("X", "O"))
        self.current_player_turn = 0
        self.board = list((" ", " ", " ", " ", " ", " ", " ", " ", " "))
        self.game_started = False
        self.valid_move = True     # added object for screening if move is valid
        self.alert_message = ""    # created a bucket to send out a message

    def player_turn(self, x: int):
        if "X" not in self.board[x] and "O" not in self.board[x]:     #checks if the game space is empty, if so, move is valid
            self.valid_move = True
            self.board[x] = self.mark[self.current_player_turn]
        else: self.valid_move = False
            
    def get_current_player(self) -> int:
        """Returns the number representing the current player.

        Parameters:
        self (object): Current object.

        Returns:
        int: Current number of players.
    
        """
        
        return self.current_player_turn

    def get_current_player_name(self) -> str:
        return self.player[self.current_player_turn].name

    def check_for_win(self) -> int:

        # All possible horizontal, vertical, and diagonal win states

        win_states = ((0, 1, 2), (3, 4, 5), (6, 7, 8), \
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), \
                        (0, 4, 8), (2, 4, 7))
        for m in self.mark:
            for w in win_states:
                if self.board[w[0]] == self.board[w[1]] == self.board[w[2]] and self.board[w[0]] != ' ': 
                    return self.get_current_player()
           
        return -1
    
    def start_game(self):
        self.game_started = True

    def next_turn(self):      
        if self.valid_move == True:     #if move is valid, clear the alert message and progress with next player
            self.alert_message = ""
            self.current_player_turn = (self.current_player_turn + 1) % 2
        else:
            self.alert_message = "Invalid Move!"     #send alert message that move is not valid
            