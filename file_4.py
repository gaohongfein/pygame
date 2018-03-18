#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Gao hongfei
#Time: 2018.03.01

import pygame
from sys import exit
from pygame.locals import *


pygame.init()
SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)

font = pygame.font.SysFont("arial",16)
font_height = font.get_linesize()
event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))

    if event.type == QUIT:
        exit()
    screen.fill((255,255,255))

    y = SCREEN_SIZE[1] - font_height
    for text in reversed(event_text):
        screen.blit(font.render(text,True,(0,255,0)),(0,y))
        y-=font_height

    pygame.display.update()
