from Materials.Piece import Piece
from Materials.Tour import Tour
from Materials.Fou import Fou

class Dame(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        super().__init__(color,li,col)
        self.point = 9
        self.letter ="D"

    def generate_moves(self, echequier) -> list:
        moves = Tour(self.color,self.li,self.col).generate_moves(echequier) + Fou(self.color,self.li,self.col).generate_moves(echequier)
        for i in range(len(moves)):
            moves[i][0] = self
        
        return moves