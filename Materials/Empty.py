class Empty:

    def __init__(self,li:int,col:int):
        self.li = li
        self.col = col
        self.letter = " "
        self.color =""
        self.is_attacked = False
        self.is_defended = False

    def __repr__(self):
        return self.letter