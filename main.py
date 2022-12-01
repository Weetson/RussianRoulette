import pygame
import Player
import Server
import config

import pretty_errors

screen = pygame.display.set_mode((config.SCREEN_SHAPE['WIDTH'], config.SCREEN_SHAPE['HEIGHT']))

pygame.display.set_caption('Test')
screen.fill(config.COLORS['WHITE'])
pygame.display.flip()

server = Server.Server()
server.connect(host = 'localhost', port = 8080)
player = Player.Player(cords = (config.SCREEN_SHAPE['WIDTH'] // 2, config.SCREEN_SHAPE['HEIGHT'] // 2), filename = 'img/Valera.png')

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        server.connect_send_data('right')            
    if keys[pygame.K_LEFT]:
        server.connect_send_data('left')
    if keys[pygame.K_UP]:
        server.connect_send_data('up')
    if keys[pygame.K_DOWN]:
        server.connect_send_data('down')

    screen.fill(config.COLORS['WHITE'])
    screen.blit(player.image, player.rect)
    pygame.display.update()
    pygame.time.delay(20)
 
    player.update(server.connect_get_data())