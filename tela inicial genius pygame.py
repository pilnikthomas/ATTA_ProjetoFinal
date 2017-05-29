import sys
import pygame as pg
from pygame.locals import *



pg.init()
tela = pg.display.set_mode((1000,800))
pg.display.set_caption('Tela inicial Genius')
tela_rect = tela.get_rect()

#rect single player
rect = pg.Rect(150,400, 300, 150)

pg.draw.rect(tela, pg.Color("blue"), rect, 10)
pg.display.flip()


#rect multiplayer
rect = pg.Rect(550,400, 300, 150)

pg.draw.rect(tela, pg.Color("red"), rect, 10)
pg.display.flip()

#rect configurações
rect = pg.Rect(150,600, 300, 150)

pg.draw.rect(tela, pg.Color("yellow"), rect, 10)
pg.display.flip()


#rect ranking
rect = pg.Rect(550,600, 300, 150)

pg.draw.rect(tela, pg.Color("green"), rect, 10)
pg.display.flip()

#texto singleplayer
fonte = pg.font.SysFont("dejavusans" , 50)
texto1 = fonte.render('Single Player', True, (0,0,255))
tela.blit(texto1, (190, 420))
pg.display.update()

#texto multiplayer
texto2 = fonte.render('Multiplayer', True, (255,0,0))
tela.blit(texto2, (610, 420))
pg.display.update()

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
        
#texto título
fonte2 = pg.font.SysFont("kristenitc" , 88)
titulo = fonte2.render('Genius Game', True, (255,200,0))
tela.blit(titulo, (210, 110))
pg.display.update()


while pg.event.poll().type != pg.QUIT:
    pass
pg.quit()
sys.exit()
