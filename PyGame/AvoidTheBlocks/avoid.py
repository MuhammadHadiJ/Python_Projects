import time
import pygame
import random
import math
from pygame import mixer

# Start Up
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Avoid The Blocks")
icon = pygame.image.load('Icon.png')
pygame.display.set_icon(icon)
Gameopen = True
gamesup = False

#Score
Score = 0
font = pygame.font.Font('I AM A PLAYER.ttf', 42)
over_font = pygame.font.Font('I AM A PLAYER.ttf', 90)

textX = 10
textY = 10

def showscore(x,y):
    score = font.render("Score: " + str(Score),True,(255,255,255))
    screen.blit(score,(x,y))

# Game Over
over_font = pygame.font.Font('I AM A PLAYER.ttf', 90)
def gameOver():
        overtxt = over_font.render("Game's Up!",True,(255,255,255))
        screen.blit(overtxt,(175,220))

# Player
playerimg = pygame.image.load('Player.png')
PlayerX = 370
PlayerY = 480
PlayerChange = 0
Score = 0

# Blocks
Objectimg = pygame.image.load('Player.png')
emptySpace = random.randint(1,7)
FallSpeed = 0.3
blocky = 20.0

# if blocks are 24 pixels below player than the player has won

# Block 1
block1x = 68

# Block 2
block2x = 168

# Block 3
block3x = 268

# Block 4
block4x = 368

# Block 5
block5x = 468

# Block 6
block6x = 568

# Block 7
block7x = 668

allxs = block1x, block2x, block3x, block4x, block5x, block6x, block7x

def Player(x,y):
    screen.blit(playerimg,(x,y))

def Block(x,y):
    screen.blit(Objectimg,(x,y))

def iscollided1(block1x, blocky, PlayerX, PlayerY):
    distance = math.sqrt(math.pow(block1x - float(PlayerX), 2) + math.pow(blocky - PlayerY, 2))
    if distance < 27:
        return True
    else:
        return False

def iscollided2(block2x, blocky, PlayerX, PlayerY):
    distance = math.sqrt(math.pow(block2x - float(PlayerX), 2) + math.pow(blocky - PlayerY, 2))
    if distance < 27:
        return True
    else:
        return False

def iscollided3(block3x, blocky, PlayerX, PlayerY):
    distance = math.sqrt(math.pow(block3x - float(PlayerX), 2) + math.pow(blocky - PlayerY, 2))
    if distance < 27:
        return True
    else:
        return False

def iscollided4(block4x, blocky, PlayerX, PlayerY):
    distance = math.sqrt(math.pow(block4x - float(PlayerX), 2) + math.pow(blocky - PlayerY, 2))
    if distance < 27:
        return True
    else:
        return False

def iscollided5(block5x, blocky, PlayerX, PlayerY):
    distance = math.sqrt(math.pow(block5x - float(PlayerX), 2) + math.pow(blocky - PlayerY, 2))
    if distance < 27:
        return True
    else:
        return False

def iscollided6(block6x, blocky, PlayerX, PlayerY):
    distance = math.sqrt(math.pow(block6x - float(PlayerX), 2) + math.pow(blocky - PlayerY, 2))
    if distance < 27:
        return True
    else:
        return False

def iscollided7(block7x, blocky, PlayerX, PlayerY):
    distance = math.sqrt(math.pow(block7x - float(PlayerX), 2) + math.pow(blocky - PlayerY, 2))
    if distance < 27:
        return True
    else:
        return False

