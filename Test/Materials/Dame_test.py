import unittest
from Materials.Echequier import Echequier
from Materials.Pion import Pion
from Materials.Dame import Dame
from Materials.Empty import Empty
from Coup import Coup

class TestDame(unittest.TestCase):

    def test_generate_moves(self):
        Echequier_1 = Echequier()
        Echequier_1.board[1][3] = Empty(2,4)
        Echequier_1.board[1][2] = Empty(2,3)
        Echequier_1.play_move(Coup(Pion("b",7,4),4,4))
        Damed1 = Echequier_1.board[0][3]
        self.assertEqual(Damed1.generate_moves(Echequier_1),[[Damed1,2,4],[Damed1,3,4],[Damed1,4,4],[Damed1,2,3],[Damed1,3,2],[Damed1,4,1]])