import tkinter as tk

def popupmsg(msg, root):
    popup = tk.Frame(root, width = 200, height = 100)
    popup.place(relx = 0.5, rely = 0.5, anchor = "center")
    tk.Label(popup, text=msg).place(relx = 0.5, rely = 0.5, anchor = "center")
    tk.Button(popup, text="Okay", command = popup.place_forget).place(relx = 0.5, rely = 1, anchor = "s")

class CustomButton(tk.Button):
    def __init__(self, master, row, column, board):
        tk.Button.__init__(self, master, text = " ", command = self.update, height = 5, width = 10)
        self.master = master
        self.row = row
        self.column = column
        self.board = board
        self.grid(row = row, column = column)
        
    def update(self):
        self["text"] = self.board.player
        self["state"] = "disabled"
        self.board.PlaceObject(self.column, self.row, self["text"])
        self.board.turn += 1
        
        win = self.board.checkForWin()
        if(win):
            popupmsg("Player " + self.board.player + " wins!", self.master)
            self.board.disableButtons()
        elif(self.board.turn == 9):
            popupmsg("It's a tie!", self.master)
            self.board.disableButtons()
        else:
            self.board.player = "X" if self.board.player == "O" else "O"
        
    def reset(self):
        self["text"] = " "
        self["state"] = "normal"