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
	
	tela_rect = tela.get_rect()
	#rect single player
	rect = pygame.Rect(25, 350, 250, 100)
	pygame.draw.rect(tela, pygame.Color("blue"), rect, 10)
	pygame.display.flip()
	#texto singleplayer
	fonte = pygame.font.SysFont("dejavusans" , 30)
	texto1 = fonte.render('Single Player', True, (0,0,255))
	tela.blit(texto1, (55, 380))
	pygame.display.update()

	#rect multiplayer
	rect = pygame.Rect(325,350, 250, 100)
	pygame.draw.rect(tela, pygame.Color("red"), rect, 10)
	pygame.display.flip()
	#texto multiplayer
	fonte = pygame.font.SysFont("dejavusans" , 30)
	texto2 = fonte.render('Multiplayer', True, (255,0,0))
	tela.blit(texto2, (365, 380))
	pygame.display.update()
	
	#rect credits
	rect = pygame.Rect(225,480, 150, 75)
	pygame.draw.rect(tela, pygame.Color("green"), rect, 10)
	pygame.display.flip()
	#texto credits
	fonte = pygame.font.SysFont("dejavusans" , 30)
	texto2 = fonte.render('Credits', True, (0,255,0))
	tela.blit(texto2, (250, 500))
	pygame.display.update()
	
	#texto título
	fonte2 = pygame.font.SysFont("kristenitc" , 75)
	titulo = fonte2.render('Genius Game', True, (255,200,0))
	tela.blit(titulo, (55, 110))
	pygame.display.update()
	
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
	botaoON = pygame.image.load("botao.jpg").convert_alpha()
	botaoON = pygame.transform.scale(botaoON, (100,100))
	
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
			
			
		pos_mouse= pygame.mouse.get_pos()
		x= pos_mouse[0]
		y= pos_mouse[1]
		
		if x>25 and x<275 and y>350 and y<450:
			print("Single Player")
			
		if x>325 and x<575 and y>350 and y<450:
			print("Multiplayer")
			
		if x>225 and x<375 and y>480 and y<555:
			print("Credits")	
		
		print(pos_mouse)
		if x>225 and x<375 and y>480 and y<555:
			print("Credits")	
			if botoes_mouse[0]:
				pygame.time.delay(500)
				Texto = '''"CRÉDITOS

						Integrantes:

						Alfredo Acerbi
						Ariel R. Iglicky
						Thomas Pilnik
						Tiago Mingossi

						Professores:

						Romero Tori
						Daniel Carvalho

						Amigos:

						Toranja Monster

						Uma inspiração...
						"Minha terra tem palmeiras,
						Onde canta o sabiá;
						As aves, que aqui gorjeiam,
						Não gorjeiam como lá.

						Nosso céu tem mais estrelas,
						Nossas várzeas têm mais flores,
						Nossos bosques têm mais vida,
						Nossa vida mais amores."

						Obrigado, Python
						"Is this a bug or a feature?
						Yes"
						"O que uma laranja disse pra um tomate?
						Python"

						pygame.quit
						'''.split('\n')

class Credits:
    def __init__(self, screen_rect, lst):
        self.srect = screen_rect
        self.lst = lst
        self.size = 16
        self.color = (255,0,0)
        self.buff_centery = self.srect.height/2 + 5
        self.buff_lines = 50
        self.timer = 0.0
        self.delay = 30
        self.make_surfaces()


    def Conf_texto(self,message):
        font = pg.font.SysFont('Arial', self.size)
        text = font.render(message,True,self.color)
        rect = text.get_rect(center = (self.srect.centerx, self.srect.centery + self.buff_centery) )
        return text,rect

    def make_surfaces(self):
        self.text = []
        for i, line in enumerate(self.lst):
            l = self.Conf_texto(line)
            l[1].y += i*self.buff_lines
            self.text.append(l)

    def update(self):
        if pg.time.get_ticks()-self.timer > self.delay:
            self.timer = pg.time.get_ticks()
            for text, rect in self.text:
                rect.y -= 1

    def render(self, surf):
        for text, rect in self.text:
            surf.blit(text, rect)

