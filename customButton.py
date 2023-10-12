import tkinter as tk

def popupmsg(msg, root):
    popup = tk.Frame(root, width = 200, height = 100)
    popup.place(relx = 0.5, rely = 0.5, anchor = "center")
    tk.Label(popup, text=msg).place(relx = 0.5, rely = 0.5, anchor = "center")
    tk.Button(popup, text="Okay", command = popup.place_forget).place(relx = 0.5, rely = 1, anchor = "s")

class CustomButton(tk.Button):
    def __init__(self, row, column, board, api):
        self.master = board.window
        tk.Button.__init__(self, self.master, text = " ", command = self.update, height = 5, width = 10)
        self.master.add(self)
        self.row = row
        self.column = column
        self.board = board
        self.api = api
        self.grid(row = row, column = column)
        
    def update(self, sender = "self"):
        self["text"] = self.board.player
        self["state"] = "disabled"
        self.board.PlaceObject(self.column, self.row, self["text"])
        self.board.turn += 1
        
        win = self.board.checkForWin()
        over = False
        if(win):
            popupmsg("Player " + self.board.player + " wins!", self.master)
            self.board.disableButtons()
            over = True
        elif(self.board.turn == 9):
            popupmsg("It's a tie!", self.master)
            self.board.disableButtons()
            over = True
        else:
            self.board.player = "X" if self.board.player == "O" else "O"
            
        if(self.board.isMultiPlayer):
            if(sender == "self"):
                self.api.sendMesg("MOVE " + str(self.row) + " " + str(self.column))        
                self.board.disableButtons()
            elif(not over):
                self.board.enableButtons()
        
        

    def reset(self):
        self["text"] = " "
        self["state"] = "normal"
        self.board.turn = 0