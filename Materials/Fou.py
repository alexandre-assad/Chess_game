from Materials.Piece import Piece

class Fou(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        super().__init__(color,li,col)
        self.point = 3
        self.letter = "F"


    def generate_moves(self) -> list:
        """
        Input : self
        Output : list de coups (list de [Objet pièce, postion d'arrivée])
        """
        pass