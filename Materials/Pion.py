from Piece import Piece


class Pion(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        self.color = color
        self.li = li
        self.col = col
        self.point = 1
        self.letter=""