from Materials.Piece import Piece

class Tour(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        super().__init__(color,li,col)
        self.point = 5
        self.letter = "T"
        
    def generate_moves(self,echequier) -> list:
        """
        Input : self
        Output : list de coups (list de [Objet pièce, postion d'arrivée])
        """
        piece = echequier.board[self.li-1][self.col-1]
        moves = []
        run = True
        pos = [self.li-1,self.col-1]
        while run:
            if pos[0] != 7:
                if echequier.board[pos[0]+1][pos[1]] == " ":
                    moves.append([self,pos[0]+1+1,pos[1]+1])
                    pos = [pos[0]+1,pos[1]]
                elif echequier.board[pos[0]+1][pos[1]] != " " and echequier.board[pos[0]+1][pos[1]].color != piece.color:
                    moves.append([piece,pos[0]+1+1,pos[1]+1])
                    run = False
                else:
                    run = False
            else:
                run = False
        run = True
        pos = [self.li-1,self.col-1]
        while run:
            if pos[0] != 0:
                if echequier.board[pos[0]-1][pos[1]] == " ":
                    moves.append([self,pos[0]-1+1,pos[1]+1])
                    pos = [pos[0]-1,pos[1]]
                elif echequier.board[pos[0]-1][pos[1]] != " " and echequier.board[pos[0]-1][pos[1]].color != piece.color:
                    moves.append([piece,pos[0]-1+1,pos[1]+1])
                    run = False
                else:
                    run = False
            else:
                run = False
        run = True
        pos = [self.li-1,self.col-1]
        while run:
            if pos[1] != 0:
                if echequier.board[pos[0]][pos[1]-1] == " ":
                    moves.append([self,pos[0]+1,pos[1]-1+1])
                    pos = [pos[0],pos[1]-1]
                elif echequier.board[pos[0]][pos[1]-1] != " " and echequier.board[pos[0]][pos[1]-1].color != piece.color:
                    moves.append([piece,pos[0]+1,pos[1]-1+1])
                    run = False
                else:
                    run = False
            else:
                run = False
        run = True
        pos = [self.li-1,self.col-1]
        while run:
            if pos[1] != 7:
                if echequier.board[pos[0]][pos[1]+1] == " ":
                    moves.append([self,pos[0]+1,pos[1]+1+1])
                    pos = [pos[0],pos[1]+1]
                elif echequier.board[pos[0]][pos[1]+1] != " " and echequier.board[pos[0]][pos[1]+1].color != piece.color:
                    moves.append([piece,pos[0]+1,pos[1]+1+1])
                    run = False
                else:
                    run = False
            else:
                run = False
        return moves