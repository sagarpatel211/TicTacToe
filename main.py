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
    
    def print_board(self):
        for i in range(0, 9):
            if ((i + 1) % 3 == 0):
                print(self.board[i])
                print("---------")
            else:
                print(self.board[i] + " | ", end = "")

    def check_winner(self, board):
        # Horizontal
        for i in range(0, 9, 3):
            if (board[i] == board[i + 1] == board[i + 2] and board[i] != "-"):
                self.winner = board[i]
        # Vertical
        for i in range(0, 3):
            if (board[i] == board[i + 3] == board[i + 6] and board[i] != "-"):
                self.winner = board[i]
        # Diagonal
        if (board[0] == board[4] == board[8] and board[0] != "-"):
            self.winner = board[0]
        if (board[2] == board[4] == board[6] and board[2] != "-"):
            self.winner = board[0]

        if self.winner != None:
            print("The winner is: " + self.winner + "!")
            self.game_running = False
            return
        if "-" not in board:
            self.winner = "Tie"
            self.game_running = False
        else:  
            if (self.current_player == "X"):
                self.current_player = "O"
            else:
                self.current_player = "X"

    def player_turn(self):
        result = None
        while result is None:
            selection = input("Select number from 1 - 9: ")
            try:
                result = int(selection)
                if (not (result >= 1 and result <= 9)):
                    raise Exception("Out of range")
                if (not (self.board[result - 1] == "-")):
                    raise Exception("Position already taken")
            except:
                pass
            else:
                self.board[result - 1] = self.current_player
                self.check_winner(self.board)


game = TicTacToe()
# game.print_board(game.board)
print("Welcome to Tic Tac Toe:")
while(game.game_running):
    game.print_board()
    print(game.current_player + "'s turn!")
    game.player_turn()
