import unittest
from Materials.Echequier import Echequier
from Materials.Fou import Fou
from Coup import Coup

class TestFou(unittest.TestCase):

    def test_generate_moves(self):
        Echequier_1 = Echequier()
        Echequier_1.play_move(Coup(Echequier_1.board[1][1],3,2))
        self.assertEqual(Echequier.board[0][2].generate_moves(),[[Fou("w",1,3),2,2],[Fou("w",1,3),3,1]])