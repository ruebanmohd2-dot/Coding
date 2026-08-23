# 1) Import the required modules:
#    a) Import `pygame` to create the game window and handle sprites/events.
#    b) Import `random` to generate random colors, directions, and positions.


# 2) Initialize pygame using `pygame.init()`.

# 3) Create two custom event IDs using `pygame.USEREVENT`:
#    a) `SPRITE_COLOR_CHANGE_EVENT` for changing the sprite color.
#    b) `BACKGROUND_COLOR_CHANGE_EVENT` for changing the background color.

# 4) Define color constants using `pygame.Color()`:
#    a) Background colors: BLUE, LIGHTBLUE, DARKBLUE
#    b) Sprite colors: YELLOW, MAGENTA, ORANGE, WHITE

# 5) Create a `Sprite` class that inherits from `pygame.sprite.Sprite`.

# 6) Define the constructor `__init__(self, color, height, width)` for the Sprite:
#    a) Call the parent constructor using `super().__init__()`.
#    b) Create a surface for the sprite using `pygame.Surface([width, height])`.
#    c) Fill the sprite surface with the given `color`.
#    d) Create a rectangle (`self.rect`) for positioning using `self.image.get_rect()`.
#    e) Set an initial velocity with random direction in x and y:
#       `self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]`.

# 7) Define an `update(self)` method to move the sprite and detect boundary hits:
#    a) Move the sprite by its velocity using `self.rect.move_ip(self.velocity)`.
#    b) Set `boundary_hit = False` to track collisions.
#    c) If the sprite touches left/right edges (0 or 500):
#       - reverse x direction (`self.velocity[0] = -self.velocity[0]`)
#       - set `boundary_hit = True`
#    d) If the sprite touches top/bottom edges (0 or 400):
#       - reverse y direction (`self.velocity[1] = -self.velocity[1]`)
#       - set `boundary_hit = True`
#    e) If `boundary_hit` is True, post two events:
#       - `SPRITE_COLOR_CHANGE_EVENT`
#       - `BACKGROUND_COLOR_CHANGE_EVENT`

# 8) Define a method `change_color(self)` in Sprite:
#    a) Fill the sprite surface with a random choice of sprite colors
#       (YELLOW, MAGENTA, ORANGE, WHITE).

# 9) Define a function `change_background_color()`:
#    a) Use `global bg_color` so the background color can be updated.
#    b) Set `bg_color` to a random choice of (BLUE, LIGHTBLUE, DARKBLUE).

# 10) Create a sprite group `all_sprites_list = pygame.sprite.Group()`
#     to store and manage sprites.

# 11) Create one sprite object `sp1 = Sprite(WHITE, 20, 30)`.

# 12) Set the sprite’s starting position randomly:
#     a) `sp1.rect.x` between 0 and 480
#     b) `sp1.rect.y` between 0 and 370

# 13) Add the sprite to the group using `all_sprites_list.add(sp1)`.

# 14) Create the game window (screen) of size 500x400 and set the title.

# 15) Set the initial background color `bg_color = BLUE`
#     and fill the screen once with this color.

# 16) Create a loop control variable `exit = False`
#     and create a `clock` object to control the FPS.

# 17) Start the main game loop `while not exit`:

# 18) Inside the loop, handle events:
#     a) If `pygame.QUIT` occurs, set `exit = True`.
#     b) If `SPRITE_COLOR_CHANGE_EVENT` occurs, call `sp1.change_color()`.
#     c) If `BACKGROUND_COLOR_CHANGE_EVENT` occurs, call `change_background_color()`.

# 19) Update all sprites using `all_sprites_list.update()`.

# 20) Redraw the screen each frame:
#     a) Fill the screen with the current `bg_color`.
#     b) Draw all sprites using `all_sprites_list.draw(screen)`.

# 21) Update the display using `pygame.display.flip()`.

# 22) Limit the frame rate using `clock.tick(240)`.

# 23) When the loop ends, close pygame using `pygame.quit()`.

import pygame

import random

pygame.init()

# -----------------------------

# Custom events

# -----------------------------

BALL_COLOR_CHANGE = pygame.USEREVENT + 1

BACKGROUND_CHANGE = pygame.USEREVENT + 2

# -----------------------------

# Colors

# -----------------------------

BALL_COLORS = [

    pygame.Color("red"),

    pygame.Color("yellow"),

    pygame.Color("green"),

    pygame.Color("magenta"),

    pygame.Color("cyan")

]

BACKGROUND_COLORS = [

    pygame.Color("black"),

    pygame.Color("darkblue"),

    pygame.Color("darkgreen"),

    pygame.Color("purple")]


class Ball(pygame.sprite.Sprite):

    def __init__(self, ):
        super().__init__()

        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)

        pygame.draw.circle(self.image, pygame.Color("white"), (20, 20), 20)

        self.rect = self.image.get_rect()
        self.rect.center = (250, 200)

        self.velocity = [random.choice([-3, 3]), random.choice([-3, 3])]

    def update(self):
        self.rect.move_ip(self.velocity)

        hitwall = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] *= -1
            hitwall = True

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] *= -1
            hitwall = True

        if hitwall:
            pygame.event.post(pygame.event.Event(BALL_COLOR_CHANGE))
            pygame.event.post(pygame.event.Event(BACKGROUND_CHANGE))

    def colorchange(self):
        color = random.choice(BALL_COLORS)
        self.image.fill((0, 0, 0, 0))

        pygame.draw.circle(self.image, color, (20, 20), 20)


backgroundcolor = pygame.Color("black")


def change_background():
    global backgroundcolor
    backgroundcolor = random.choice(BACKGROUND_COLORS)


ball = Ball()
ball1 = Ball()
ball2 = Ball()
ball3 = Ball()
ball.rect.center = (random.randint(50, 400), random.randint(50, 400))
ball1.rect.center = (random.randint(50, 400), random.randint(50, 400))
ball2.rect.center = (random.randint(50, 400), random.randint(50, 400))
ball3.rect.center = (random.randint(50, 400), random.randint(50, 400))
allsprites = pygame.sprite.Group()
allsprites.add(ball)
allsprites.add(ball1)
allsprites.add(ball2)
allsprites.add(ball3)


screen = pygame.display.set_mode((500, 400))

pygame.display.set_caption("Event Driven Ball")

clock = pygame.time.Clock()

running = True
while running:

    # 1. EVENTS

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == BALL_COLOR_CHANGE:

            ball.colorchange()
            ball1.colorchange()
            ball2.colorchange()
            ball3.colorchange()

        elif event.type == BACKGROUND_CHANGE:

            change_background()

# 2. UPDATE
    allsprites.update()

# 3. DRAW

    screen.fill(backgroundcolor)

    allsprites.draw(screen)

# 4. DISPLAY

    pygame.display.flip()

# 5. FPS

    clock.tick(120)

pygame.quit()
