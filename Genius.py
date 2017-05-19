# -*- coding: utf-8 -*-
"""
Created on Sat May  6 17:23:45 2017

@author: Alfredo Acerbi, Ariel Iglicky, Tiago Mingossi, Thomas Pilnik
"""

import pygame
from pygame.locals import *
import sys
import random 


class Button:
	def __init__(self, color, bright_color, pos_x, pos_y):
		self.x = pos_x
		self.y = pos_y
		self.image = pygame.image.load(color).convert_alpha()
		self.image = pygame.transform.scale(self.image, (300, 300))
		self.image_bright = pygame.image.load(bright_color).convert_alpha()
		self.image_bright = pygame.transform.scale(self.image, (300, 300))
		self.bright = False

	def show(self, window):
		if self.bright:
			window.blit(self.image_bright, (self.x, self.y))
		else:
			window.blit(self.image, (self.x, self.y))
		pygame.display.update()

	def blink(self, window):
		self.bright = True
		self.show(window)
		pygame.time.wait(800)
		self.bright = False
		self.show(window)