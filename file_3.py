#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Gao hongfei
#Time: 2018.03.01


import pygame
from pygame.locals import *
background_image_filename = '/home/gao/图片/sushiplate.jpg'
pygame.init()

screen = pygame.display.set_mode((640,320),0,32)
background = pygame.image.load(background_image_filename).convert()

x,y = 0, 0
move_x, move_y = 0,0

while True:
    # for event in pygame.event.get():
    #     if event.type == QUIT:
    #         exit()
    #     if event.type == KEYDOWN:
    #         if event.key == K_LEFT:
    #             move_x = 1
    #         elif event.key == K_RIGHT:
    #             move_y = -1
    #         elif event.key == K_UP:
    #             move_y = -1
    #         elif event.key == K_DOWN:
    #             move_y = 1
    #     elif event.type ==KEYUP:
    #         move_y = 0
    #         move_x = 0
    #
    # x += move_x
    # y += move_y

    screen.fill((0,0,0))
    screen.blit(background,(x,y))
    pygame.display.update()

