import pygame
import sys

#Intialization
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Bubbling A Potion Of Trouble")
icon = pygame.image.load('Icon.png')
pygame.display.set_icon(icon)
screen_X = 800
screen_Y = 500
screen = pygame.display.set_mode((screen_X,screen_Y))

# Images
rect1 = pygame.Rect(375,90,50,50)
Y_speed = 4
#X_speed = 5
rect2 = pygame.Rect(0,450,800,50)
# Player
pl_X = 386
pl_y = 383
plvelminus = 10
Plyr_rect = pygame.Rect(pl_X, pl_y, 28, 65)

def Player():
    PL = pygame.draw.rect(screen, (255,255,255), Plyr_rect)

def Drawing_Rects():
    global X_speed
    global Y_speed
    #rect1.x += X_speed
    rect1.y += Y_speed
    
    if rect1.right >= screen_X or rect1.left <= 0:
        X_speed *= -1

    if rect1.bottom >= rect2.top or rect1.top <= 0:
        Y_speed *= -1
    
    pygame.draw.rect(screen, (255,255,255), rect1)
    pygame.draw.rect(screen, (37,37,37), rect2)

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
    
    screen.fill((29,17,19))

    Player()
    Drawing_Rects()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if keys[pygame.K_SPACE]:

            pl_X -= plvelminus
            print("Works to left")

    pygame.display.flip()
    clock.tick(60)