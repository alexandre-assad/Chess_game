from Materials.Piece import Piece

class Tour(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        super().__init__(color,li,col)
        self.point = 5
        self.letter = "T"
        
    def possible_move(self) -> list:
        pass