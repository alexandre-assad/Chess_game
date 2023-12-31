import unittest
from Materials.Echequier import Echequier
from Materials.Pion import Pion
from Coup import Coup

class TestPion(unittest.TestCase):

    def test_generate_moves(self):
        Echequier_1 = Echequier()
        Piona2 = Echequier_1.board[1][0]
        self.assertEqual(Piona2.generate_moves(Echequier_1),[[Piona2,3,1],[Piona2,4,1]])
        Echequier_1.board[4][0] = Pion("b",5,1)
        Echequier_1.play_move(Coup(Piona2,4,1))
        self.assertEqual(Piona2.generate_moves(Echequier_1),[])
        Echequier_1.board[4][1] = Pion("b",5,2)
        self.assertEqual(Piona2.generate_moves(Echequier_1),[[Piona2,5,2]])
        self.assertEqual(Echequier_1.board[6][4].generate_moves(Echequier_1),[[Echequier_1.board[6][4],6,5],[Echequier_1.board[6][4],5,5]])
        Echequier_1.board[3][1] = Pion("b",4,2)
        Echequier_1.play_move(Coup(Piona2,2,1))
        Piona2.en_passant = [3,2]
        self.assertEqual(Piona2.generate_moves(Echequier_1),[[Piona2,3,1],[Piona2,4,1],[Piona2,3,2]])
        Echequier_1.setup()
        Pione4 = Echequier_1.board[1][4]
        Echequier_1.play_move(Coup(Pione4,4,5))
        Echequier_1.board[4][3] = Pion("b",5,4)
        self.assertEqual(Pione4.generate_moves(Echequier_1),[[Pione4,5,5],[Pione4,5,4]])