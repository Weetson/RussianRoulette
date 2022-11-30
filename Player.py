import pygame
import config

class Player(pygame.sprite.Sprite):
    def __init__(self, cords, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=cords)

    def update(self, side):
        if side == 'right':
            self.rect.x += config.PLAYER_SPEED
        elif side == 'left':
            self.rect.x += -config.PLAYER_SPEED
        elif side == 'up':
            self.rect.y += -config.PLAYER_SPEED
        elif side == 'down':
            self.rect.y += config.PLAYER_SPEED

        if self.rect.x == config.SCREEN_SHAPE['WIDTH']:
            self.rect.x = 0