import pygame
import random
import config

class Valera(pygame.sprite.Sprite):
    def __init__(self, cords, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=cords)

    def random_person(self, players_amount):
        self.person = random.randint(0, players_amount)

    def rotation(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=config.SCREEN_CENTER)