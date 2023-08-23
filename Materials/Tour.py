from Materials.Piece import Piece

class Tour(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        self.color = color
        self.li = li
        self.col = col
        self.point = 5
        self.letter = "T"
        
    def possible_move(self) -> list:
        pass