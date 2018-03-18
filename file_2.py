#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Gao hongfei
#Time: 2018.03.01

import pygame
from pygame.locals import *

pygame.init()
SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode((640,480),0,32)

font = pygame.font.SysFont("arial",16)
font_height = font.get_linesize()
event_text = []
while True:
    event = pygame.event.wait()
    event_text.append(str(event))

    event_text = event_text[int(-SCREEN_SIZE[1]/font_height):]

    if event.type == QUIT:
        exit()

    screen.fill((255,255,255))
    y = SCREEN_SIZE[1] - font_height

    #找一个合适的起笔位置，最下面开始但是要留一行的空
    for text in reversed(event_text):
        screen.blit( font.render(text, True, (0, 0, 0)), (0, y) )
        #以后会讲
        y-=font_height
            #把笔提一行




    pygame.display.update()