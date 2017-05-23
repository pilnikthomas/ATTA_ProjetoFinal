"""
Created on Sat May  6 17:23:45 2017

@author: Thomas Pilnik
"""

import pygame
from pygame.locals import *
import sys


		
		

def tela_inicial():
	pygame.init()
	tela = pygame.display.set_mode((600,584))
	pygame.display.set_caption("Genius Game")
	fundo = pygame.image.load("genius.jpg").convert()
	font_name = pygame.font.get_default_font()
	game_font = pygame.font.SysFont(font_name, 72)
	text = game_font.render('Aperte espaco para iniciar', 1, (255, 0, 0))
	tela.blit(text, (300, 292))
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			tela.blit(fundo,(0,0))
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[K_BACKSPACE]:
			print(ola)
		pygame.display.update()
		
print(tela_inicial())
