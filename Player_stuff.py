import pygame, os, sys


STEP = 6
BULLET_VELOCITY = 12


def load_image(name):
    fullname = os.path.join('C:\\Users\\1\\Desktop\\data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


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
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(*coords)
        

    def cut_sheet(self, columns=7, rows=1):
        self.rect = pygame.Rect(0, 0, self.sheet.get_width() // columns, 
                                self.sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(self.sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

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
        if self.rect.y < -100:
            self.kill()
