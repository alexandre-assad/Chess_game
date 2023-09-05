from Materials.Piece import Piece

class Roi(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        super().__init__(color,li,col)
        self.point = 999
        self.letter= "R"
    
    def generate_moves(self, echequier) -> list:
        piece = echequier.board[self.li-1][self.col-1]
        moves = []
        pos = [self.li-1,self.col-1]
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                if echequier.board[pos[0]+i][pos[1]+j] == " ":
                    moves.append([piece,pos[0]+i+1,pos[1]+j+1])
                elif echequier.board[pos[0]+i][pos[1]+j] != " " and echequier.board[pos[0]+i][pos[1]+j].color != piece.color and echequier.board[pos[0]+i][pos[1]+j].is_defended == False:
                     moves.append([piece,pos[0]+i+1,pos[1]+j+1])
        return moves