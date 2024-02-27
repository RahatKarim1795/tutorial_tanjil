class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        print("   0   1   2")

        # for i in range(self.size):
        #     j = 0
        #     print(f"{i}  {self.board[i][j]} | {self.board[i][j+1]} | {self.board[i][j+2]}")
        #     # board = [[1,2,3],[0,0,0],[2,3,2]]
        #     if i != (self.size - 1):
        #         print("  -----------")

        for i in range(self.size):
            print(f"{i} ", end="")

            for j in range(self.size):
                print(f' {self.board[i][j]} ', end="")
                if j != (self.size-1):
                    print(f'|', end="")

            if i != (self.size - 1):
                print("\n  -----------")
        print()
        print()

    
    def squareIsEmpty(self, row, col):
        if self.board[row][col] == 0:
            return True
        else:
            return False
    
    def update(self, row, col, num):
        if self.squareIsEmpty(row,col):
            self.board[row][col] = num
            return True
        else:
            return False
            
    def boardFull(self):

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return False
                
        # loop over; all elements checked        
        return True
        
    def checkRows(self):
        for i in range(self.size):
            j = 0
            if self.board[i][j] + self.board[i][j+1] + self.board[i][j+2] == 15:
                return True
        return False
    
    def checkColumns(self):
        for i in range(self.size):
            j=0
            if self.board[j][i] + self.board[j+1][i] + self.board[j+2][i] == 15:
                return True
        return False

    def checkDiag(self):
        i=0
        j=0
        if self.board[i][j] + self.board[i+1][j+1] + self.board[i+2][j+2] == 15:
            return True
        elif self.board[i+2][j] + self.board[i+1][j+1] + self.board[i][j+2] == 15:
            return True
        else:
            return False
        
    def isWinner(self):
        if self.checkRows() or self.checkColumns() or self.checkDiag():
            return True
        else:
            return False
        
    def isWinner2(self):
        # Check rows and columns in the same loop
        for i in range(self.size):
            if sum(self.board[i]) == 15:  # Check row
                return True
            
        for i in range(self.size): # Check column
            sum = 0
            for j in range(self.size):  
                sum += self.board[j][i]

            if sum == 15:
                return True

        # Check diagonals
        if sum(self.board[i][i] for i in range(self.size)) == 15 or sum(self.board[i][self.size - 1 - i] for i in range(self.size)) == 15:
            return True

        return False
        
print("Tic Tac Toe")
a = NumTicTacToe()

a.drawBoard()
a.update(0,0,5)
a.update(1,1,7)
a.update(2,2,3)
a.drawBoard()

if a.isWinner():
    print("sdasdasd")

    

