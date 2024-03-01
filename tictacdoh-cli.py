from tictacdoh import TicTacDoh

def game_loop(game: TicTacDoh):
    game_over = False

    while(not game_over):
        
        draw_board(game.board)
        
        name = game.player[game.current_player_turn]

        print(f"Player {name}'s turn")
        x = input("What square do you want? ")
        
        game.player_turn(int(x))

        game_over_state = game.check_for_win()
        if(game_over_state == 0):
            print("Player 1 wins")
            game_over = True
        elif(game_over_state == 1):
            print("Player 2 wins")
            game_over = True
        else:
            game.next_turn()

    print("Game over")

def draw_board(board):
    print("---|---|---")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("---|---|---")


def main():
    p1_name = input("Enter a name for player 1: ")
    p2_name = input("Enter a name for player 2: ")

    game = TicTacDoh()
    game.player = ((p1_name, p2_name))
    game.start_game()

    game_loop(game)

    print("Game ended")

if __name__ == "__main__":
    main()
    