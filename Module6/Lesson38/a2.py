import math
import random
import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

PLAYER_START_X = 370
PLAYER_START_Y = 380

ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150

ENEMY_SPEED_X = 0.1
ENEMY_SPEED_Y = 40

BULLET_SPEED_Y = 0.7
COLLISION_DISTANCE = 27

PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64

ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50

BULLET_WIDTH = 16
BULLET_HEIGHT = 16

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Space Invader")


background = pygame.image.load("Module6\\Lesson37\\b1.jpg").convert()

background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

playerImg = pygame.image.load("Module6\\Lesson37\\Character.png").convert()

playerImg = pygame.transform.scale(playerImg, (PLAYER_WIDTH, PLAYER_HEIGHT))

playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 1

image = pygame.image.load(
    "Module6\\Lesson37\\Enemy sprite.jpg").convert_alpha()

image = pygame.transform.scale(image, (ENEMY_WIDTH, ENEMY_HEIGHT))

enemyImg.append(image)

enemyX.append(random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH))

enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))

enemyX_change.append(ENEMY_SPEED_X)

enemyY_change.append(ENEMY_SPEED_Y)


bulletImg = pygame.image.load("Module6\\Lesson37\\bullets.png").convert_alpha()

bulletImg = pygame.transform.scale(bulletImg, (BULLET_WIDTH, BULLET_HEIGHT))
bulletX = 0
bulletY = PLAYER_START_Y
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

score_value = 0

font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10

textY = 10

over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + PLAYER_WIDTH // 2 -
                BULLET_WIDTH // 2, y - BULLET_HEIGHT))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE


running = True

while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                playerX_change = -0.5

            if event.key == pygame.K_RIGHT:

                playerX_change = 0.5
            if (
                    event.key == pygame.K_SPACE
                    and bullet_state == "ready"):

                bulletX = playerX

                bulletY = playerY

                fire_bullet(bulletX, bulletY)

        if (event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]):

            playerX_change = 0

    playerX += playerX_change

    playerX = max(0, min(playerX, SCREEN_WIDTH - PLAYER_WIDTH))

    for i in range(num_of_enemies):
        if score_value == 1 or score_value > 1:
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if (enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - ENEMY_WIDTH):

            enemyX_change[i] *= -1

            enemyY[i] += enemyY_change[i]

        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
pygame.quit()
