import unittest
from coup import *
from Materials.Cavalier import Cavalier
class TestCoup(unittest.TestCase):
    
    def test_coup_str(self):
        self.assertEqual(print(Coup(Cavalier("b",4,7),3,6)),"CH4 F3")
