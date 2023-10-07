class Board:
    def __init__(self):
        self.grid = [[0,0,0], [0,0,0], [0,0,0]]
        self.buttons = []
        self.player = "X"
        self.turn = 0
        
    def PlaceObject(self, column, row, player):
        self.grid[row][column] = player
        
    def addButtons(self, buttons):
        self.buttons = buttons
        
    def checkForWin(self):        
        def checkForVerticalWin(self):
            for i in range(3):
                if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] == self.player:
                    return True
            return False
        
        def checkForHorizontalWin(self):
            for i in range(3):
                if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] == self.player:
                    return True
            return False
        
        def checkForDiagonalWin(self):
            return self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == self.player or self.grid[2][0] == self.grid[1][1] == self.grid[0][2] == self.player
        
        return checkForVerticalWin(self) or checkForHorizontalWin(self) or checkForDiagonalWin(self)

    def restart(self):
        self.grid = [[0,0,0], [0,0,0], [0,0,0]]
        self.player = "X"
        for button in self.buttons:
            button.reset()
            
    def disableButtons(self):
        for button in self.buttons:
            button["state"] = "disabled"