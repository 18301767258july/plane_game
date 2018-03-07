#!/usr/bin/python

#get keyboard event
key_pressed = pygame.key.get_pressed()
# handle keyboard event
if key_pressed[K_w] or key_pressed[K_UP]:
    player.moveUp()
if key_pressed[K_s] or key_pressed[K_DOWN]:
    player.movedOWN()
if key_pressed[K_a] or key_pressed[K_LEFT]:
    player.moveLeft()
if key_pressed[K_d] or key_pressed[K_RIGHT]:
    player.moveRight()

