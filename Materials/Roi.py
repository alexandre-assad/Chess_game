from Materials.Piece import Piece

class Roi(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        super().__init__(color,li,col)
        self.point = 999
        self.letter= "R"
        self.has_moved = False
    
    def generate_moves(self, echequier) -> list:
        piece = echequier.board[self.li-1][self.col-1]
        moves = []
        pos = [self.li-1,self.col-1]
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                if pos[0]+i <= 7 and pos[0]+i >= 0 and pos[1]+j <= 7 and pos[1]+j >= 0:
                    if echequier.board[pos[0]+i][pos[1]+j].letter == " ":
                        moves.append([piece,pos[0]+i+1,pos[1]+j+1])
                    elif echequier.board[pos[0]+i][pos[1]+j].letter != " " and echequier.board[pos[0]+i][pos[1]+j].color != piece.color and echequier.board[pos[0]+i][pos[1]+j].is_defended == False:
                        moves.append([piece,pos[0]+i+1,pos[1]+j+1])
        moves.append(self.rock_possible(echequier))
        return moves
    
    def rock_possible(self,echequier) -> bool :
        pass