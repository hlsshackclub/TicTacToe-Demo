import board
import tkinter as tk
from customButton import CustomButton

root = tk.Tk()

GameBoard = board.Board()
GameBoard.addButtons([CustomButton(root, row, column, GameBoard) for row in range(3) for column in range(3)])

restartButton = tk.Button(root, text = "Restart", command = GameBoard.restart).grid(row = 3, column = 1)

root.mainloop()