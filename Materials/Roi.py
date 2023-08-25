from Materials.Piece import Piece

class Roi(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        super().__init__(color,li,col)
        self.point = 999
        self.letter= "R"