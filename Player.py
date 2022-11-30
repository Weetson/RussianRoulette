import pygame
import config

class Player(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 0))

    def update(self):
        if self.rect.y < config.SCREEN_SHAPE['HEIGHT']:
            self.rect.y += config.PLAYER_SPEED
        else:
            self.rect.y = 0