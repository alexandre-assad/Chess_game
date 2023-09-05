import unittest
from Materials.Echequier import Echequier
from Materials.Pion import Pion
from Materials.Fou import Fou
from Coup import Coup

class TestFou(unittest.TestCase):

    def test_generate_moves(self):
        Echequier_1 = Echequier()
        Echequier_1.play_move(Coup(Echequier_1.board[1][1],3,2))
        self.assertEqual(Echequier_1.board[0][2].generate_moves(Echequier_1),[[Echequier_1.board[0][2],2,2],[Echequier_1.board[0][2],3,1]])
        Echequier_1.board[2][0] = Pion("w",3,1)
        self.assertNotEqual(Echequier_1.board[0][2].generate_moves(Echequier_1),[[Echequier_1.board[0][2],2,2],[Echequier_1.board[0][2],3,1]])
        Echequier_1.board[2][0] = Pion("b",3,1)
        self.assertEqual(Echequier_1.board[0][2].generate_moves(Echequier_1),[[Echequier_1.board[0][2],2,2],[Echequier_1.board[0][2],3,1]])
        