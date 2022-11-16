import unittest
from tictactoe import *

class TestTicTacToeShould(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()
        
    def test_GiveNextPlayer(self):
        
        player = self.game.GetNextPlayer()

        self.assertEqual(player, "X", "Should start with player X")
        
    def test_GiveSecondPlayer(self):
        
        self.game.Play(1)
        player = self.game.GetNextPlayer()

        self.assertEqual(player, "O", "Should start with player O")
        
    def test_GiveThirdPlayer(self):
        
        self.game.Play(1)
        self.game.Play(2)
        player = self.game.GetNextPlayer()

        self.assertEqual(player, "X", "Should start with player X")
        
    def test_NotBeAbleToPlayOnPlayedSquare(self):
        
        self.game.Play(1)
        canPlay = self.game.Play(1)
        
        self.assertEqual(canPlay, False)
        
    def test_BeAbleToPlayOnUnPlayedSquare(self):
        
        canPlay = self.game.Play(1)
        
        self.assertEqual(canPlay, True)

    def test_WinnerO123(self):
        
        self.game.Play(5)
        self.game.Play(1)
        self.game.Play(6)
        self.game.Play(2)
        self.game.Play(9)
        self.game.Play(3)
        winner = self.game.GetWinner()

        self.assertEqual(winner, "O", "Should have O as winner")
        
    def test_WinnerX123(self):
        
        self.game.Play(1)
        self.game.Play(6)
        self.game.Play(2)
        self.game.Play(9)
        self.game.Play(3)
        winner = self.game.GetWinner()

        self.assertEqual(winner, "X", "Should have X as winner")
        
    def test_NoWinnerWhenNoPlays(self):
        

        winner = self.game.GetWinner()

        self.assertEqual(winner, None, "Should have no winner")
        
        
        