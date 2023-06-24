import pygame

# Initialization
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Bubble Drouble")
# icon = pygame.image.load('Icon.png')
# pygame.display.set_icon(icon)
BG = pygame.image.load("D:\Python\PyGame\Bubble trouble\BG.png")
screen.blit(BG, (0,0))

# static Images & Moving Image Theory
_stage = pygame.image.load("D:\Python\PyGame\Bubble trouble\Stage.png")
stage = screen.blit(_stage, (0,0))

_ball = pygame.image.load("D:\Python\PyGame\Bubble trouble\Ball.png")
y_ball_speed = 9
ball = screen.blit(_ball,(0,0))

def Move_Ball():
    ball += y_ball_speed
    pygame.image.load()

# RUN
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    clock.tick(60)
    pygame.display.update()