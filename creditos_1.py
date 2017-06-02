import pygame as pg

pg.init()

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
        self.size = 13
        self.color = (255,0,0)
        self.buff_centery = self.srect.height/2 + 5
        self.buff_lines = 50
        self.timer = 0.0
        self.delay = 15
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
    pg.display.update()
    clock.tick(200)