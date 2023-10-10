import tkinter as tk

#main menu for tictactoe with a single player and multiplayer option
class MainMenu:
    def __init__(self, board, master):
        #create the window
        self.board = board
        self.master = master
        self.window = tk.PanedWindow(self.master, orient = "vertical")
        
        #add the buttons
        tk.Button(self.window, text = "Single Player", command = self.singlePlayer).grid(row = 0, column = 0)
        tk.Button(self.window, text = "Multiplayer", command = self.multiplayer).grid(row = 1, column = 0)
    
    def show(self):
        self.window.place(relx = 0.5, rely = 0.5, anchor = "center")
        
    def hide(self):
        self.window.place_forget()
        
    def singlePlayer(self):
        self.hide()
        self.board.singlePlayer.show()
        
    def multiplayer(self):
        self.hide()
        self.board.multiPlayer.show()
        