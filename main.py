import board
import tkinter as tk
from customButton import CustomButton
from menu import MainMenu
import socket

root = tk.Tk()
root.geometry("350x350")

# Connect to the server
server_host = "127.0.0.1"  # Replace with the actual server IP
server_port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

GameBoard = board.Board(root, client_socket)
GameBoard.addButtons([CustomButton(row, col, GameBoard, client_socket) for col in range(3) for row in range(3)])

mainMenu = MainMenu(GameBoard, root, client_socket)
mainMenu.show()

root.mainloop()