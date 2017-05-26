import pygame
from pygame.locals import *
import sys
import random 


	
	
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
			tela.blit(botao2,(500,514))
			
		pos_mouse= pygame.mouse.get_pos()
		x= pos_mouse[0]
		y= pos_mouse[1]
		
		if x>0 and x<300 and y>0 and y<293:
			print("azul")
			
		if x>301 and x<600 and y>0 and y<292:
			print("vermelho")
			
		if x>0 and x<300 and y>293 and y<586:
			print("amarelo")
			
		if x>301 and x<600 and y>294 and y<586:
			print("verde")
		
			
		print(pos_mouse)
		botoes_mouse= pygame.mouse.get_pressed()
		if x>250 and x<350 and y>242 and y<342:
			print("botao")
			if botoes_mouse[0]:
				def tela_jogo():
					pygame.init()
					tela = pygame.display.set_mode((600,586))
					pygame.display.set_caption("Genius Game")
					botao1 = pygame.image.load("botao_azul.jpg").convert()
					botao2 = pygame.image.load("botao_vermelho.jpg").convert()
					botao3 = pygame.image.load("botao_amarelo.jpg").convert()
					botao4 = pygame.image.load("botao_verde.jpg").convert()
					botao5 = pygame.image.load("botao_azul_claro.jpg").convert()
					botao6 = pygame.image.load("botao_vermelho_claro.jpg").convert()
					botao7 = pygame.image.load("botao_amarelo_claro.jpg").convert()
					botao8 = pygame.image.load("botao_verde_claro.jpg").convert()
					
					while True:
						for evento in pygame.event.get():
							if evento.type == QUIT:
								pygame.quit()
								sys.exit()
							tela.blit(botao1,(0,0))
							tela.blit(botao2,(300,0))
							tela.blit(botao3,(0,300))
							tela.blit(botao4,(300,300))
						
						pos_mouse= pygame.mouse.get_pos()
						x= pos_mouse[0]
						y= pos_mouse[1]
						
						botoes_mouse= pygame.mouse.get_pressed()
						if x>0 and x<300 and y>0 and y<293:
							#print("azul")
							if botoes_mouse[0]:
								tela.blit(botao5,(0,0))
								print("azul")
						if x>301 and x<600 and y>0 and y<293:
							#print("vermelho")
							if botoes_mouse[0]:
								tela.blit(botao6,(300,0))
								print("vermelho")
						if x>0 and x<300 and y>294 and y<586:
							#print("amarelo")
							if botoes_mouse[0]:
								tela.blit(botao7,(0,300))
								print("amarelo")
						if x>301 and x<600 and y>294 and y<586:
							#print("verde")	
							if botoes_mouse[0]:
								tela.blit(botao8,(300,300))
								print("verde")
						sequencia = {"verde", "vermelho", "azul"}
						for botao in sequencia:
						
							if botao=="verde":
								tela.blit(botao8,(300,300))
							if botao=="vermelho":
								tela.blit(botao6,(300,0))
							if botao=="azul":
								tela.blit(botao5,(0,0))
							if botao=="amarelo":
								tela.blit(botao7,(0,300))
								
							
						
						pygame.display.update()
						
				print(tela_jogo())
				
		if x>500 and x<600 and y>516 and y<586:
			print("ranking")
			if botoes_mouse[0]:
				def tela_ranking():
					pygame.init()
					tela = pygame.display.set_mode((600,586))
					pygame.display.set_caption("Genius Game")
					
					while True:
						for evento in pygame.event.get():
							if evento.type == QUIT:
								pygame.quit()
								sys.exit()
								
						pygame.display.update()
						
				print(tela_ranking())
		
		pygame.display.update()
		
print(tela_inicial())			