class TicTacToe:
    def __init__(self):
        self.board = ['-', '-', '-',
                      '-', '-', '-',
                      '-', '-', '-']
        self.current_player = "X"

    def reset(self):
        self.board = ['-', '-', '-',
                      '-', '-', '-',
                      '-', '-', '-']
        self.current_player = "X"

print("hi")