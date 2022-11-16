
class TicTacToe:
    def __init__(self):
        self._player = "X"
        self.board = [None for x in range(10)]
        return

    def GetNextPlayer(self):
        return self._player
    
    def Play(self, square):

        if self.board[square] != None:
            return False
    
        self.board[square] = self._player
        self.NextPlayer()
        
        return True
            

    def NextPlayer(self):
        if self._player == "X":
            self._player = "O"
        else:
            self._player = "X"
            
    def GetWinner(self):
        if self.board[1] == self.board[2] == self.board[3] and self.board[1] != None:
            return self.board[1]