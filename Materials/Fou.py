from Materials.Piece import Piece

class Fou(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        super().__init__(color,li,col)
        self.point = 3
        self.letter = "F"