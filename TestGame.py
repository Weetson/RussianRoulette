import pygame
import Player
import Server
import config
import math
import Valera

import pretty_errors

screen = pygame.display.set_mode((config.SCREEN_SHAPE['WIDTH'], config.SCREEN_SHAPE['HEIGHT']))

pygame.display.set_caption('Test')
screen.fill(config.COLORS['WHITE'])
pygame.display.flip()

valera = Valera.Valera(cords = config.SCREEN_CENTER, filename = 'img/Valera.png')
players = []

def player_cords(x, y):
    """ Counting players positions """
    return (x + math.sin((step * i) * (math.pi / (config.CIRCLE / 2))) * config.PADDING, y - math.cos((step * i) * (math.pi / (config.CIRCLE / 2))) * config.PADDING)

angle = 0
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                players.append(Player.Player(cords = config.SCREEN_CENTER, filename = 'img/icon.png'))
            if event.key == pygame.K_k:
                players[3].killed('img/icon-dead.png')
            if event.key == pygame.K_RIGHT:
                players.remove(players[-1])
            if event.key == pygame.K_SPACE:
                valera.random_person(len(players), step)

    '''keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        valera.random_person(len(players), step)'''

    screen.fill(config.COLORS['WHITE'])

    if len(players) == 0:
        pass
    else:
        step = config.CIRCLE // len(players)
        for i in range(len(players)):
            screen.blit(players[i].image, player_cords(players[i].rect.x, players[i].rect.y))

    
    screen.blit(valera.image, valera.rect)
    pygame.display.update()
    pygame.time.delay(20)