import pygame
import config

class Player(pygame.sprite.Sprite):
    def __init__(self, cords, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=cords)

    def killed(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()