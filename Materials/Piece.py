class Piece:
    
    def __init__(self,color:str,li:int,col:int):
        self.color = color
        self.li = li
        self.col = col
        self.point = 0
        self.letter =""
    
    
    def generate_moves(self) -> list:
        """
        Input : self
        Output : list de coups (list de [Objet pièce, position de départ, postion d'arrivée])
        """
        pass 

    def __repr__(self):
        return self.letter
    