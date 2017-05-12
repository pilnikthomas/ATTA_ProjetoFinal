# -*- coding: utf-8 -*-
"""
Created on Sat May  6 17:23:45 2017

@author: Thomas Pilnik
"""

import pygame
import tkinter as tk
from pygame.locals import *
import sys


		
		

def tela_inicial():
	pygame.init()
	tela = pygame.display.set_mode((234,234))
	pygame.display.set_caption("Jogo Genius")
	fundo = pygame.image.load("imagens/genius.png").convert()
	#botao = pygame.Button(tela)
	#botao.configure(text="Iniciar")
	#botao.grid()
	
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			tela.blit(fundo,(0,0))
			#botao.blit(fundo,(234/2,234/2))
		pygame.display.update()
		
print(tela_inicial())
