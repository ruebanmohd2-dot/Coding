# 1) Import the `pygame` library to create a window and draw shapes.
import pygame
# 2) Initialize pygame using `pygame.init()`.
pygame.init()
window = pygame.display.set_mode((400, 400))
window.fill((255, 255, 255))
green = (0, 225, 0)
pygame.draw.circle(window, green, (300, 300), 50)
pygame.draw.circle(window, green, (100, 100), 50, 3)
pygame.display.update()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()

# 6) Draw a solid (filled) circle on the window:
#    a) Use `pygame.draw.circle(window, GREEN, (300, 300), 50)`
#    b) Center is at (300, 300) and radius is 50.

# 7) Draw an outlined circle on the window:
#    a) Use `pygame.draw.circle(window, GREEN, (100, 100), 50, 3)`
#    b) The last value `3` is the thickness of the circle border.

# 8) Update the screen to show drawings using `pygame.display.update()`.

# 9) Start the game loop with `running = True` to keep the window open.

# 10) Inside the loop, handle events:
#     a) Use `pygame.event.get()` to read events.
#     b) If the user clicks the close button (`pygame.QUIT`), set `running = False`.

# 11) After the loop ends, close pygame using `pygame.quit()`.
