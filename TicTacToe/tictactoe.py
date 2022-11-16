
class TicTacToe:
    def __init__(self):
        self.player = "X"
        self.board = [None for x in range(10)]
        return

    def GetNextPlayer(self):
        return self.player
    
    def Play(self, square):

        if self.board[square] != None:
            return False
    
        self.board[square] = self.player
        self.NextPlayer()
        
        return True
            

    def NextPlayer(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"
            
    def GetWinner(self):
        if self.WinnerInRow(1,2,3):
            return self.board[1]
        
        if self.WinnerInRow(4,5,6):
            return self.board[4]
        
        if self.WinnerInRow(7,8,9):
            return self.board[7]
        
        if self.WinnerInRow(7,4,1):
            return self.board[7]
        
        if self.WinnerInRow(8,5,2):
            return self.board[8]
        
        if self.WinnerInRow(9,6,3):
            return self.board[9]
        
        if self.WinnerInRow(7,5,3):
            return self.board[7]
        
        if self.WinnerInRow(9,5,1):
            return self.board[9]
        
        if None in self.board[1:10]:
            return None
        
        return "Tie"

    def WinnerInRow(self, first, second, third):
        return self.board[first] == self.board[second] == self.board[third] and self.board[first] != None