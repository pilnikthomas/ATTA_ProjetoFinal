# -*- coding: utf-8 -*-
"""
Created on Sat May  6 17:23:45 2017

@author: Thomas Pilnik
"""

import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((1500, 1500))
image = pygame.image.load('simon.jpg')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            
    screen.fill((200, 200, 200))
    screen.blit(image, (750, 750))
    pygame.display.flip()
        