import random 
import pygame
import math
from pygame import mixer  
pygame.init() 
screen = pygame.display.set_mode((800,600))
mixer.music.load('background.mp3')
mixer.music.play(-1) 
pygame.display.set_caption("Space Invaders") 
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
EnemyImg  = []
enemyX = []
enemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 3
for i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,180))
    EnemyX_change.append(5)
    EnemyY_change.append(40)
backgroundImg = pygame.image.load('background.png')
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
score_value = 0   
font = pygame.font.Font('freesansbold.ttf',22)
textX = 10
textY = 10
over_font = font = pygame.font.Font('freesansbold.ttf',66)
def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))
def player(x,y):
    screen.blit(playerImg, (x,y))
def enemy(x,y, i):
    screen.blit(EnemyImg[i], (x,y))
def background():
    screen.blit(backgroundImg, (0,0))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(bulletX-enemyX,2) + math.pow(bulletY-enemyY,2))
    if distance < 50 :
        return True
    else:
        return False 
runnig = True
while runnig:
    screen.fill((1,100,1)) 
    background()
    for eventt in pygame.event.get():
        if eventt.type == pygame.QUIT:
             runnig = False
        if eventt.type == pygame.KEYDOWN:
            if eventt.key == pygame.K_LEFT:
                playerX_change = -6
            if eventt.key == pygame.K_RIGHT:
                playerX_change = 6
            if eventt.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        if eventt.type == pygame.KEYUP:
            if eventt.key == pygame.K_LEFT or eventt.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    for i in range(num_of_enemies):
        if enemyY[i] > 430:
            for j in range(num_of_enemies):
                enemyY[j]= 2000
            game_over_text()
            mixer.music.play(0) 
            break
        enemyX[i] += EnemyX_change[i]
        if enemyX[i] <= 0:
            EnemyX_change[i] = 5
            enemyY[i] += EnemyY_change[i]
        elif enemyX[i] >= 770:
            EnemyX_change[i] = -5
            enemyY[i] += EnemyY_change[i]
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 100
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,180)
        enemy(enemyX[i],enemyY[i], i)
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    player(playerX,playerY)
    show_score(textX, textY)
    pygame.display.update()
