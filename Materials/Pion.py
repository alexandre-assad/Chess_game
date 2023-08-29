from Piece import Piece


class Pion(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        super().__init__(color,li,col)
        self.point = 1
        self.letter=""
        
    