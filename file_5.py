#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Gao hongfei
#Time: 2018.03.01

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
background_image_filename = '/home/gao/图片/sushiplate.jpg'
background = pygame.image.load(background_image_filename).convert()
Fullscreen = False
done = False

while not False:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((640,480),FULLSCREEN,32)
                else:
                    screen = pygame.display.set_mode((640,480),0,32)
    screen.blit(background,(0,0))
    pygame.display.update()
