import tkinter as tk
import random
import time
from tkinter import *


game = tk.Tk()
mycolor = '#%02x%02x%02x' % (0, 16, 143)
game.config(bg = mycolor)
game.title("Genius")
game.geometry("1000x850")
canvas = tk.Canvas(game, height = 50, width = 50, bg = "black")
green=tk.Button(game,height=25,width=55, bg="green")
red=tk.Button(game,height=25,width=55, bg="red")
blue=tk.Button(game,height=25,width=55, bg="blue")
yellow=tk.Button(game,height=25,width=55, bg="yellow")
green.grid(column=1,row=1)
red.grid(column=1,row=0)
blue.grid(column=0,row=0)
yellow.grid(column=0,row=1)
game.mainloop()     