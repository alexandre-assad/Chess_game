from Materials.Piece import Piece


class Pion(Piece):
    
    def __init__(self,color:str,li:int,col:int):
        super().__init__(color,li,col)
        self.point = 1
        self.letter="P"
        self.en_passant = [] #Must be an array like [3,2] to go .board[2][1]
    
    def generate_moves(self, echequier) -> list:
        piece = echequier.board[self.li-1][self.col-1]
        moves = []
        pos = [self.li-1,self.col-1]
        if piece.color == "w":
            distance = 1
            if pos[0] == 1:
                for i in range(2):
                    if echequier.board[pos[0]+distance][pos[1]].letter == " ":
                        moves.append([self,pos[0]+distance+1,pos[1]+1])
                        pos = [pos[0]+distance,pos[1]]
                pos = [self.li-1,self.col-1]
            else:
                if echequier.board[pos[0]+distance][pos[1]].letter == " ":
                        moves.append([self,pos[0]+distance+1,pos[1]+1])
            if pos[1]+1 <= 7:
                if echequier.board[pos[0]+distance][pos[1]+1].letter != " " and echequier.board[pos[0]+distance][pos[1]+1].color != piece.color:
                    moves.append([self,pos[0]+distance+1,pos[1]+1+1])
            if pos[1]-1 >= 0:
                if echequier.board[pos[0]+distance][pos[1]-1].letter != " " and echequier.board[pos[0]+distance][pos[1]-1].color != piece.color:
                    moves.append([self,pos[0]+distance+1,pos[1]-1+1])
                
        else:
            distance = -1
            if pos[0] == 6:
                for i in range(2):
                    if echequier.board[pos[0]+distance][pos[1]].letter == " ":
                        moves.append([self,pos[0]+distance+1,pos[1]+1])
                        pos = [pos[0]+distance,pos[1]]
                pos = [self.li-1,self.col-1]
            else:
                if echequier.board[pos[0]+distance][pos[1]].letter == " ":
                        moves.append([self,pos[0]+distance+1,pos[1]+1])
                        pos = [pos[0]+distance,pos[1]]
            if pos[1]+1 <= 7: 
                if echequier.board[pos[0]+distance][pos[1]+1].letter != " " and echequier.board[pos[0]+distance][pos[1]+1].color != piece.color:
                    moves.append([self,pos[0]+distance+1,pos[1]+1+1])
            if pos[1]-1 >= 0:
                if echequier.board[pos[0]+distance][pos[1]-1].letter != " " and echequier.board[pos[0]+distance][pos[1]-1].color != piece.color:
                    moves.append([self,pos[0]+distance+1,pos[1]-1+1])
        if self.en_passant != []:
            moves.append([self,self.en_passant[0],self.en_passant[1]])
        self.en_passant = []
        return moves