screen = pg.display.set_mode((600,600))
screen_rect = screen.get_rect()
clock = pg.time.Clock()
done = False
cred = Credits(screen_rect, Texto)

while not done:
    for event in pg.event.get(): 
        if event.type == pg.QUIT:
            done = True
    screen.fill((0,0,0))
    cred.update()
    cred.render(screen)
#    pg.display.update()
    clock.tick(60)
					

		if x>325 and x<575 and y>350 and y<450:
			print("online")
			if botoes_mouse[0]:
				pygame.time.delay(500)
				def tela_online():	
					#RT inicio
					tela.blit(botao1,(0,0))
					tela.blit(botao2,(300,0))
					tela.blit(botao4,(0,300))
					tela.blit(botao3,(300,300))
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
						tela.blit(botao3,(300,300))
						tela.blit(botao4,(0,300))
						
						
						#apresenta a sequencia 
						for i in range(posicao):
							botao=sequencia_jogo[i]
						
							if botao=="amarelo":
								tela.blit(botao8,(0,300))
								pygame.display.update()
								tempo = pygame.time.get_ticks()
								pygame.time.delay(1000)
								tela.blit(botao4,(0,300))
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
								tela.blit(botao7,(300,300))
								pygame.display.update()
								tempo = pygame.time.get_ticks()
								pygame.time.delay(1000)
								tela.blit(botao3,(300,300))
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
									if x>0 and x<300 and y>301 and y<600:
										#print("verde")
										botaoSobre = "amarelo"
									if x>301 and x<600 and y>301 and y<600:
										#print("amarelo")
										botaoSobre = "verde"
									
									if sequencia_jogo[contador] == botaoSobre:
										print("acertou"+botaoSobre)
									elif sequencia_jogo[contador] != botaoSobre:
										tela_inicial()
										print("errou"+botaoSobre)
									if x>325 and x<575 and y>350 and y<450:
										pygame.quit()
										sys.exit()
									contador+=1
								if evento.type == QUIT:
									pygame.quit()
									sys.exit()
						posicao+=1
						print ("apresentando a sequencia")
				tela_online()
	
		if x>25 and x<275 and y>350 and y<450:
			print("jogo")
			if botoes_mouse[0]:
				pygame.time.delay(500)
				def tela_jogo():
					tela.blit(botao1,(0,0))
					tela.blit(botao2,(300,0))
					tela.blit(botao3,(300,300))
					tela.blit(botao4,(0,300))
					
					sequencia = ["verde", "vermelho", "azul","amarelo"]
					sequencia_jogo = []
					sequencia_jogador=[]
					for i in range(100):
						sequencia_jogo.append(random.choice(sequencia))
					print(sequencia_jogo)
					posicao=0
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
						
						for i in range(posicao):
							botao=sequencia_jogo[i]
						
							if botao=="amarelo":
								tela.blit(botao8,(0,300))
								pygame.display.update()
								tempo = pygame.time.get_ticks()
								pygame.time.delay(1000)
								tela.blit(botao4,(0,300))
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
								tela.blit(botao7,(300,300))
								pygame.display.update()
								tempo = pygame.time.get_ticks()
								pygame.time.delay(1000)
								tela.blit(botao3,(300,300))
								pygame.display.update()
								pygame.time.delay(1000)
								
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
									if x>0 and x<300 and y>301 and y<600:
										#print("verde")
										botaoSobre = "amarelo"
									if x>301 and x<600 and y>301 and y<600:
										#print("amarelo")
										botaoSobre = "verde"
									
									if sequencia_jogo[contador] == botaoSobre:
										print("acertou"+botaoSobre)
									elif sequencia_jogo[contador] != botaoSobre:
										tela_inicial()
										print("errou"+botaoSobre)
									if x>25 and x<275 and y>350 and y<450:
										pygame.quit()
										sys.exit()
									contador+=1
								if evento.type == QUIT:
									pygame.quit()
									sys.exit()
						posicao+=1
						print ("apresentando a sequencia")														
				tela_jogo()
				
		pygame.display.update()
		
print(tela_inicial())