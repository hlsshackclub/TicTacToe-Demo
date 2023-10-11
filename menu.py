import tkinter as tk

def entrypopup(msg, root):
    def submit():
        popup.place_forget()
        print(answer.get())
        wait.set(1)
    popup = tk.Frame(root, width = 200, height = 100)
    popup.place(relx = 0.5, rely = 0.5, anchor = "center")
    tk.Label(popup, text=msg).place(relx = 0.5, rely = 0.25, anchor = "center")
    answer = tk.StringVar()
    tk.Entry(popup, textvariable = answer).place(relx = 0.5, rely = 0.5, anchor = "center")
    button = tk.Button(popup, text="Okay", command = submit)
    button.place(relx = 0.5, rely = 1, anchor = "s")
    wait = tk.IntVar()
    button.wait_variable(wait)
    return answer.get()

#main menu for tictactoe with a single player and multiplayer option
class MainMenu:
    def __init__(self, board, master, client_socket):
        #create the window
        self.board = board
        self.master = master
        self.window = tk.PanedWindow(self.master, orient = "vertical")
        self.client_socket = client_socket
        
        #add the buttons
        tk.Button(self.window, text = "Single Player", command = self.singlePlayer).grid(row = 0, column = 0)
        tk.Button(self.window, text = "Multiplayer", command = self.multiplayer).grid(row = 1, column = 0)
    
    def show(self):
        self.window.place(relx = 0.5, rely = 0.5, anchor = "center")
        
    def hide(self):
        self.window.place_forget()
        
    def singlePlayer(self):
        self.hide()
        self.board.singlePlayer()
        
    def multiplayer(self):
        self.hide()
        #create a new window to ask if the player wants to create or join a game
        menu = tk.PanedWindow(self.master, orient = "vertical")
        tk.Button(menu, text = "Create Game", command = lambda: self.createGame(menu)).grid(row = 0, column = 0)
        tk.Button(menu, text = "Join Game", command = lambda: self.joinGame(menu)).grid(row = 1, column = 0)
        menu.place(relx = 0.5, rely = 0.5, anchor = "center")
        
    def createGame(self, menu):
        menu.place_forget()
        self.client_socket.send("CREATE".encode())
        answer = self.client_socket.recv(1024).decode()
        print(answer)
        self.board.multiPlayer(0)
        
    def joinGame(self, menu):
        gameID = entrypopup("Enter the game ID", self.master)
        self.client_socket.send(("JOIN " + gameID).encode())
        menu.place_forget()
        self.board.multiPlayer(1)