# Game loop
game_open = True
while game_open == True:
    screen.fill((15, 190, 221))
    if blocky >= 600 and Gameopen == True:
        Score += 1
        levelup = mixer.Sound('pickupCoin2.wav')
        levelup.play()
        time.sleep(0.2)
        if Score == 5:
            FallSpeed += 0.1
        if Score == 10:
            FallSpeed += 0.1
        if Score == 20:
            FallSpeed += 0.1
        emptySpace = random.randint(1,7)
        blocky = 20.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_open = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerChange = -0.4
                if Score == 5:
                    PlayerChange = -0.5
                if Score == 10:
                    PlayerChange = -0.6
                if Score == 20:
                    PlayerChange = -0.7
                elif Score < 5:
                    PlayerChange = -0.4
            
            if event.key == pygame.K_RIGHT:
                PlayerChange = 0.4
                if Score == 5:
                    PlayerChange = 0.6
                if Score == 10:
                    PlayerChange = 0.7
                if Score == 20:
                    PlayerChange = 0.8
                elif Score < 5:
                    PlayerChange = 0.4
            
            if event.key == pygame.K_r:
                Gameopen = True
                Score = 0
                FallSpeed = 0.3
                emptySpace = random.randint(1,7)
                blocky = 20.0
                
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                PlayerChange = 0
            
            if event.key == pygame.K_RIGHT:
                PlayerChange = 0

    PlayerX += PlayerChange
    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736
    Player(PlayerX,PlayerY)
    blocky += FallSpeed

    # Empty Space
    if emptySpace == 1:
        allblocks = Block(block2x,blocky),Block(block3x,blocky), Block(block4x,blocky), Block(block5x,blocky), Block(block6x,blocky), Block(block7x,blocky)
    if emptySpace == 2:
        allblocks = Block(block1x,blocky), Block(block3x,blocky), Block(block4x,blocky), Block(block5x,blocky), Block(block6x,blocky), Block(block7x,blocky)
    if emptySpace == 3:
        allblocks = Block(block1x,blocky),Block(block2x,blocky), Block(block4x,blocky), Block(block5x,blocky), Block(block6x,blocky), Block(block7x,blocky)
    if emptySpace == 4:
        allblocks = Block(block1x,blocky),Block(block2x,blocky),Block(block3x,blocky), Block(block5x,blocky), Block(block6x,blocky), Block(block7x,blocky)
    if emptySpace == 5:
        allblocks = Block(block1x,blocky),Block(block2x,blocky),Block(block3x,blocky), Block(block4x,blocky), Block(block6x,blocky), Block(block7x,blocky)
    if emptySpace == 6:
        allblocks = Block(block1x,blocky),Block(block2x,blocky),Block(block3x,blocky), Block(block4x,blocky), Block(block5x,blocky), Block(block7x,blocky)
    if emptySpace == 7:
        allblocks = Block(block1x,blocky),Block(block2x,blocky),Block(block3x,blocky), Block(block4x,blocky), Block(block5x,blocky), Block(block6x,blocky)
    # Empty Space
    
    if emptySpace == 1:
        collision = iscollided2(block2x,blocky,PlayerX,PlayerY) or iscollided3(block3x,blocky,PlayerX,PlayerY) or iscollided4(block4x,blocky,PlayerX,PlayerY) or iscollided5(block5x,blocky,PlayerX,PlayerY) or iscollided6(block6x,blocky,PlayerX,PlayerY) or iscollided7(block7x,blocky,PlayerX,PlayerY)
    
    if emptySpace == 2:
        collision = iscollided1(block1x,blocky,PlayerX,PlayerY) or iscollided3(block3x,blocky,PlayerX,PlayerY) or iscollided4(block4x,blocky,PlayerX,PlayerY) or iscollided5(block5x,blocky,PlayerX,PlayerY) or iscollided6(block6x,blocky,PlayerX,PlayerY) or iscollided7(block7x,blocky,PlayerX,PlayerY)
    
    if emptySpace == 3:
        collision = iscollided1(block1x,blocky,PlayerX,PlayerY) or iscollided2(block2x,blocky,PlayerX,PlayerY) or iscollided4(block4x,blocky,PlayerX,PlayerY) or iscollided5(block5x,blocky,PlayerX,PlayerY) or iscollided6(block6x,blocky,PlayerX,PlayerY) or iscollided7(block7x,blocky,PlayerX,PlayerY)
    
    if emptySpace == 4:
        collision = iscollided1(block1x,blocky,PlayerX,PlayerY) or iscollided2(block2x,blocky,PlayerX,PlayerY) or iscollided3(block3x,blocky,PlayerX,PlayerY) or iscollided5(block5x,blocky,PlayerX,PlayerY) or iscollided6(block6x,blocky,PlayerX,PlayerY) or iscollided7(block7x,blocky,PlayerX,PlayerY)

    if emptySpace == 5:
        collision = iscollided1(block1x,blocky,PlayerX,PlayerY) or iscollided2(block2x,blocky,PlayerX,PlayerY) or iscollided3(block3x,blocky,PlayerX,PlayerY) or iscollided4(block4x,blocky,PlayerX,PlayerY) or iscollided6(block6x,blocky,PlayerX,PlayerY) or iscollided7(block7x,blocky,PlayerX,PlayerY)
    
    if emptySpace == 6:
        collision = iscollided1(block1x,blocky,PlayerX,PlayerY) or iscollided2(block2x,blocky,PlayerX,PlayerY) or iscollided3(block3x,blocky,PlayerX,PlayerY) or iscollided4(block4x,blocky,PlayerX,PlayerY) or iscollided5(block5x,blocky,PlayerX,PlayerY) or iscollided7(block7x,blocky,PlayerX,PlayerY)
    
    if emptySpace == 7:
        collision = iscollided1(block1x,blocky,PlayerX,PlayerY) or iscollided2(block2x,blocky,PlayerX,PlayerY) or iscollided3(block3x,blocky,PlayerX,PlayerY) or iscollided4(block4x,blocky,PlayerX,PlayerY) or iscollided5(block5x,blocky,PlayerX,PlayerY) or iscollided6(block6x,blocky,PlayerX,PlayerY)
    
    
    if collision:
        lost = mixer.Sound('hitHurt.wav')
        lost.play()
        Gameopen = False

    if Gameopen == False:
        gameOver()
    showscore(textX,textY)
    pygame.display.update()