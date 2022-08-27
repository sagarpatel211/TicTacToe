class TicTacToe:
    games_played = 0
    def __init__(self):
        self.board = ['-', '-', '-',
                      '-', '-', '-',
                      '-', '-', '-']
        self.current_player = "X"
        self.winner = None
        self.game_running = True
        TicTacToe.games_played += 1


game = TicTacToe()
print("Welcome to Tic Tac Toe:")
while(game.game_running):
    print(game.current_player + "'s turn!")
    game.game_running = False
    print(TicTacToe.games_played)