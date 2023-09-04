import unittest
from Materials.Echequier import Echequier
class TestEchequier(unittest.TestCase):
    
    def test_setup(self):
        Echequier_1 = Echequier()
        self.assertEqual(Echequier_1.board[4][4],"")
    
    
    def test_display(self):
        Echequier_1 = Echequier()
        self.assertEqual(Echequier_1.display(),
        """
        [[T],[C],[F],[D],[R],[F],[C],[T]],
        [[P],[P],[P],[P],[P],[P],[P],[P]],
        [[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ]],
        [[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ]],
        [[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ]],
        [[ ],[ ],[ ],[ ],[ ],[ ],[ ],[ ]],
        [[P],[P],[P],[P],[P],[P],[P],[P]],
        [[T],[C],[F],[D],[R],[F],[C],[T]]
        """)
    
    
    def test_evaluate(self):
        pass
    
    
    def test_play_move(self):
        pass
    
    
    def test_promote_pion(self):
        pass