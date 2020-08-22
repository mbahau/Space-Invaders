# MD BAHAUDDIN
# NATIONAL INSTITUTE OF TECHNOLOGY
# Space Invaders

# pyGames.org 
# download pip by 'pip install pygame' for package manager
import random
import pygame
# import pygame in our profile
import math
from pygame import mixer
# for music 

# initialize the pygame
pygame.init() 
# without it game will not work

# creating window/screen
screen = pygame.display.set_mode((800,600))
# Width, height
# inside bracket there is another bracket bcz it is tuple and without it wont work
# After few seconds windows go away :(
# So we will create infinite loop 

# Background Music 
mixer.music.load('background.mp3')
mixer.music.play(-1)

# Title & Icon of the window
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
# values depend on the screen,, which is set such that image will appear in the middle 

# Enemy
EnemyImg  = []
# this is list i,e, array
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




# Background set
backgroundImg = pygame.image.load('background.png')

# Bullet
# Ready - you can't see the bullet before fire
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# FONT 
# Score card
score_value = 0   
font = pygame.font.Font('freesansbold.ttf',22)
textX = 10
textY = 10
# positions x,y

# Game Over 
over_font = font = pygame.font.Font('freesansbold.ttf',66)

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))
    # we have to render the text before printing then print/show 


# creating function , loading image , (image x location, image y location) 
def player(x,y):
    screen.blit(playerImg, (x,y))
# added x, y so that player can move on x- & y- axes

# Creating enemy 
def enemy(x,y, i):
    screen.blit(EnemyImg[i], (x,y))

def background():
    screen.blit(backgroundImg, (0,0))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

# for Collision of bullet with enemy we use this function
# they collide when the distance between them becomes 0 
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(bulletX-enemyX,2) + math.pow(bulletY-enemyY,2))
    if distance < 50 :
        return True
    else:
        return False 


"""while True:
    pass"""
# running this loop will hang the program,so we will add quit button
# every things happened by keyboard, cancel/exit button, left, right, up, down bottons are event

# Game Loop 
runnig = True
# running is close button 
while runnig:
    # we change the background
    # we added the red (RGB) color but we did not update the screen
    screen.fill((1,100,1))
    background()
    for eventt in pygame.event.get():
        if eventt.type == pygame.QUIT:
             runnig = False
    
        # if keystroke is pressed whether left or right
        if eventt.type == pygame.KEYDOWN:
            # means keystroke pressed by keyboard
            if eventt.key == pygame.K_LEFT:
                # print("Left is pressed")
                playerX_change = -6
            if eventt.key == pygame.K_RIGHT:
                # print("RIGHT is pressed")
                playerX_change = 6

            # for bullet, if space is precessed bullet  will show
            # since bullet follow space craft so we use bulletX var...

            if eventt.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        # keydown means pressing a key , keyup means releasing a key 
        if eventt.type == pygame.KEYUP:
            if eventt.key == pygame.K_LEFT or eventt.key == pygame.K_RIGHT:
                # print("Keystroke is released")
                playerX_change = 0



    # we added player after screen.fill so that player will come after screen background 
    # otherwise background will overlap the player
    playerX += playerX_change
    # to change the position of spaceship 
    

    # Spaceship should not go beyond the screen
    if playerX <= 0:
        playerX = 0

    if playerX >= 736:
        playerX = 736
    
    # Enemy 
    # Enemy movement 
    for i in range(num_of_enemies):

        # Game over 
        if enemyY[i] > 430:
            for j in range(num_of_enemies):
                enemyY[i]= 2000
            game_over_text()
            break

        enemyX[i] += EnemyX_change[i]
    
        if enemyX[i] <= 0:
            EnemyX_change[i] = 5
            enemyY[i] += EnemyY_change[i]
        elif enemyX[i] >= 770:
            EnemyX_change[i] = -5
            enemyY[i] += EnemyY_change[i]

        # Collision condition
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 100
            # print(score)
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,180)
        
        # displaying enemy 
        enemy(enemyX[i],enemyY[i], i)
    

    # BUllet Movement 
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
        # bullet will fire but can not fire again   

   

    # displaying player craft
    player(playerX,playerY)
    
    show_score(textX, textY)
    # updating the screen
    pygame.display.update()
