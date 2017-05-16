import tkinter as tk
import random
import time
from tkinter import *

#def pisca(objeto):
#	objeto.acende()

class Game():
	
	def __init__(self):
		self.game = Tk()
		self.game.config(bg = "black") # definindo a cor do background
		self.game.title("Genius") # titulo do jogo
		self.game.geometry("1200x800")
		self.color_blue = '#%02x%02x%02x' % (0, 16, 143)
		self.color_red = '#%02x%02x%02x' % (178, 1, 1)
		self.color_yellow = '#%02x%02x%02x' % (253, 202, 0)
		self.color_green = '#%02x%02x%02x' % (0, 179, 0)
		self.color_bright_blue = '#%02x%02x%02x' % (0, 16, 255)
		self.color_bright_red = '#%02x%02x%02x' % (253, 1, 1)
		self.color_bright_yellow = '#%02x%02x%02x' % (253, 252, 0)
		self.color_bright_green = '#%02x%02x%02x' % (0, 254, 0)	
		self.canvas = tk.Canvas(self.game, height = 50, width = 50, bg = "black")
		self.green=tk.Button(self.game, height=25,width=55, bg=self.color_green, command=self.acende)
		self.red=tk.Button(self.game, height=25,width=55, bg=self.color_red)
		self.blue=tk.Button(self.game, height=25,width=55, bg=self.color_blue)
		self.yellow=tk.Button(self.game, height=25,width=55, bg=self.color_yellow)
		self.green.grid(column=1,row=1)
		self.red.grid(column=1,row=0)
		self.blue.grid(column=0,row=0)
		self.yellow.grid(column=0,row=1)
		self.aceso = False

	#def flash():
		#self.green.config(bg = color_bright_green)
		#self.game.after(1000, lambda: self.green.config(bg = self.color_green))
		#self.game.bind("KeyPress-f>", flash)

	#def run(self):
		#colors = [self.color_blue, self.color_red, self.color_yellow, self.color_green]
		#bright_colors = [self.color_bright_blue, self.color_bright_red, self.color_bright_yellow, self.color_bright_green]
		
		#while True:
			#random = random.randrange(4)
		#for random in colors:

	def acende(self):
		if self.aceso == False:
			self.green["bg"]=self.color_bright_green
			self.aceso = True
		else:
			self.green["bg"]=self.color_green
			self.aceso = False
	
	def acende(self):
		self.green["bg"]=self.color_bright_green

	def apaga(self):
		self.green["bg"]=self.color_green

	def pisca(self):
		print("acende")
		self.acende()
		for i in range(100000000):
			x = 2
		self.apaga()


	def run_game(self):
		self.game.mainloop()  

a = Game()
a.run_game()

