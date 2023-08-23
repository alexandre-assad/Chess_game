from Materials.Piece import Piece

class Dame(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        self.color = color
        self.li = li
        self.col = col
        self.point = 9
        self.letter ="D"