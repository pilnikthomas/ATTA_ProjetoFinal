import pygame
from pygame.locals import *
import sys
import random 
import time
import urllib.request
	
def tela_inicial():
	pygame.init()
	tela = pygame.display.set_mode((600,600))
	pygame.display.set_caption("Genius Game")
	botao1 = pygame.image.load("botao_azul.jpg").convert()
	botao1 = pygame.transform.scale(botao1, (300, 300))
	botao2 = pygame.image.load("botao_vermelho.jpg").convert()
	botao2 = pygame.transform.scale(botao2, (300, 300))
	botao3 = pygame.image.load("botao_verde.jpg").convert()
	botao3 = pygame.transform.scale(botao3, (300, 300))
	botao4 = pygame.image.load("botao_amarelo.jpg").convert()
	botao4 = pygame.transform.scale(botao4, (300, 300))
	botao5 = pygame.image.load("botao_azul_claro.jpg").convert()
	botao5 = pygame.transform.scale(botao5, (300, 300))
	botao6 = pygame.image.load("botao_vermelho_claro.jpg").convert()
	botao6 = pygame.transform.scale(botao6, (300, 300))
	botao7 = pygame.image.load("botao_verde_claro.jpg").convert()
	botao7 = pygame.transform.scale(botao7, (300, 300))
	botao8 = pygame.image.load("botao_amarelo_claro.jpg").convert()
	botao8 = pygame.transform.scale(botao8, (300, 300))
	botaoON = pygame.image.load("botao.png").convert_alpha()
	botaoON = pygame.transform.scale(botaoON, (50, 50))
	tela.blit(botao1,(0,0))
	tela.blit(botao2,(300,0))
	tela.blit(botao3,(0,300))
	tela.blit(botao4,(300,300))
	tela.blit(botaoON,(275,275))
	
	
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			
			
		pos_mouse= pygame.mouse.get_pos()
		x= pos_mouse[0]
		y= pos_mouse[1]
		
		if x>0 and x<300 and y>0 and y<300:
			print("azul")
			
		if x>301 and x<600 and y>0 and y<300:
			print("vermelho")
			
		if x>0 and x<300 and y>300 and y<600:
			print("amarelo")
			
		if x>301 and x<600 and y>300 and y<600:
			print("verde")
		
			
		print(pos_mouse)
		botoes_mouse= pygame.mouse.get_pressed()
		if x>275 and x<325 and y>275 and y<325:
			print("botao")
			if botoes_mouse[0]:
				pygame.time.delay(1000)
				def tela_jogo():
										
					#RT inicio
					tela.blit(botao1,(0,0))
					tela.blit(botao2,(300,0))
					tela.blit(botao4,(0,300))
					tela.blit(botao3,(300,300))
					tela.blit(botaoON,(275,275))
				    #RT fim
					
					sequencia = ["verde", "vermelho", "azul","amarelo"]
					sequencia_jogo = []
					sequencia_jogador=[]
					req = urllib.request.Request(url='http://iglicky.pythonanywhere.com/')
					urllib.request.urlopen(req)
					req = urllib.request.Request(url='http://iglicky.pythonanywhere.com/novo')
					urllib.request.urlopen(req)
					req = urllib.request.Request(url='http://iglicky.pythonanywhere.com/mostra')
					with urllib.request.urlopen(req) as f:
						sequencia_jogo=f.read().decode('utf-8')
					sequencia_jogo=sequencia_jogo.split(',')
					sequencia_jogo[-1]="brunoartc"
					print(sequencia_jogo)
					posicao=0
					while True:
						for evento in pygame.event.get():
							if evento.type == QUIT:
								pygame.quit()
								sys.exit()
						tela.blit(botao1,(0,0))
						tela.blit(botao2,(300,0))
						tela.blit(botao3,(0,300))
						tela.blit(botao4,(300,300))
						
						
						#apresenta a sequencia 
						for i in range(posicao):
							botao=sequencia_jogo[i]
						
							if botao=="amarelo":
								tela.blit(botao8,(300,300))
								pygame.display.update()
								tempo = pygame.time.get_ticks()
								pygame.time.delay(1000)
								tela.blit(botao4,(300,300))
								pygame.display.update()
								pygame.time.delay(1000)
								
							if botao=="vermelho":
								tela.blit(botao6,(300,0))
								pygame.display.update()
								tempo = pygame.time.get_ticks()
								pygame.time.delay(1000)
								tela.blit(botao2,(300,0))
								pygame.display.update()
								pygame.time.delay(1000)
									
							if botao=="azul":
								tela.blit(botao5,(0,0))
								pygame.display.update()
								tempo = pygame.time.get_ticks()
								pygame.time.delay(1000)
								tela.blit(botao1,(0,0))
								pygame.display.update()
								pygame.time.delay(1000)
									
							if botao=="verde":
								tela.blit(botao7,(0,300))
								pygame.display.update()
								tempo = pygame.time.get_ticks()
								pygame.time.delay(1000)
								tela.blit(botao3,(0,300))
								pygame.display.update()
								pygame.time.delay(1000)
								
						#aguarda o usuário clicar a sequecia
						print ("clique a sequencia")
						contador = 0
						while (contador) < posicao:
							ev = pygame.event.get()
							for event in ev:
								if event.type == pygame.MOUSEBUTTONUP:
									print ("clicou")
									pygame.time.delay(100)
									pos_mouse= pygame.mouse.get_pos()
									x= pos_mouse[0]
									y= pos_mouse[1]
									if x>0 and x<300 and y>0 and y<300:
										#print("azul")
										botaoSobre = "azul"
									if x>301 and x<600 and y>0 and y<300:
										#print("vermelho")
										botaoSobre = "vermelho"
									if x>0 and x<300 and y>300 and y<600:
										#print("verde")
										botaoSobre = "verde"
									if x>301 and x<600 and y>294 and y<600:
										#print("amarelo")
										botaoSobre = "amarelo"
									
									if sequencia_jogo[contador] == botaoSobre:
										print("acertou"+botaoSobre)
									elif sequencia_jogo[contador] != botaoSobre:
										pygame.quit()
										sys.exit()
									if x>275 and x<325 and y>275 and y<325:
										pygame.quit()
										sys.exit()
									contador+=1
								if evento.type == QUIT:
									pygame.quit()
									sys.exit()
						posicao+=1
						print ("apresentando a sequencia")
				tela_jogo()
		
		if x>0 and x<100 and y>516 and y<586:
			print("online")
			if botoes_mouse[0]:
				def tela_online():
									
					
					while True:
						for evento in pygame.event.get():
							if evento.type == QUIT:
								pygame.quit()
								sys.exit()
						tela.blit(botao1,(0,0))
						tela.blit(botao2,(300,0))
						tela.blit(botao4,(0,300))
						tela.blit(botao3,(300,300))
						pygame.display.update()
						
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
							#print("verde")
							if botoes_mouse[0]:
								tela.blit(botao8,(0,300))
								print("verde")
						if x>301 and x<600 and y>294 and y<586:
							#print("amarelo")	
							if botoes_mouse[0]:
								tela.blit(botao7,(300,300))
								print("amarelo")
								
						pygame.display.update()
						
				tela_online()

		
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
						
				tela_ranking()
		
		pygame.display.update()
		
print(tela_inicial())