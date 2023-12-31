import unittest 
from Materials.Echequier import Echequier
from Materials.Cavalier import Cavalier
from Materials.Pion import Pion
from Materials.Empty import Empty
from Coup import Coup 

class TestCavalier(unittest.TestCase):


    def test_generate_moves(self):
        Echequier_1 = Echequier()
        Cavalierb1 = Echequier_1.board[0][1]
        Echequier_1.board[1][3] = Empty(2,4)
        self.assertEqual(Cavalierb1.generate_moves(Echequier_1),[[Cavalierb1,2,4],[Cavalierb1,3,3],[Cavalierb1,3,1]])