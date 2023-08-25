from Materials.Piece import Piece

class Dame(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        super().__init__(color,li,col)
        self.point = 9
        self.letter ="D"