from operator import index
import pygame
import random

# Start Up
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Crossy road")
icon = pygame.image.load('Icon.png')
pygame.display.set_icon(icon)
b1x = 0
b1y = 0


grimg = pygame.image.load('ground.png')
def groundimg(x,y):
    screen.blit(grimg,(x,y))

plimg = pygame.image.load('Chicken3.png')
def Playerimg(x,y):
    screen.blit(plimg,(x,y))

game_open = True
while game_open == True:
    screen.fill((0, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_open = False
    
    groundimg(b1x,b1y)
    if b1x == 0 and b1y == 0:
        ranblock = random.randint(0,1)
        if ranblock == 0:
            print("block 0 chosed")
        elif ranblock == 1:
            print("block 1 chosed")
    Playerimg(50,275)
    b1x -= 0.5
    pygame.display.update()