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
	botao1 = pygame.image.load("botao.jpg").convert()
	botao2 = pygame.image.load("botao2.jpg").convert()
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			tela.blit(fundo,(0,0))
			tela.blit(botao1,(250,242))
			tela.blit(botao2,(500,534))
			
		pos_mouse= pygame.mouse.get_pos()
		x= pos_mouse[0]
		y= pos_mouse[1]
		
		if x>0 and x<300 and y>0 and y<292:
			print("azul")
			
		print(pos_mouse)
		
		if x>250 and x<350 and y>242 and y<342:
			print("botao")
		botoes_mouse1= pygame.mouse.get_pressed()
		if botoes_mouse1[0]:
			print("iniciar")
		
		if x>500 and x<600 and y>534 and y<584:
			print("ranking")
		botoes_mouse2= pygame.mouse.get_pressed()
		if botoes_mouse2[0]:
			print("ranking")
			
		
		
		pygame.display.update()
		
print(tela_inicial())
