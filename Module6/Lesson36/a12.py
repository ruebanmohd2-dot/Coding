import pygame
import random

screenheight = 700  # height
screenwidth = 1100  # width
fontsize = 36
speed = 5
done = False

pygame.init()
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Collision Game")
backgroundimage = pygame.transform.scale(pygame.image.load(
    'Module6\\Lesson36\\bg.png'), (screenwidth, screenheight))


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, r):
        super().__init__()

        self.image = pygame.Surface((2*r, 2*r), pygame.SRCALPHA)

        pygame.draw.circle(self.image, color, (r, r), r)

        self.rect = self.image.get_rect()

    def move(self, xchange, ychange):

        self.rect.x += xchange
        self.rect.y += ychange
        self.rect.left = max(0, self.rect.left)
        self.rect.top = max(0, self.rect.top)
        self.rect.right = min(screenwidth, self.rect.right)
        self.rect.bottom = min(screenheight, self.rect.bottom)


ball = Ball(pygame.Color("Red"), 20)
ball1 = Ball(pygame.Color("black"), 20)
ball2 = Ball(pygame.Color("black"), 20)
ball.rect.center = (random.randint(1, 1100), random.randint(1, 700))
ball1.rect.center = (random.randint(1, 1100), random.randint(1, 700))
ball2.rect.center = (random.randint(1, 1100), random.randint(1, 700))
allsprites = pygame.sprite.Group()
allsprites.add(ball)
allsprites.add(ball1)
allsprites.add(ball2)


clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    xchange = pressed[pygame.K_d]-pressed[pygame.K_a]
    ychange = pressed[pygame.K_s]-pressed[pygame.K_w]
    xchange *= speed
    ychange *= speed
    ball.move(xchange, ychange)

    if ball.rect.colliderect(ball1.rect):
        allsprites.remove(ball1)
    if ball.rect.colliderect(ball2.rect):
        allsprites.remove(ball2)
    screen.blit(backgroundimage, (0, 0))
    allsprites.update()
    allsprites.draw(screen)
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
