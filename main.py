import tkinter as tk

import board
from customButton import CustomButton
from menu import MainMenu
from api import API
from gameManager import GameManager

root = tk.Tk()
root.geometry("350x350")

serverAPI = API()

GameBoard = board.Board(root)
GameBoard.addButtons([CustomButton(row, col, GameBoard, serverAPI) for col in range(3) for row in range(3)])

manager = GameManager(GameBoard, serverAPI)

mainMenu = MainMenu(GameBoard, root, serverAPI, manager)
mainMenu.show()

root.mainloop()