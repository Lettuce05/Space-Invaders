import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Create the screen(width,height)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(30)

# enemy2
enemy2Img = []
enemy2X = []
enemy2Y = []
enemy2X_change = []
enemy2Y_change = []
enemy2_health = []

num_of_enemies2 = 5

for i in range(num_of_enemies2):
    enemy2Img.append(pygame.image.load('enemyGreen.png'))
    enemy2X.append(random.randint(0, 735))
    enemy2Y.append(random.randint(50, 150))
    enemy2X_change.append(4)
    enemy2Y_change.append(30)
    enemy2_health.append(2)

# enemy3
enemy3Img = []
enemy3X = []
enemy3Y = []
enemy3X_change = []
enemy3Y_change = []
enemy3_health = []

num_of_enemies3 = 4

for i in range(num_of_enemies3):
    enemy3Img.append(pygame.image.load('enemyRed.png'))
    enemy3X.append(random.randint(0, 735))
    enemy3Y.append(random.randint(50, 150))
    enemy3X_change.append(2)
    enemy3Y_change.append(30)
    enemy3_health.append(3)

# enemy4
enemy4Img = []
enemy4X = []
enemy4Y = []
enemy4X_change = []
enemy4Y_change = []
enemy4_health = []

num_of_enemies4 = 3

for i in range(num_of_enemies4):
    enemy4Img.append(pygame.image.load('enemyBlue.png'))
    enemy4X.append(random.randint(0, 735))
    enemy4Y.append(random.randint(50, 150))
    enemy4X_change.append(2)
    enemy4Y_change.append(20)
    enemy4_health.append(4)

# enemy5
enemy5Img = []
enemy5X = []
enemy5Y = []
enemy5X_change = []
enemy5Y_change = []
enemy5_health = []

num_of_enemies5 = 5

for i in range(num_of_enemies5):
    enemy5Img.append(pygame.image.load('enemyBrown.png'))
    enemy5X.append(random.randint(0, 735))
    enemy5Y.append(random.randint(50, 150))
    enemy5X_change.append(2)
    enemy5Y_change.append(20)
    enemy5_health.append(5)

# enemy6
enemy6Img = []
enemy6X = []
enemy6Y = []
enemy6X_change = []
enemy6Y_change = []
enemy6_health = []

num_of_enemies6 = 4

for i in range(num_of_enemies6):
    enemy6Img.append(pygame.image.load('enemyYellow.png'))
    enemy6X.append(random.randint(0, 735))
    enemy6Y.append(random.randint(50, 150))
    enemy6X_change.append(2)
    enemy6Y_change.append(20)
    enemy6_health.append(6)

# enemy7
enemy7Img = []
enemy7X = []
enemy7Y = []
enemy7X_change = []
enemy7Y_change = []
enemy7_health = []

num_of_enemies7 = 3

for i in range(num_of_enemies7):
    enemy7Img.append(pygame.image.load('enemyPurple.png'))
    enemy7X.append(random.randint(0, 735))
    enemy7Y.append(random.randint(50, 150))
    enemy7X_change.append(3)
    enemy7Y_change.append(30)
    enemy7_health.append(7)


# bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# player 2 bullet
bullet2Img = pygame.image.load('bullet.png')
bullet2X = 0
bullet2Y = 480
bullet2X_change = 0
bullet2Y_change = 10
bullet2_state = "ready"


# player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Player 2
player2Img = pygame.image.load('player2.png')
player2X = 430
player2Y = 480
player2X_change = 0


# Variable for score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Variable for level
level_value = 1
level_font = pygame.font.Font('freesansbold.ttf', 32)
level_type = "Level: "
level_textX = 650
level_textY = 10

#game over state
game_Over = False

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)
restart_Font = pygame.font.Font('freesansbold.ttf', 24)

#Boss info
boss1Exists = True
boss1Img = pygame.image.load('boss1.png')
boss1health = 4
boss1X = random.randint(0, 735)
boss1Y = random.randint(50, 150)
boss1X_change = 4
boss1Y_change = 30

#Boss2 info
boss2Exists = True
boss2Img = pygame.image.load('boss2.png')
boss2health = 5
boss2X = random.randint(0, 735)
boss2Y = random.randint(50, 150)
boss2X_change = 2
boss2Y_change = 20

