import unittest
from Materials.Cavalier import Cavalier
from Materials.Echequier import Echequier
from Coup import Coup

class TestEchequier(unittest.TestCase):
    
    def test_setup(self):
        Echequier_1 = Echequier()
        self.assertEqual(Echequier_1.board[4][4]," ")
        self.assertEqual(Echequier_1.board[1][2].color,"w")
        self.assertEqual(Echequier_1.board[7][2].color,"b")
    
    def test_display(self):
        Echequier_1 = Echequier()
        self.maxDiff = None
        self.assertEqual(Echequier_1.display(),
"""[[T],[C],[F],[D],[R],[F],[C],[T]],
[[P],[P],[P],[P],[P],[P],[P],[P]],
[[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ]],
[[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ]],
[[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ]],
[[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ]],
[[P],[P],[P],[P],[P],[P],[P],[P]],
[[T],[C],[F],[D],[R],[F],[C],[T]]""")
    
    
    def test_evaluate(self):
        pass
    
    
    def test_play_move(self):
        Echequier_1 = Echequier()
        Echequier_1.play_move(Coup(Echequier_1.board[0][1],3,3))
        self.assertEqual(Echequier_1.board[0][1]," ")
        self.assertEqual(Echequier_1.board[2][2].letter,"C")
    
    def test_promote_pion(self):
        pass