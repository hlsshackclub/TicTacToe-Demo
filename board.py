import tkinter as tk

class Board:
    def __init__(self, master):
        self.grid = [[0,0,0], [0,0,0], [0,0,0]]
        self.buttons = []
        self.player = "X"
        self.turn = 0
        self.master = master
        self.window = tk.PanedWindow(self.master, orient = "vertical")
        tk.Button(self.window, text = "Restart", command = self.restart).grid(row = 3, column = 1)
        
    def show(self):
        self.window.place(relx = 0.5, rely = 0.5, anchor = "center")
        
    def hide(self):
        self.window.place_forget()
        
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
    
    def enableButtons(self):
        for i in range(len(self.grid)):
            for j in range(i):
                if self.grid[i][j] == 0:
                    self.buttons[i][j]["state"] = "normal"