class Echequier:
    
    def __init__(self):
        self.board = self.setup()
        
    def setup(self):
        """
        Input : self
        Basic code : Fill the pieces at the right place
        Output : a matrix of matrix, with pieces in it, to be self.board
        """
        pass
    
    
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
        pass
        
    def evaluate(self):
        """
        Input : self
        Output : a float, the evaluation of the position. It will be positive for a good white's position, and negative for a good black's position.
        """
        pass