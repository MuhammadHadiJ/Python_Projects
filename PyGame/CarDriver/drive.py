import pygame

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Carefull driving")
icon = pygame.image.load('Car2.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('car.png')
PlayerX = 395
PlayerY = 480
PlayerYChange = 0
Score = 0
Carrotation = 0

def Playerimg(x,y):
    screen.blit(playerimg,(x,y))

# Player 2
playerimg2 = pygame.image.load('car2.png')
PlayerX2 = 335
PlayerY2 = 480
PlayerYChange2 = 0
Carrotation2 = 0

def Playerimg2(x,y):
    screen.blit(playerimg2,(x,y))

# Game loop
game_open = True
while game_open == True:
    screen.fill((15, 190, 221))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_open = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerimg = pygame.transform.rotate(playerimg,90)
                Carrotation += 90
                if Carrotation == 360:
                    Carrotation = 0
                if Carrotation == 270:
                    Carrotation = -90
                print(Carrotation)
            
            if event.key == pygame.K_RIGHT:
                playerimg = pygame.transform.rotate(playerimg,-90)
                Carrotation -= 90
                if Carrotation == -270:
                    Carrotation = 90
                if Carrotation == -360:
                    Carrotation = 0
                if Carrotation == -180:
                    Carrotation = 180
                print(Carrotation)
            
            if event.key == pygame.K_UP:
                PlayerYChange = -0.3
            
            if event.key == pygame.K_DOWN:
                PlayerYChange = 0.3
            
            # Car 2 controls
            if event.key == pygame.K_a:
                playerimg2 = pygame.transform.rotate(playerimg2,90)
                Carrotation2 += 90
                if Carrotation2 == 360:
                    Carrotation2 = 0
                if Carrotation2 == 270:
                    Carrotation2 = -90
                print(Carrotation2)
            
            if event.key == pygame.K_d:
                playerimg2 = pygame.transform.rotate(playerimg2,-90)
                Carrotation2 -= 90
                if Carrotation2 == -270:
                    Carrotation2 = 90
                if Carrotation2 == -360:
                    Carrotation2 = 0
                if Carrotation2 == -180:
                    Carrotation2 = 180
                print(Carrotation2)
            
            if event.key == pygame.K_w:
                PlayerYChange2 = -0.3
            
            if event.key == pygame.K_s:
                PlayerYChange2 = 0.3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                PlayerYChange = 0
            
            if event.key == pygame.K_DOWN:
                PlayerYChange = 0
            
            # Player 2 controls
            if event.key == pygame.K_w:
                PlayerYChange2 = 0
            
            if event.key == pygame.K_s:
                PlayerYChange2 = 0

    if Carrotation == 0:
        PlayerY += PlayerYChange
    if Carrotation == 180:
        PlayerY -= PlayerYChange
    if Carrotation == 90:
        PlayerX += PlayerYChange
    if Carrotation == -90:
        PlayerX -= PlayerYChange
    
    # Player 2 controls
    if Carrotation2 == 0:
        PlayerY2 += PlayerYChange2
    if Carrotation2 == 180:
        PlayerY2 -= PlayerYChange2
    if Carrotation2 == 90:
        PlayerX2 += PlayerYChange2
    if Carrotation2 == -90:
        PlayerX2 -= PlayerYChange2
    Playerimg(PlayerX,PlayerY)
    Playerimg2(PlayerX2,PlayerY2)
    pygame.display.update()