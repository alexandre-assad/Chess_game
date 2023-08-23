from Materials.Piece import Piece

class Cavalier(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        self.color = color
        self.li = li
        self.col = col
        self.point = 3
        self.letter = "C"