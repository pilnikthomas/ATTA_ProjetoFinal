import sys
import pygame as pg
from pygame.locals import *
import time


pg.init()
tela = pg.display.set_mode((600,600))
pg.display.set_caption('Tela inicial Genius')
tela_rect = tela.get_rect()

#rect single player
rect = pg.Rect(25, 350, 250, 100)

pg.draw.rect(tela, pg.Color("blue"), rect, 10)
pg.display.flip()

#rect multiplayer
rect = pg.Rect(325,350, 250, 100)

pg.draw.rect(tela, pg.Color("red"), rect, 10)
pg.display.flip()

#rect credits
rect = pg.Rect(225,480, 150, 75)

pg.draw.rect(tela, pg.Color("green"), rect, 10)
pg.display.flip()
	
	


while True:
		for evento in pg.event.get():
			if evento.type == QUIT:
				pg.quit()
				sys.exit()
		
		pos_mouse = pg.mouse.get_pos()
		x = pos_mouse[0]
		y = pos_mouse[1]
		
		if x>25 and x<275 and y>350 and y<450:
			print("Single Player")
					
		if x>325 and x<575 and y>350 and y<450:
			print("Multiplayer")
					
		if x>225 and x<375 and y>480 and y<555:
			print("Credits")
						

		'''

		#rect configurações
		rect = pg.Rect(150,600, 300, 150)

		pg.draw.rect(tela, pg.Color("yellow"), rect, 10)
		pg.display.flip()


		#rect ranking
		rect = pg.Rect(550,600, 300, 150)

		pg.draw.rect(tela, pg.Color("green"), rect, 10)
		pg.display.flip()

		'''

		#texto singleplayer
		fonte = pg.font.SysFont("dejavusans" , 30)
		texto1 = fonte.render('Single Player', True, (0,0,255))
		tela.blit(texto1, (55, 380))
		pg.display.update()

		#texto multiplayer
		fonte = pg.font.SysFont("dejavusans" , 30)
		texto2 = fonte.render('Multiplayer', True, (255,0,0))
		tela.blit(texto2, (365, 380))
		pg.display.update()

		#texto credits
		fonte = pg.font.SysFont("dejavusans" , 30)
		texto2 = fonte.render('Credits', True, (0,255,0))
		tela.blit(texto2, (250, 500))
		pg.display.update()


		'''

		#texto configurações
		texto3 = fonte.render('Configurações', True, (255,255,0))
		tela.blit(texto3, (180, 620))
		pg.display.update()

		#texto configurações
		texto3 = fonte.render('Configurações', True, (255,255,0))
		tela.blit(texto3, (180, 620))
		pg.display.update()

		#texto ranking
		texto4 = fonte.render('Ranking', True, (0,255,0))
		tela.blit(texto4, (630, 620))
		pg.display.update()
			  
		'''
			  
		#texto título
		fonte2 = pg.font.SysFont("kristenitc" , 75)
		titulo = fonte2.render('Genius Game', True, (255,200,0))
		tela.blit(titulo, (55, 110))
		pg.display.update()


while pg.event.poll().type != pg.QUIT:
    pass
pg.quit()
sys.exit()
