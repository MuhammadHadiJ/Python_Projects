import pygame
import random
import math
from pygame import mixer

# initialize
pygame.init()

# Window
screen = pygame.display.set_mode((800, 600))

#BG
BG = pygame.image.load('BG.png')

# Title and Icon
pygame.display.set_caption("Space Demo-lishers")
icon = pygame.image.load('Icon2.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('player2.png')
PlayerX = 370
PlayerY = 480
PlayerChange = 0

# Enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
num_enemies = 6

for i in range(num_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(40,140))
    enemyX_Change.append(0.3)
    enemyY_Change.append(40)

# Bullet
bulletimg = pygame.image.load('Bullet.png')
bulletX = 0
bulletY = 480
bulletX_Change = 0
bulletY_Change = 0.5
bullet_State = "ready"

#Score
Score = 0
font = pygame.font.Font('I AM A PLAYER.ttf', 42)
over_font = pygame.font.Font('I AM A PLAYER.ttf', 90)

textX = 10
textY = 10

def showscore(x,y):
    score = font.render("Score: " + str(Score),True,(255,255,255))
    screen.blit(score,(x,y))

def Player(x,y):
    screen.blit(playerimg, (x,y))

def Enemy(x,y,i):
    screen.blit(enemyimg[i], (x,y))

def FIRE(x,y):
    global bullet_State
    bullet_State = "fire"
    screen.blit(bulletimg, (x + 16,y + 10))

def iscollided(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

def gameOver():
        overtxt = over_font.render("Game's Up!",True,(255,255,255))
        screen.blit(overtxt,(175,220))

# Game loop
game_open = True
while game_open == True:
    screen.fill((0, 0, 0))
    screen.blit(BG,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_open = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerChange = -0.5
            if event.key == pygame.K_RIGHT:
                PlayerChange = 0.5
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if bullet_State == "ready":
                    bullet_sound = mixer.Sound('laserShoot.wav')
                    bullet_sound.play()
                    bulletX = PlayerX
                    FIRE(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                PlayerChange = 0
            elif event.key == pygame.K_LEFT:
                PlayerChange = 0

    PlayerX += PlayerChange
    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    for i in range(num_enemies):
        
        if enemyY[i] > 410:
            for j in range(num_enemies):
                enemyY[j] = 2000
            gameOver()
            break
        
        enemyX[i] += enemyX_Change[i]
        if enemyX[i] <= 0:
            enemyX_Change[i] = 0.3
            enemyY[i] += enemyY_Change[i]
        elif enemyX[i] >= 736:
            enemyX_Change[i] = -0.3
            enemyY[i] += enemyY_Change[i]
    
        #Collision
        collision = iscollided(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_State = "ready"
            Score += 1
            expo_sound = mixer.Sound('explosion.wav')
            expo_sound.play()
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(40,140)

        Enemy(enemyX[i], enemyY[i], i)
    
    #Fire mechanisim
    if bullet_State is "fire":
        FIRE(bulletX,bulletY)
        if bulletY > 0:
            bulletY -= bulletY_Change
        elif bulletY <= 0:
            bullet_State = "ready"
            bulletY = 480


    Player(PlayerX, PlayerY)
    showscore(textX,textY)
    pygame.display.update()
