import pygame, os, sys
import shapely
from shapely.geometry.point import Point
from shapely.geometry import Polygon


STEP = 6
BULLET_VELOCITY = 12
BULLET_DAMAGE = 5


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


class Null_thingy(pygame.sprite.Sprite):
    def __init__(self, coords, groups):
        super().__init__(*groups)
        self.image = pygame.Surface((60, 80))
        self.rect = self.image.get_rect().move(*coords)


class Player(pygame.sprite.Sprite):
    def __init__(self, coords, groups):
        super().__init__(*groups)
        #self.image = load_image('ship.png')
        #self.image = pygame.transform.scale(self.image, (60, 80))
        #self.rect = self.image.get_rect().move(*coords)
        self.frames = []
        self.sheet = load_image('ship_animated.png')
        self.cut_sheet()
        self.cur_frame = 0
        self.dead = False
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect().move(*coords)
        self.hitbox = Polygon([(coords[0] + 26, coords[1] + 56),
                               (coords[0] + 26 + 8, coords[1] + 56),
                               (coords[0] + 26 + 8, coords[1] + 56 + 10),
                               (coords[0] + 26, coords[1] + 56 + 10)])
        

    def cut_sheet(self, columns=7, rows=1):
        self.rect = pygame.Rect(0, 0, self.sheet.get_width() // columns, 
                                self.sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(self.sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, *enemy_bullet_group):
        if enemy_bullet_group:
            for bullet in enemy_bullet_group[0]:
                if self.hitbox.intersects(bullet.hitbox):
                    self.dead = True
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.hitbox = Polygon([(self.rect.x + 26, self.rect.y + 56),
                               (self.rect.x + 26 + 8, self.rect.y + 56),
                               (self.rect.x + 26 + 8, self.rect.y + 56 + 10),
                               (self.rect.x + 26, self.rect.y + 56 + 10)])

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
        self.hitbox = Polygon([(self.rect.x, self.rect.y),
                               (self.rect.x + 2, self.rect.y),
                               (self.rect.x + 2, self.rect.y + 4),
                               (self.rect.x, self.rect.y + 4)])
        self.damage = BULLET_DAMAGE

    def update(self):
        self.rect.y -= BULLET_VELOCITY
        self.hitbox = Polygon([(self.rect.x, self.rect.y),
                               (self.rect.x + 2, self.rect.y),
                               (self.rect.x + 2, self.rect.y + 4),
                               (self.rect.x, self.rect.y + 4)])
        if self.rect.y < -100:
            self.kill()
