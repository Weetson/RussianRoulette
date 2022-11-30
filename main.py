import pygame

background_colour = (0, 0, 0)
screen_width_x, screen_width_y = 300, 300
screen = pygame.display.set_mode((screen_width_x, screen_width_y))
pygame.display.set_caption('RussianRoulette')
screen.fill(background_colour)
pygame.display.flip()

# Variable to keep our game loop running
running = True

# game loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
