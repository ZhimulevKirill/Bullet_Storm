import pygame, os, sys


STEP = 6
BULLET_VELOCITY = 15


def load_image(name):
    fullname = os.path.join('C:\\Users\\1\\Desktop\\data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self, coords, groups):
        super().__init__(*groups)
        self.image = load_image('ship.png')
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect().move(*coords)

    def go_left(self):
        self.rect.x -= STEP

    def go_right(self):
        self.rect.x += STEP

    def go_down(self):
        self.rect.y += STEP

    def go_up(self):
        self.rect.y -= STEP


class YourBullet(pygame.sprite.Sprite):
    def __init__(self, coords, groups):
        super().__init__(*groups)
        self.image = load_image('bullet.png')
        self.image = pygame.transform.scale(self.image, (2, 4))
        self.rect = self.image.get_rect().move(*coords)

    def update(self):
        self.rect.y -= BULLET_VELOCITY
