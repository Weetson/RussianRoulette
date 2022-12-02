import pygame
import config

class Player(pygame.sprite.Sprite):
    def __init__(self, cords, filename, player_name_text, player_name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=cords)
        self.player_name_text = player_name_text
        self.player_name_cords = (cords[0] - 40, cords[1] + 30)
        self.is_dead = False
        self.player_name = player_name

    def killed(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()
        self.is_dead = True