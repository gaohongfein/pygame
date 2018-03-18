#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Gao hongfei
#Time: 2018.03.01

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)
sprite_1 = pygame.image.load(sprite_image_filename)
# Clock对象
clock = pygame.time.Clock()

x = 0.
y = 0.
# 速度（像素/秒）
speed_x,speed_y = 2.,2.
# clock = pygame.time.Clock()
# time_passed = clock.tick()
# speed_x,speed_y = 2.*time_passed,2.*time_passed

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, y))
    screen.blit(sprite_1, (x+100, y+100))
    time_passed = clock.tick(100)
    time_passed_seconds = time_passed / 1000.0

    x += speed_x
    y += speed_y

    # 想一下，这里减去640和直接归零有何不同？

    if x > 640.-sprite.get_width():
        speed_x = -speed_x
    elif x < 0:
        speed_x = -speed_x
    if y > 480. - sprite.get_height():
        speed_y = -speed_y
    elif y < 0:
        speed_y = -speed_y




    pygame.display.update()