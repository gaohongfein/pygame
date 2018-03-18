#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Gao hongfei
#Time: 2018.03.01

my_name = "Will McGugan"
import pygame

pygame.init()
my_font = pygame.font.SysFont("arial",64)
name_surface = my_font.render(my_name,True,(0,0,0),(255,255,255))
pygame.image.save(name_surface,"name.png")
