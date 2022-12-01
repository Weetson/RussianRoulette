import pygame
import Player
import Server
import config
import math

import pretty_errors

screen = pygame.display.set_mode((config.SCREEN_SHAPE['WIDTH'], config.SCREEN_SHAPE['HEIGHT']))

pygame.display.set_caption('Test')
screen.fill(config.COLORS['WHITE'])
pygame.display.flip()

players = []

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                players.append(Player.Player(cords = config.SCREEN_CENTER, filename = 'img/icon.png'))      

    screen.fill(config.COLORS['WHITE'])

    if len(players) == 0:
        pass
    else:
        step = 360 // len(players)
        for i in range(len(players)):
            x, y = players[i].rect.x, players[i].rect.y
            x, y = x + math.sin((step * i) * (math.pi / 180)) * 100, y - math.cos((step * i) * (math.pi / 180)) * 100
            screen.blit(players[i].image, (x, y))
            print(x, y, step)

    
    pygame.display.update()
    pygame.time.delay(20)