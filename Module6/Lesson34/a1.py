# 1) Import the `pygame` library to create a window and draw shapes.
import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(30, 30, 120, 90))
    pygame.display.flip()


# 7) Draw a rectangle on the screen using `pygame.draw.rect()`:
#    a) Draw it on `screen`.
#    b) Use the color `(0, 125, 255)` (RGB).
#    c) Use `pygame.Rect(30, 30, 60, 60)` to set the rectangle position and size:
#       - x = 30, y = 30
#       - width = 60, height = 60

# 8) Update the display using `pygame.display.flip()` to show the rectangle
#    and any changes on the window.
