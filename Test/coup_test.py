import unittest
from Coup import Coup
from Materials.Cavalier import Cavalier
from Materials.Dame import Dame

class TestCoup(unittest.TestCase):
    
    def test_coup_str(self):
        C = Coup(Cavalier("b",4,8),3,6)
        self.assertEqual(f"{C}",'CH4 F3')

