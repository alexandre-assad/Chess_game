import unittest
from Materials.Echequier import Echequier
from Materials.Pion import Pion
from Materials.Tour import Tour
from Coup import Coup

class TestTour(unittest.TestCase):

    def test_generate_moves(self):
        Echequier_1 = Echequier()
        Echequier_1.board[0][1]= " "
        Toura1 = Echequier_1.board[0][0]
        self.assertEqual(Toura1.generate_moves(Echequier_1),[[Toura1,2,1],[Toura1,3,1],[Toura1,4,1],[Toura1,5,1],[Toura1,6,1],[Toura1,7,1]])