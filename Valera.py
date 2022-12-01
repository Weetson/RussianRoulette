import pygame
import random
import config
import time

class Valera(pygame.sprite.Sprite):
    def __init__(self, cords, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image_clean = self.image.copy()
        self.rect = self.image.get_rect(center=cords)

    def random_person(self, players_amount, step):
        self.person = random.randint(0, players_amount)
        print(self.person)
        for i in range(360):
            self.rotation(1)
        self.rotation(self.person * step)

    def rotation(self, angle):
        self.image = pygame.transform.rotate(self.image_clean, angle)
        self.rect = self.image.get_rect(center=config.SCREEN_CENTER)