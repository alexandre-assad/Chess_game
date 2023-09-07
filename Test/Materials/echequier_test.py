import unittest
from Materials.Cavalier import Cavalier
from Materials.Echequier import Echequier
from Materials.Empty import Empty
from Coup import Coup

class TestEchequier(unittest.TestCase):
    
    def test_setup(self):
        Echequier_1 = Echequier()
        self.assertEqual(Echequier_1.board[4][4].letter," ")
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
        self.assertEqual(Echequier_1.board[0][1].letter," ")
        self.assertEqual(Echequier_1.board[2][2].letter,"C")
    
    def test_promote_pion(self):
        pass


    def test_pointer(self):
        Echequier_1 = Echequier()
        self.assertEqual(Echequier_1.pointer([1,1],"w"),True)
        self.assertNotEqual(Echequier_1.pointer([4,1],"w"),True)
        self.assertEqual(Echequier_1.pointer([8,4],"b"),True)

    
    def test_set_attack(self):
        Echequier_1 = Echequier()
        Echequier_1[1][0] = Empty(2,1)
        Echequier_1.set_attack()
        self.assertEqual(Echequier_1[0][0].is_attacked,True)