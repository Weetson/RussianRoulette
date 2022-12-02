import pygame
import Player
import Server
import config
import math
import Valera
import random

import pretty_errors

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_SHAPE['WIDTH'], config.SCREEN_SHAPE['HEIGHT']))

pygame.display.set_caption('Test')
screen.fill(config.COLORS['WHITE'])
pygame.display.flip()

valera = Valera.Valera(cords = config.SCREEN_CENTER, filename = 'img/Valera.png')
players = []
names = ['Vasya', 'Sveta', 'Lyaha', 'Vadim', 'Dimon', 'David', 'Artem', 'Evgeniy', 'Vit', 'Eren', 'Armin', 'Levi', 'Zhak', 'Mikasa', 'Anny', 'Handi', 'Billy', 'Marko', 'Sasha', 'Zik', 'Van', 'Floch']
f1 = pygame.font.Font('fonts/times-new-roman.ttf', 36)

def player_cords(x, y):
    """ Counting players positions """
    return (x + math.sin((step * i) * (math.pi / (config.CIRCLE / 2))) * config.PADDING, y - math.cos((step * i) * (math.pi / (config.CIRCLE / 2))) * config.PADDING)

people_counter = 0
angle = 0
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT: # Adding player 
                player_name = random.choice(names)
                name = f1.render(player_name, 1, (0, 0, 0))
                players.append(Player.Player(cords = config.SCREEN_CENTER, filename = 'img/icon.png', player_name_text = name, player_name = player_name))

            if event.key == pygame.K_r: # Rotating valera
                valera.rotation(-step * (people_counter + 1))
                people_counter += 1
                if people_counter > len(players) - 1:
                    people_counter = 0

            if event.key == pygame.K_s: # Shooting player
                if people_counter == valera.bullet:
                    print(f'killed - {players[people_counter].player_name}')
                    players.remove(players[people_counter])
                    valera.bullet = random.randint(0, len(players))
                    if people_counter > len(players) - 1:
                        people_counter = 0
                else:
                    print(f'not killed - {players[people_counter].player_name}')
                
                print(f'valera - {valera.bullet}, counter - {people_counter}')

            if event.key == pygame.K_RIGHT: # Removing player
                players.remove(players[-1])

            if event.key == pygame.K_SPACE: # Random person in game start
                valera.random_person(len(players), step)
                valera.bullet = random.randint(0, len(players) - 1)

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
            screen.blit(players[i].player_name_text, player_cords(players[i].player_name_cords[0], players[i].player_name_cords[1]))

    
    screen.blit(valera.image, valera.rect)
    pygame.display.update()
    pygame.time.delay(20)