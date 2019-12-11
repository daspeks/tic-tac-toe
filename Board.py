# Constants for piece types

EMPTY = 0
X = 1
O = 2

class Board:
    ### PART 01 / CONSTRUCTOR:
    def __init__(self, rows=3, cols=3):
        self.board = [[EMPTY for i in range(cols)] for j in range(rows)]
    
    ### PART O1 / METHOD:
    def rows(self):
        return len(self.board)
    
    ### PART 01 / METHOD:
    def cols(self):
        return len(self.board[0])
    
    ### PART 02 / METHOD:
    def canPlay(self, r, c):
        return (self.board[r][c] == EMPTY)
    
    ### PART 02 / METHOD:
    def play(self, r, c, piece):
        self.board[r][c] = piece
    
    ### PART 03 / METHOD:
    def full(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == EMPTY:
                    return False
        return True
    
    ### PART 04 / METHOD:
    def winInRow(self, r, piece):
        rowl = self.board[r]
        for i in range(len(rowl)):
            if (i + 3 <= len(rowl)) and (rowl[i] == rowl[i + 1] == rowl[i + 2] == piece):
                return True
        return False

    ### PART 04 / METHOD:
    def winInCol(self, c, piece):
        coll = list(zip(*self.board))[c] # to understand this line look at part 06 comments
        for i in range(len(coll)):
            if (i + 3 <= len(coll)) and (coll[i] == coll[i + 1] == coll[i + 2] == piece):
                return True
        return False

    ### PART 05 / METHOD:
    def winInDiag(self, piece):
        ### Find all the diagonals of the board
        # Find rows and cols
        rows = len(self.board)
        cols = len(self.board[0])
        
        ########################################################
        ########################################################
        # Following code is slightly modified from
        # https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
        # It is upto you to include this citation or not
        ########################################################
        ########################################################
        # Create empty lists to contain all diagonal lists
        fdiag = [[] for x in range(rows + cols - 1)]
        bdiag = [[] for x in range(len(fdiag))]
        #
        min_bdiag = 1 - rows
        #
        for x in range(rows):
            for y in range(cols):
                fdiag[x + y].append(self.board[x][y])
                bdiag[y - x - min_bdiag].append(self.board[x][y])
        ########################################################
        ########################################################
        ########################################################
        ########################################################
        ########################################################

        # Delete elements of sizes less than 3 from forward diagonal
        for item in fdiag:
            if len(item) < 3:
                fdiag.remove(item)
        # Delete elements of sizes less than 3 from backward diagonal
        for item in bdiag:
            if len(item) < 3:
                bdiag.remove(item)
        # Find 3 serial 'pieces' in forward diagonals
        for item in fdiag:
            for i in range(0, len(item), 1):
                if (i + 3 <= len(item)) and (item[i] == item[i + 1] == item[i + 2] == piece):
                    return True
        # Find 3 serial 'pieces' in backward diagonals
        for item in bdiag:
            for i in range(0, len(item), 1):
                if (i + 3 <= len(item)) and (item[i] == item[i + 1] == item[i + 2] == piece):
                    return True
        #
        return False

    ### PART 06 / METHOD:
    def won(self, piece):
        for r,row in enumerate(self.board): # Applying enumerate() on a list returns index, value of the elements in the list
            if self.winInRow(r, piece):
                return True
    
    
        # *list_name unpacks a list i.e if a = [[1, 2], [3,4]] then print (*a) = [1, 2], [3, 4] (note that outer brackets are not printed)
        # zip() on a 2-D list if place the list one below the other and 'zip' them i.e zip(*a) is (1, 3), (2,4).
        # print (zip(*a)) won't show anything so I list() it to get [(1, 3), (2,4)]
        for c,col in enumerate(list(zip(*self.board))):
            if self.winInCol(c, piece):
                return True
        
        if self.winInDiag(piece):
            return True
        else:
            return False

    ### PART 07 / METHOD:
    def hint(self, piece):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.canPlay(r, c):
                    self.play(r, c, piece)
                    if self.won(piece):
                        self.board[r][c] = EMPTY
                        return r, c
                    else:
                        self.board[r][c] = EMPTY
        return -1, -1
    
    ### METHOD:
    def gameover(self):
        if self.won(X) or self.won(O) or self.full():
            return True
        return False
