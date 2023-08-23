from Materials.Piece import Piece
from utils import letter_col

class Coup:
    
    
    def __init__(self,piece:Piece,li_arr:int,col_arr:int):
        self.piece = piece
        self.li_dep= self.piece.li
        self.col_dep= self.piece.col
        self.li_arr=li_arr
        self.col_arr=col_arr
        
    def __str__(self):
        return f"{self.piece.letter}{letter_col(self.col_dep)}{self.li_dep} {letter_col(self.col_arr)}{self.li_arr}"
    