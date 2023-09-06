from Materials.Piece import Piece

class Cavalier(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        super().__init__(color,li,col)
        self.point = 3
        self.letter = "C"


    def generate_moves(self, echequier) -> list:
        piece = echequier.board[self.li-1][self.col-1]
        moves = []
        pos = [self.li-1,self.col-1]
        possible_distance = [-2,-1,1,2]
        for i in possible_distance:
            if abs(i) == 2:
                if pos[0] +i <= 7 and pos[0] + i >= 0 and pos[1]+1 <= 7:
                    if echequier.board[pos[0]+i][pos[1]+1] == " " or  echequier.board[pos[0]+i][pos[1]+1].color != piece.color:
                        moves.append([self,pos[0]+i+1,pos[1]+1+1])
                if pos[0] +i <= 7 and pos[0] + i >= 0 and pos[1]-1 >= 0:
                    if echequier.board[pos[0]+i][pos[1]-1] == " " or  echequier.board[pos[0]+i][pos[1]-1].color != piece.color:
                    
                        moves.append([self,pos[0]+i+1,pos[1]-1+1])
            else:
                if pos[0] +i <= 7 and pos[0] + i >= 0 and pos[1]+2 <= 7:
                    if echequier.board[pos[0]+i][pos[1]+2] == " " or  echequier.board[pos[0]+i][pos[1]+2].color != piece.color:
                    
                        moves.append([self,pos[0]+i+1,pos[1]+2+1])
                if pos[0] +i <= 7 and pos[0] + i >= 0 and pos[1]-2 >= 0:
                    if echequier.board[pos[0]+i][pos[1]-2] == " " or  echequier.board[pos[0]+i][pos[1]-2].color != piece.color:
                    
                        moves.append([self,pos[0]+i+1,pos[1]-2+1])
        return moves