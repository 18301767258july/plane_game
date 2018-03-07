#!/usr/bin/python
# -*- coding:utf-8 -*-

import pygame
#init pygame
pygame.init()

#set game screen size,background img,caption etc

#set screen
screen = pygame.display.set_mode((480,800))

#set caption

pygame.display.set_caption("plane shoot")

#set background image
background = pygame.image.load("resources/image/background.png").convert()

#get game plane image
plane_imgs = pygame.image.load("resources/image/shoot.png")

#get player plane image
player = plane_imgs.subsurface(pygame.Rect(0,99,102,126))

#main circle to handle init,update,exit

while True:
    #init screen
    screen.fill(0)
    screen.blit(background,(0,0))
    #display player plane location
    screen.blit(player,[200,600])
    #update screen
    pygame.display.update()

    #exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()








