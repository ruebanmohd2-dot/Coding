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

    x, y = 60, 0

    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False

    dx = 3
    dy = 3

    while not done:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                done = True
        x = dx+x
        y = dy+y
        if x <= 0 or x+sprite_width >= screen_width:
            dx = -dx
        if y <= 0 or y+sprite_height >= screen_height:
            dy = -dy
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
        clock.tick(60)

    pygame.quit()


main()
