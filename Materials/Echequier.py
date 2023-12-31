from Materials.Cavalier import Cavalier
from Materials.Dame import Dame
from Materials.Tour import Tour
from Materials.Fou import Fou
from Materials.Roi import Roi
from Materials.Pion import Pion
from Materials.Empty import Empty
from Coup import Coup

class Echequier:
    
    def __init__(self):
        self.board = self.setup()
        
    def setup(self):
        """
        Input : self
        Basic code : Fill the pieces at the right place
        Output : a matrix of matrix, with pieces in it, to be self.board
        """
        board_array = []
        for line in range(8):
            line_board = []
            if line == 0 or line == 7:
                line_board = [Tour("b",line+1,1),Cavalier("b",line+1,2),Fou("b",line+1,3),Dame("b",line+1,4),Roi("b",line+1,5),Fou("b",line+1,6),Cavalier("b",line+1,7),Tour("b",line+1,8)]
                board_array.append(line_board)
            elif line ==1 or line == 6:
                line_board = [Pion("b",line+1,i+1) for i in range(8)]
                board_array.append(line_board)
            else:
                line_board = [Empty(line+1,i+1) for i in range(8)]
                board_array.append(line_board)
        #Change color
        for i in range(2):
            for j in range(8):
                board_array[i][j].color = "w"
        return board_array
    
    def play_move(self,Coup):
        """
        Input : A Coup object
        Basic code : Change the content of self.board[1st coordiantes] to empty, and self.board[2nd coordinates] with the piece
        Output : the self.board actualised
        """
        self.board[Coup.li_dep-1][Coup.col_dep-1] = Empty(Coup.li_dep,Coup.col_dep)
        self.board[Coup.li_arr-1][Coup.col_arr-1] = Coup.piece
        Coup.piece.li,Coup.piece.col = Coup.li_arr,Coup.col_arr
        if Coup.piece.letter == "R" and abs(Coup.col_arr - Coup.col_dep) == 2:
            if Coup.col_arr == 3:
                self.board[Coup.li_arr-1][3],self.board[Coup.li_arr-1][0] = self.board[Coup.li_arr-1][0],Empty(Coup.li_arr,1)
                self.board[Coup.li_arr-1][3].col = 4
            else:
                self.board[Coup.li_arr-1][5],self.board[Coup.li_arr-1][7] = self.board[Coup.li_arr-1][7],Empty(Coup.li_arr,8)
                self.board[Coup.li_arr-1][5].col = 6
        
    
    
    def promote_pion(self):
        """
        Input : self
        Basic code : the method transform a Pion in last row to whatever it want except a Pion
        Output : self with updated board
        """
        pass
    
    def display(self):
        """
        Input : self
        Output : display the chess board in terminal
        """
        display_str = "["
        for i in range(7,-1,-1):
            for j in range(7):
                display_str += f"[{str(self.board[i][j])}],"
            display_str += f"[{str(self.board[i][7])}]"
            display_str += "],\n["
        display_str = display_str[0:len(display_str)-3]
        return display_str
        
    def evaluate(self):
        """
        Input : self
        Output : a float, the evaluation of the position. It will be positive for a good white's position, and negative for a good black's position.
        """
        pass


    def pointer(self,pos:list,color:str) -> bool:
        if "b" in self.is_checked:
            if self.board[pos[0]-1][pos[1]-1].letter != "R" or self.board[pos[0]-1][pos[1]-1].color != "b":
                return False
            else:
                return True
        elif "w" in self.is_checked:
            if self.board[pos[0]-1][pos[1]-1].letter != "R" or self.board[pos[0]-1][pos[1]-1].color != "w":
                return False
            else:
                return True
        else:
            return self.board[pos[0]-1][pos[1]-1].letter != " " and self.board[pos[0]-1][pos[1]-1].color == color

    def set_attack(self):

        for li in range(8):
            for col in range(8):

                if self.board[li][col].letter != " ":

                    if  self.board[li][col].generate_moves(self) != []:
                        
                        for move in self.board[li][col].generate_moves(self):

                            if self.board[li][col].color not in self.board[move[1]-1][move[2]-1].is_attacked:
                                self.board[move[1]-1][move[2]-1].is_attacked.append(self.board[li][col].color)
