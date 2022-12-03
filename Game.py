import pygame
import Player, Server, Valera
import config
import math
import data

import pretty_errors

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_SHAPE['WIDTH'], config.SCREEN_SHAPE['HEIGHT']))
server = Server.Server()

players = []
font = pygame.font.Font('fonts/times-new-roman.ttf', 36)

if data.style == "host":
    player_name = data.name
    name = font.render(player_name, 1, (0, 0, 0))
    players.append(Player.Player(cords = config.SCREEN_CENTER, filename = 'img/icon.png', player_name_text = name, player_name = player_name))
    server.host(data.host, data.port)
    is_host = True
else:
    server.connect(data.host, data.port)
    server.connect_send_data(data.name)
    is_host = False

pygame.display.set_caption('Test')
screen.fill(config.COLORS['WHITE'])
pygame.display.flip()

valera = Valera.Valera(cords = config.SCREEN_CENTER, filename = 'img/Valera.png')

def player_cords(x, y):
    """ Counting players positions """
    return (x + math.sin((step * i) * (math.pi / (config.CIRCLE / 2))) * config.PADDING, y - math.cos((step * i) * (math.pi / (config.CIRCLE / 2))) * config.PADDING)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(config.COLORS['WHITE'])

    if is_host:
        if server.host_get_client():
            player_name = server.host_get_data()
            name = font.render(player_name, 1, (0, 0, 0))
            players.append(Player.Player(cords = config.SCREEN_CENTER, filename = 'img/icon.png', player_name_text = name, player_name = player_name))
        
        server.host_send_data(players)

    elif not is_host:
        players = server.connect_get_data()

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