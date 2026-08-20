# 1) Import the `pygame` library to create a game window and handle events.
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 600))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()
# 4) Create a variable `done = False` to control the main game loop.

# 5) Start the main loop using `while not done`:
#    (This loop keeps the window open until the user quits.)

# 6) Inside the loop, process all events using `pygame.event.get()`:
#    a) Use a `for` loop to check each event in the event queue.
#    b) If the event type is `pygame.QUIT` (user clicks close button):
#       i) Call `pygame.quit()` to close the pygame window and stop pygame.
#       (This exits the game window.)

# 7) Update the display using `pygame.display.flip()`:
#    (This makes all changes visible on the screen after each loop iteration.)
