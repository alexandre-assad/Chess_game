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
        self.board[Coup.li_dep-1][Coup.col_dep-1] = self.board[Coup.li_arr-1][Coup.col_arr-1]
        self.board[Coup.li_dep-1][Coup.col_dep-1].li, self.board[Coup.li_dep-1][Coup.col_dep-1].col = Coup.li_dep,Coup.col_dep
        self.board[Coup.li_arr-1][Coup.col_arr-1] = Coup.piece
        Coup.piece.li,Coup.piece.col = Coup.li_arr,Coup.col_arr
        
    
    
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
        return self.board[pos[0]-1][pos[1]-1].letter != " " and self.board[pos[0]-1][pos[1]-1].color == color