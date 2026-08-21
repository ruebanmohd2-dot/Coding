# 11) Read keyboard inputs using `pygame.key.get_pressed()`:
#     a) If LEFT key is pressed, move sprite left by decreasing `x`.
#     b) If RIGHT key is pressed, move sprite right by increasing `x`.
#     c) If UP key is pressed, move sprite up by decreasing `y`.
#     d) If DOWN key is pressed, move sprite down by increasing `y`.

# 12) Restrict the sprite to stay inside the screen boundaries:
#     a) Clamp `x` between 0 and `screen_width - sprite_width`.
#     b) Clamp `y` between 0 and `screen_height - sprite_height`.

# 13) Change the sprite color based on which boundary it touches:
#     a) If `x == 0`, change to blue (left wall).
#     b) Else if `x == screen_width - sprite_width`, change to yellow (right wall).
#     c) Else if `y == 0`, change to red (top wall).
#     d) Else if `y == screen_height - sprite_height`, change to green (bottom wall).
#     e) Otherwise, keep it white (not touching any boundary).

# 14) Draw everything on the screen:
#     a) Fill the background with black using `screen.fill((0, 0, 0))`.
#     b) Draw the sprite as a rectangle using `pygame.draw.rect(...)`.

# 15) Update the display using `pygame.display.flip()`.

# 16) Limit the frame rate using `clock.tick(90)`.

# 17) After the loop ends, close pygame using `pygame.quit()`.

# 18) Use `if __name__ == "__main__":` to call `main()` only when
#     the file is run directly.
import pygame


def main():

    pygame.init()

    screen_width, screen_height = 500, 500

    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption('color changing sprite')

# Mapping of color names to RGB values

    colors = {

        'red': pygame.Color('red'),

        'green': pygame.Color('green'),

        'blue': pygame.Color('blue'),

        'yellow': pygame.Color('yellow'),

        'white': pygame.Color('white')}

    current_color = colors['white']

    x, y = 30, 30

    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False

    while not done:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                done = True

        pressed = pygame.key.get_pressed()
        if pressed == [pygame.K_d]:
            x -= 5
        if pressed == [pygame.K_a]:
            x += 5
        if pressed == [pygame.K_w]:
            y -= 5
        if pressed == [pygame.K_s]:
            y += 5

        x = min(max(0, x), screen_width-sprite_width)
        y = min(max(0, y), screen_height-sprite_height)

        if x == 0:
            current_color = colors['blue']
        elif x == screen_width-sprite_width:
            colors['yellow']
        elif y == 0:
            current_color = colors['red']
        elif y == screen_height-sprite_height:
            colors['green']

        else:
            current_color = colors['white']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,
                         (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(120)

    pygame.quit()


main()
