from Materials.Cavalier import Cavalier
from Materials.Dame import Dame
from Materials.Tour import Tour
from Materials.Fou import Fou
from Materials.Roi import Roi
from Materials.Pion import Pion

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
                line_board = [" " for i in range(8)]
                board_array.append(line_board)
        #Change color
        for i in range(2):
            for j in range(8):
                board_array[i][j].color = "w"
        return board_array
    
    def play_move(self,li_dep,col_dep,li_arr,col_arr):
        """
        Input : coordinates of piece and coordinates of arrivals
        Basic code : Change the content of self.board[1st coordiantes] to empty, and self.board[2nd coordinates] with the piece
        Output : the self.board actualised
        """
        pass
    
    
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
        display_str = ""
        for i in range(len(self.board)):
            display_str += str(self.board[i])
            display_str += "\n"
        return display_str
        
    def evaluate(self):
        """
        Input : self
        Output : a float, the evaluation of the position. It will be positive for a good white's position, and negative for a good black's position.
        """
        pass