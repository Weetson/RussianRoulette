import pygame
import Player
import Server
import config

screen = pygame.display.set_mode((config.SCREEN_SHAPE['WIDTH'], config.SCREEN_SHAPE['HEIGHT']))

pygame.display.set_caption('Test')
screen.fill(config.COLORS['WHITE'])
pygame.display.flip()

server = Server.Server()
player = Player.Player(x = 250, filename = 'Valera.png')

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(config.COLORS['WHITE'])
    screen.blit(player.image, player.rect)
    pygame.display.update()
    pygame.time.delay(20)
 
    