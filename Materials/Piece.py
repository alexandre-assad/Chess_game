class Piece:
    
    def __init__(self,color:str,li:int,col:int):
        self.color = color
        self.li = li
        self.col = col
        self.point = 0
    
    
    def possible_move(self) -> list[Coup]:
        """
        Input : self
        Output : list de coups (list de [Objet pièce, position de départ, postion d'arrivée])
        """
        pass 
