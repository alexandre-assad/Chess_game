import unittest
from Materials.Echequier import Echequier
from Materials.Pion import Pion
from Materials.Roi import Roi
from Materials.Empty import Empty
from Coup import Coup

class TestRoi(unittest.TestCase):

    def test_generate_moves(self):
        Echequier_1 = Echequier()
        Roiblanc = Echequier_1.board[0][4]
        Echequier_1.play_move(Coup(Roiblanc,3,5))
        PionDef = Pion("b",4,5)
        PionDef.is_defended=True
        Echequier_1.board[3][4] = PionDef
        self.assertEqual(Roiblanc.generate_moves(Echequier_1),[[Roiblanc,3,4],[Roiblanc,3,6],[Roiblanc,4,4],[Roiblanc,4,6]])
        Echequier_2 = Echequier()
        Roiblanc = Echequier_2.board[0][4]
        Echequier_2.board[0][5], Echequier_2.board[0][6] = Empty(1,6), Empty(1,7)
        self.assertEqual(Roiblanc.generate_moves(Echequier_2),[[Roiblanc,1,6],[Roiblanc,1,7]])
    

    def test_rock_possible(self):
        Echequier_1 = Echequier()
        Roiblanc = Echequier_1.board[0][4]
        self.assertEqual(Roiblanc.rock_possible(Echequier_1),[])
        Echequier_1.board[0][5], Echequier_1.board[0][6] = Empty(1,6), Empty(1,7)
        self.assertEqual(Roiblanc.rock_possible(Echequier_1),[[Roiblanc,1,7]])
        Echequier_1.board[0][5].is_attacked = True
        self.assertEqual(Roiblanc.rock_possible(Echequier_1),[])