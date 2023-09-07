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
        for rock in self.rock_possible(echequier):
            moves.append(rock)
        return moves
    
    def rock_possible(self,echequier) -> bool :
        rock_moves = []
        #Small rock
        if echequier.board[0][5].letter == " " and echequier.board[0][5].is_attacked == False and echequier.board[0][6].letter == " " and echequier.board[0][6].is_attacked == False and self.has_moved == False and echequier.board[0][7].has_moved == False:
            rock_moves.append([self,self.li,self.col+2])
        if echequier.board[0][3].letter == " " and echequier.board[0][3].is_attacked == False and echequier.board[0][2].letter == " " and echequier.board[0][2].is_attacked == False and echequier.board[0][1].letter == " " and self.has_moved == False and echequier.board[0][0].has_moved== False:
            rock_moves.append([self,self.li,self.col-2])
        return rock_moves