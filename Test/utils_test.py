import unittest

from utils import *

class TestUtils(unittest.TestCase):
    
    def test_letter_col(self):
        self.assertEqual(letter_col(1),"A")
        self.assertEqual(letter_col(3),"C")
        self.assertEqual(letter_col(8),"H")

