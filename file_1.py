#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Gao hongfei
#Time: 2018.03.01

background_image_filename = '/home/gao/图片/sushiplate.jpg'
mouse_image_filename = '/home/gao/图片/fugu.png'


import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("hello World!")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background,(0,0))

    x,y = pygame.mouse.get_pos()

    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2

    screen.blit(mouse_cursor,(x,y))

    pygame.display.update()