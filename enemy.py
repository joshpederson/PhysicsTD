import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rec = self.image.getRect()
        self.rec.center = pos
