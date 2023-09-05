import unittest
from Materials.Echequier import Echequier
from Materials.Pion import Pion
from Materials.Roi import Roi
from Coup import Coup

class TestRoi(unittest.TestCase):

    def test_generate_moves(self):
        Echequier_1 = Echequier()
        Roiblanc = Echequier_1.board[0][4]
        Echequier_1.play_move(Coup(Roiblanc,3,5))
        PionDef = Pion("b",4,5)
        PionDef.is_defended=True
        Echequier_1.board[3][4] = PionDef
        self.assertEqual(Roiblanc.generate_moves(Echequier_1),[[Roiblanc,3,4],[Roiblanc,4,4],[Roiblanc,4,6],[Roiblanc,3,6]])