#Boss3 info
boss3Exists = True
boss3Img = pygame.image.load('boss3.png')
boss3health = 10
boss3X = random.randint(0, 735)
boss3Y = random.randint(50, 150)
boss3X_change = 2
boss3Y_change = 30


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_level(x, y):
    global level_type
    level = font.render(level_type + str(level_value), True, (255, 255, 255))
    screen.blit(level, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    score_text = font.render("You Scored: " + str(score_value), True, (255, 255, 255))
    screen.blit(score_text, (295, 330))
    restart_text = restart_Font.render("Press 'R' to Restart Game", True, (255, 255, 255))
    screen.blit(restart_text, (255, 430))
    

def player(x, y):
    screen.blit(playerImg, (x, y))

def player2(x, y):
    screen.blit(player2Img, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def enemy2(x, y, i):
    screen.blit(enemy2Img[i], (x, y))

def enemy3(x, y, i):
    screen.blit(enemy3Img[i], (x, y))

def enemy4(x, y, i):
    screen.blit(enemy4Img[i], (x, y))

def enemy5(x, y, i):
    screen.blit(enemy5Img[i], (x, y))

def enemy6(x, y, i):
    screen.blit(enemy6Img[i], (x, y))

def enemy7(x, y, i):
    screen.blit(enemy7Img[i], (x, y))

def fire_bullet (x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def fire_bullet2 (x, y):
    global bullet2_state
    bullet2_state = "fire"
    screen.blit(bullet2Img, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def boss1(x, y):
    if boss1Exists == True:
        screen.blit(boss1Img, (x, y))

def boss2(x, y):
    if boss2Exists == True:
        screen.blit(boss2Img, (x, y))

def boss3(x, y):
    if boss3Exists == True:
        screen.blit(boss3Img, (x, y))

        


def restart_Game():
    global boss1Exists
    global boss1health
    global boss1X
    global boss1Y
    global score_value
    global level_value
    global level_type
    global boss2Exists
    global boss2health
    global boss2X
    global boss2Y
    global boss3Exists
    global boss3health
    global boss3X
    global boss3Y
    # bullet
    # Ready - You can't see the bullet on the screen
    # Fire - The bullet is currently moving
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"

    bullet2X = 0
    bullet2Y = 480
    bullet2X_change = 0
    bullet2Y_change = 10
    bullet2_state = "ready"

    # player
    playerX = 370
    playerY = 480
    playerX_change = 0

    # player 2
    player2X = 430
    player2Y = 480
    player2X_change = 0

    #reset Boss
    boss1health = 4
    boss1X = random.randint(0, 735)
    boss1Y = random.randint(50, 150)
    boss1Exists = True

    #reset Boss2
    boss2health = 5
    boss2X = random.randint(0, 735)
    boss2Y = random.randint(50, 150)
    boss2Exists = True

    #reset Boss3
    boss3health = 10
    boss3X = random.randint(0, 735)
    boss3Y = random.randint(50, 150)
    boss3Exists = True

    # Variable for score
    score_value = 0

    textX = 10
    textY = 10

    # Variable for level
    level_value = 1
    level_type = "Level: "
    level_textX = 650
    level_textY = 10

    #game over state
    game_Over = False

    for i in range(num_of_enemies):
        enemyX[i] = random.randint(0, 735)
        enemyY[i] = random.randint(50, 150)

    for i in range(num_of_enemies2):
        enemy2_health[i] = 2
        enemy2X[i] = random.randint(0, 735)
        enemy2Y[i] = random.randint(50, 150)
    
    for i in range(num_of_enemies3):
        enemy3_health[i] = 3
        enemy3X[i] = random.randint(0, 735)
        enemy3Y[i] = random.randint(50, 150)

    for i in range(num_of_enemies4):
        enemy4_health[i] = 4
        enemy4X[i] = random.randint(0, 735)
        enemy4Y[i] = random.randint(50, 150)

    for i in range(num_of_enemies5):
        enemy5_health[i] = 5
        enemy5X[i] = random.randint(0, 735)
        enemy5Y[i] = random.randint(50, 150)

    for i in range(num_of_enemies6):
        enemy6_health[i] = 6
        enemy6X[i] = random.randint(0, 735)
        enemy6Y[i] = random.randint(50, 150)

    for i in range(num_of_enemies7):
        enemy7_health[i] = 7
        enemy7X[i] = random.randint(0, 735)
        enemy7Y[i] = random.randint(50, 150)
        


    

# Game Loop
running = True
while running:

    #Set screen color
        #RGB - Red, Green, Blue
    screen.fill((0,0,0))

    # Background image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5 #ship speed
            if event.key == pygame.K_RIGHT:
                playerX_change = 5 #ship speed
            if event.key == pygame.K_UP:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    #get the current x coordinate of spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_w:
                if bullet2_state == "ready":
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    #get the current x coordinate of spaceship
                    bullet2X = player2X
                    fire_bullet2(bullet2X, bullet2Y)
            if event.key == pygame.K_a:
                player2X_change = -5 #player2 speed
            if event.key == pygame.K_d:
                player2X_change = 5 #player2 speed
            if game_Over:
                if event.key == pygame.K_r:
                    restart_Game()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0 
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player2X_change = 0

    #Updates player location(movement)
    playerX += playerX_change
    player2X += player2X_change
    #Checking boundaries of spaceship so that it does not go out of bounds
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    #Checking boundaries for player2
    if player2X <= 0:
        player2X = 0
    elif player2X >= 736:
        player2X = 736

    for i in range(num_of_enemies):
        # Game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            for j in range(num_of_enemies2):
                enemy2Y[j] = 2000
            for j in range(num_of_enemies3):
                enemy3Y[j] = 2000
            for j in range(num_of_enemies4):
                enemy4Y[j] = 2000
            for j in range(num_of_enemies5):
                enemy5Y[j] = 2000
            for j in range(num_of_enemies6):
                enemy6Y[j] = 2000
            for j in range(num_of_enemies7):
                enemy7Y[j] = 2000
            boss1Y = 2000
            boss2Y = 2000
            boss3Y = 2000
            game_over_text()
            game_Over = True
            break
        #Updates enemy location(movement)
        enemyX[i] += enemyX_change[i]
        #Checking boundaries of enemy so that it does not go out of bounds
        if enemyX[i] <= 0:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = 4
        elif enemyX[i] >= 736:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -4
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        # Collision2 
        collision2 = isCollision(enemyX[i], enemyY[i], bullet2X, bullet2Y)
        if collision2:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bullet2Y = 480
            bullet2_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
    
    #Keeping track of enemy2
    if score_value > 29:
        level_value = 2
        level_type = "Level: "
        level_textX = 650
        level_textY = 10
        for i in range(num_of_enemies2):
            # Game over
            if enemy2Y[i] > 440:
                for j in range(num_of_enemies2):
                    enemy2Y[j] = 2000
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                for j in range(num_of_enemies3):
                    enemy3Y[j] = 2000
                for j in range(num_of_enemies4):
                    enemy4Y[j] = 2000
                for j in range(num_of_enemies5):
                    enemy5Y[j] = 2000
                for j in range(num_of_enemies6):
                    enemy6Y[j] = 2000
                for j in range(num_of_enemies7):
                    enemy7Y[j] = 2000
                boss1Y = 2000
                boss2Y = 2000
                boss3Y = 2000
                game_over_text()
                game_Over = True
                break
            #Updates enemy location(movement)
            enemy2X[i] += enemy2X_change[i]
            #Checking boundaries of enemy so that it does not go out of bounds
            if enemy2X[i] <= 0:
                enemy2Y[i] += enemy2Y_change[i]
                enemy2X_change[i] = 4
            elif enemy2X[i] >= 736:
                enemy2Y[i] += enemy2Y_change[i]
                enemy2X_change[i] = -4
            # Collision
            collision5 = isCollision(enemy2X[i], enemy2Y[i], bulletX, bulletY)
            if collision5:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemy2_health[i] -= 1
                if enemy2_health[i] < 1:
                    enemy2_health[i] = 2
                    enemy2X[i] = random.randint(0, 735)
                    enemy2Y[i] = random.randint(50, 150)
            # Collision2 
            collision4 = isCollision(enemy2X[i], enemy2Y[i], bullet2X, bullet2Y)
            if collision4:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bullet2Y = 480
                bullet2_state = "ready"
                score_value += 1
                enemy2_health[i] -= 1
                if enemy2_health[i] < 1:
                    enemy2_health[i] = 2
                    enemy2X[i] = random.randint(0, 735)
                    enemy2Y[i] = random.randint(50, 150)
            enemy2(enemy2X[i], enemy2Y[i], i)

    #Keeping track of enemy3
    if score_value > 59:
        level_value = 3
        level_type = "Level: "
        level_textX = 650
        level_textY = 10
        for i in range(num_of_enemies3):
            # Game over
            if enemy3Y[i] > 440:
                for j in range(num_of_enemies3):
                    enemy3Y[j] = 2000
                for j in range(num_of_enemies2):
                    enemy2Y[j] = 2000
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                for j in range(num_of_enemies4):
                    enemy4Y[j] = 2000
                for j in range(num_of_enemies5):
                    enemy5Y[j] = 2000
                for j in range(num_of_enemies6):
                    enemy6Y[j] = 2000
                for j in range(num_of_enemies7):
                    enemy7Y[j] = 2000
                boss1Y = 2000
                boss2Y = 2000
                boss3Y = 2000
                game_over_text()
                game_Over = True
                break
            #Updates enemy location(movement)
            enemy3X[i] += enemy3X_change[i]
            #Checking boundaries of enemy so that it does not go out of bounds
            if enemy3X[i] <= 0:
                enemy3Y[i] += enemy3Y_change[i]
                enemy3X_change[i] = 2
            elif enemy3X[i] >= 736:
                enemy3Y[i] += enemy3Y_change[i]
                enemy3X_change[i] = -2
            # Collision
            collision6 = isCollision(enemy3X[i], enemy3Y[i], bulletX, bulletY)
            if collision6:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemy3_health[i] -= 1
                if enemy3_health[i] < 1:
                    enemy3_health[i] = 3
                    enemy3X[i] = random.randint(0, 735)
                    enemy3Y[i] = random.randint(50, 150)
            # Collision2 
            collision7 = isCollision(enemy3X[i], enemy3Y[i], bullet2X, bullet2Y)
            if collision7:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bullet2Y = 480
                bullet2_state = "ready"
                score_value += 1
                enemy3_health[i] -= 1
                if enemy3_health[i] < 1:
                    enemy3_health[i] = 3
                    enemy3X[i] = random.randint(0, 735)
                    enemy3Y[i] = random.randint(50, 150)
            enemy3(enemy3X[i], enemy3Y[i], i)

    #Keeping track of enemy4
    if score_value > 99:
        level_type = "Level: "
        level_value = 4
        level_textX = 650
        level_textY = 10
        for i in range(num_of_enemies4):
            # Game over
            if enemy4Y[i] > 440:
                for j in range(num_of_enemies4):
                    enemy4Y[j] = 2000
                for j in range(num_of_enemies3):
                    enemy3Y[j] = 2000
                for j in range(num_of_enemies2):
                    enemy2Y[j] = 2000
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                for j in range(num_of_enemies5):
                    enemy5Y[j] = 2000
                for j in range(num_of_enemies6):
                    enemy6Y[j] = 2000
                for j in range(num_of_enemies7):
                    enemy7Y[j] = 2000
                boss1Y = 2000
                boss2Y = 2000
                boss3Y = 2000
                game_over_text()
                game_Over = True
                break
            #Updates enemy location(movement)
            enemy4X[i] += enemy4X_change[i]
            #Checking boundaries of enemy so that it does not go out of bounds
            if enemy4X[i] <= 0:
                enemy4Y[i] += enemy4Y_change[i]
                enemy4X_change[i] = 2
            elif enemy4X[i] >= 736:
                enemy4Y[i] += enemy4Y_change[i]
                enemy4X_change[i] = -2
            # Collision
            collision8 = isCollision(enemy4X[i], enemy4Y[i], bulletX, bulletY)
            if collision8:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemy4_health[i] -= 1
                if enemy4_health[i] < 1:
                    enemy4_health[i] = 4
                    enemy4X[i] = random.randint(0, 735)
                    enemy4Y[i] = random.randint(50, 150)
            # Collision2 
            collision9 = isCollision(enemy4X[i], enemy4Y[i], bullet2X, bullet2Y)
            if collision9:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bullet2Y = 480
                bullet2_state = "ready"
                score_value += 1
                enemy4_health[i] -= 1
                if enemy4_health[i] < 1:
                    enemy4_health[i] = 4
                    enemy4X[i] = random.randint(0, 735)
                    enemy4Y[i] = random.randint(50, 150)
            enemy4(enemy4X[i], enemy4Y[i], i)

    #Keeping track of enemy5
    if score_value > 170:
        level_type = "Level: "
        level_value = 5
        level_textX = 650
        level_textY = 10
        for i in range(num_of_enemies5):
            # Game over
            if enemy5Y[i] > 440:
                for j in range(num_of_enemies4):
                    enemy4Y[j] = 2000
                for j in range(num_of_enemies3):
                    enemy3Y[j] = 2000
                for j in range(num_of_enemies2):
                    enemy2Y[j] = 2000
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                for j in range(num_of_enemies5):
                    enemy5Y[j] = 2000
                for j in range(num_of_enemies6):
                    enemy6Y[j] = 2000
                for j in range(num_of_enemies7):
                    enemy7Y[j] = 2000
                boss1Y = 2000
                boss2Y = 2000
                boss3Y = 2000
                game_over_text()
                game_Over = True
                break
            #Updates enemy location(movement)
            enemy5X[i] += enemy5X_change[i]
            #Checking boundaries of enemy so that it does not go out of bounds
            if enemy5X[i] <= 0:
                enemy5Y[i] += enemy5Y_change[i]
                enemy5X_change[i] = 2
            elif enemy5X[i] >= 736:
                enemy5Y[i] += enemy5Y_change[i]
                enemy5X_change[i] = -2
            # Collision
            collision12 = isCollision(enemy5X[i], enemy5Y[i], bulletX, bulletY)
            if collision12:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemy5_health[i] -= 1
                if enemy5_health[i] < 1:
                    enemy5_health[i] = 5
                    enemy5X[i] = random.randint(0, 735)
                    enemy5Y[i] = random.randint(50, 150)
            # Collision2 
            collision13 = isCollision(enemy5X[i], enemy5Y[i], bullet2X, bullet2Y)
            if collision13:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bullet2Y = 480
                bullet2_state = "ready"
                score_value += 1
                enemy5_health[i] -= 1
                if enemy5_health[i] < 1:
                    enemy5_health[i] = 5
                    enemy5X[i] = random.randint(0, 735)
                    enemy5Y[i] = random.randint(50, 150)
            enemy5(enemy5X[i], enemy5Y[i], i)

    #Keeping track of enemy6
    if score_value > 210:
        level_type = "Level: "
        level_value = 6
        level_textX = 650
        level_textY = 10
        for i in range(num_of_enemies6):
            # Game over
            if enemy6Y[i] > 440:
                for j in range(num_of_enemies4):
                    enemy4Y[j] = 2000
                for j in range(num_of_enemies3):
                    enemy3Y[j] = 2000
                for j in range(num_of_enemies2):
                    enemy2Y[j] = 2000
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                for j in range(num_of_enemies5):
                    enemy5Y[j] = 2000
                for j in range(num_of_enemies6):
                    enemy6Y[j] = 2000
                for j in range(num_of_enemies7):
                    enemy7Y[j] = 2000
                boss1Y = 2000
                boss2Y = 2000
                boss3Y = 2000
                game_over_text()
                game_Over = True
                break
            #Updates enemy location(movement)
            enemy6X[i] += enemy6X_change[i]
            #Checking boundaries of enemy so that it does not go out of bounds
            if enemy6X[i] <= 0:
                enemy6Y[i] += enemy6Y_change[i]
                enemy6X_change[i] = 2
            elif enemy6X[i] >= 736:
                enemy6Y[i] += enemy6Y_change[i]
                enemy6X_change[i] = -2
            # Collision
            collision14 = isCollision(enemy6X[i], enemy6Y[i], bulletX, bulletY)
            if collision14:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemy6_health[i] -= 1
                if enemy6_health[i] < 1:
                    enemy6_health[i] = 6
                    enemy6X[i] = random.randint(0, 735)
                    enemy6Y[i] = random.randint(50, 150)
            # Collision2 
            collision15 = isCollision(enemy6X[i], enemy6Y[i], bullet2X, bullet2Y)
            if collision15:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bullet2Y = 480
                bullet2_state = "ready"
                score_value += 1
                enemy6_health[i] -= 1
                if enemy6_health[i] < 1:
                    enemy6_health[i] = 6
                    enemy6X[i] = random.randint(0, 735)
                    enemy6Y[i] = random.randint(50, 150)
            enemy6(enemy6X[i], enemy6Y[i], i)

    #Keeping track of enemy7
    if score_value > 270:
        level_type = "Level: "
        level_value = 7
        level_textX = 650
        level_textY = 10
        for i in range(num_of_enemies7):
            # Game over
            if enemy7Y[i] > 440:
                for j in range(num_of_enemies4):
                    enemy4Y[j] = 2000
                for j in range(num_of_enemies3):
                    enemy3Y[j] = 2000
                for j in range(num_of_enemies2):
                    enemy2Y[j] = 2000
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                for j in range(num_of_enemies5):
                    enemy5Y[j] = 2000
                for j in range(num_of_enemies6):
                    enemy6Y[j] = 2000
                for j in range(num_of_enemies7):
                    enemy7Y[j] = 2000
                boss1Y = 2000
                boss2Y = 2000
                boss3Y = 2000
                game_over_text()
                game_Over = True
                break
            #Updates enemy location(movement)
            enemy7X[i] += enemy7X_change[i]
            #Checking boundaries of enemy so that it does not go out of bounds
            if enemy7X[i] <= 0:
                enemy7Y[i] += enemy7Y_change[i]
                enemy7X_change[i] = 3
            elif enemy7X[i] >= 736:
                enemy7Y[i] += enemy7Y_change[i]
                enemy7X_change[i] = -3
            # Collision
            collision16 = isCollision(enemy7X[i], enemy7Y[i], bulletX, bulletY)
            if collision16:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemy7_health[i] -= 1
                if enemy7_health[i] < 1:
                    enemy7_health[i] = 7
                    enemy7X[i] = random.randint(0, 735)
                    enemy7Y[i] = random.randint(50, 150)
            # Collision2 
            collision17 = isCollision(enemy7X[i], enemy7Y[i], bullet2X, bullet2Y)
            if collision17:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.play()
                bullet2Y = 480
                bullet2_state = "ready"
                score_value += 1
                enemy7_health[i] -= 1
                if enemy7_health[i] < 1:
                    enemy7_health[i] = 7
                    enemy7X[i] = random.randint(0, 735)
                    enemy7Y[i] = random.randint(50, 150)
            enemy7(enemy7X[i], enemy7Y[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Bullet2 movement
    if bullet2Y <= 0:
        bullet2Y = 480
        bullet2_state = "ready"

    if bullet2_state == "fire":
        fire_bullet2(bullet2X, bullet2Y)
        bullet2Y -= bullet2Y_change

    #BossLevel1 
    if score_value >= 30:
        if boss1Exists == True:
            level_type = "Boss Level: "
            level_value = 1
            level_textX = 560
            level_textY = 10
            if boss1health > 0:
                
                # Game over
                if boss1Y > 440:
                    boss1Y = 2000
                    for j in range(num_of_enemies):
                        enemyY[j] = 2000
                    for j in range(num_of_enemies2):
                        enemy2Y[j] = 2000
                    for j in range(num_of_enemies3):
                        enemy3Y[j] = 2000
                    for j in range(num_of_enemies4):
                        enemy4Y[j] = 2000
                    for j in range(num_of_enemies5):
                        enemy5Y[j] = 2000
                    for j in range(num_of_enemies6):
                        enemy6Y[j] = 2000
                    for j in range(num_of_enemies7):
                        enemy7Y[j] = 2000
                    game_over_text()
                    game_Over = True
                
                #Updates enemy location(movement)
                boss1X += boss1X_change

                #Checking boundaries of enemy so that it does not go out of bounds
                if boss1X <= 0:
                    boss1Y += boss1Y_change
                    boss1X_change = 4
                elif boss1X >= 736:
                    boss1Y += boss1Y_change
                    boss1X_change = -4

                #Boss Collision
                collision3 = isCollision(boss1X, boss1Y, bulletX, bulletY)
                collision4 = isCollision(boss1X, boss1Y, bullet2X, bullet2Y)

                if collision3:
                    explosion_Sound = mixer.Sound('explosion.wav')
                    explosion_Sound.play()
                    bulletY = 480
                    bullet_state = "ready"
                    score_value += 1
                    boss1health -= 1
                    if boss1health < 1:
                        boss1health = 4
                        boss1Exists = False

                if collision4:
                    explosion_Sound = mixer.Sound('explosion.wav')
                    explosion_Sound.play()
                    bullet2Y = 480
                    bullet2_state = "ready"
                    score_value += 1
                    boss1health -= 1
                    if boss1health < 1:
                        boss1health = 4
                        boss1Exists = False
                boss1(boss1X, boss1Y)

    #BossLevel2 
    if score_value >= 130:
        if boss2Exists == True:
            level_type = "Boss Level: "
            level_value = 2
            level_textX = 560
            level_textY = 10
            if boss2health > 0:
                
                # Game over
                if boss2Y > 440:
                    boss2Y = 2000
                    boss1Y = 2000
                    for j in range(num_of_enemies):
                        enemyY[j] = 2000
                    for j in range(num_of_enemies2):
                        enemy2Y[j] = 2000
                    for j in range(num_of_enemies3):
                        enemy3Y[j] = 2000
                    for j in range(num_of_enemies4):
                        enemy4Y[j] = 2000
                    for j in range(num_of_enemies5):
                        enemy5Y[j] = 2000
                    for j in range(num_of_enemies6):
                        enemy6Y[j] = 2000
                    for j in range(num_of_enemies7):
                        enemy7Y[j] = 2000
                    game_over_text()
                    game_Over = True
                
                #Updates enemy location(movement)
                boss2X += boss2X_change

                #Checking boundaries of enemy so that it does not go out of bounds
                if boss2X <= 0:
                    boss2Y += boss2Y_change
                    boss2X_change = 2
                elif boss2X >= 736:
                    boss2Y += boss2Y_change
                    boss2X_change = -2

                #Boss Collision
                collision10 = isCollision(boss2X, boss2Y, bulletX, bulletY)
                collision11 = isCollision(boss2X, boss2Y, bullet2X, bullet2Y)

                if collision10:
                    explosion_Sound = mixer.Sound('explosion.wav')
                    explosion_Sound.play()
                    bulletY = 480
                    bullet_state = "ready"
                    score_value += 1
                    boss2health -= 1
                    if boss2health < 1:
                        boss2health = 5
                        boss2Exists = False

                if collision11:
                    explosion_Sound = mixer.Sound('explosion.wav')
                    explosion_Sound.play()
                    bullet2Y = 480
                    bullet2_state = "ready"
                    score_value += 1
                    boss2health -= 1
                    if boss2health < 1:
                        boss2health = 5
                        boss2Exists = False
                boss2(boss2X, boss2Y)

    #BossLevel3
    if score_value >= 350:
        if boss3Exists == True:
            level_type = "Boss Level: "
            level_value = 3
            level_textX = 560
            level_textY = 10
            if boss3health > 0:
                
                # Game over
                if boss3Y > 440:
                    boss3Y = 2000  
                    boss2Y = 2000
                    boss1Y = 2000
                    for j in range(num_of_enemies):
                        enemyY[j] = 2000
                    for j in range(num_of_enemies2):
                        enemy2Y[j] = 2000
                    for j in range(num_of_enemies3):
                        enemy3Y[j] = 2000
                    for j in range(num_of_enemies4):
                        enemy4Y[j] = 2000
                    for j in range(num_of_enemies5):
                        enemy5Y[j] = 2000
                    for j in range(num_of_enemies6):
                        enemy6Y[j] = 2000
                    for j in range(num_of_enemies7):
                        enemy7Y[j] = 2000
                    game_over_text()
                    game_Over = True
                
                #Updates enemy location(movement)
                boss3X += boss3X_change

                #Checking boundaries of enemy so that it does not go out of bounds
                if boss3X <= 0:
                    boss3Y += boss3Y_change
                    boss3X_change = 2
                elif boss3X >= 736:
                    boss3Y += boss3Y_change
                    boss3X_change = -2

                #Boss Collision
                collision18 = isCollision(boss3X, boss3Y, bulletX, bulletY)
                collision19 = isCollision(boss3X, boss3Y, bullet2X, bullet2Y)

                if collision18:
                    explosion_Sound = mixer.Sound('explosion.wav')
                    explosion_Sound.play()
                    bulletY = 480
                    bullet_state = "ready"
                    score_value += 1
                    boss3health -= 1
                    if boss3health < 1:
                        boss3health = 10
                        boss3Exists = False

                if collision19:
                    explosion_Sound = mixer.Sound('explosion.wav')
                    explosion_Sound.play()
                    bullet2Y = 480
                    bullet2_state = "ready"
                    score_value += 1
                    boss3health -= 1
                    if boss3health < 1:
                        boss3health = 10
                        boss3Exists = False
                boss3(boss3X, boss3Y)
        

    
    player(playerX, playerY)
    player2(player2X, player2Y)
    show_score(textX, textY)
    show_level(level_textX, level_textY)
    pygame.display.update()
