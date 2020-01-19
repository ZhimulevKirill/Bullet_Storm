import pygame, os, math


BULLET_VEL = 3


def load_image(name):
    fullname = os.path.join('C:\\Users\\1\\Desktop\\data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


class Loading_Sign(pygame.sprite.Sprite):
    def __init__(self, coords, groups):
        super().__init__(*groups)
        self.image = load_image('Bullet_loading.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect().move(*coords)

    def update(self, counter):
        self.rect.x -= BULLET_VEL


class Title(pygame.sprite.Sprite):
    def __init__(self, coords, groups):
        super().__init__(*groups)
        self.image = load_image('Title.png')
        self.image = pygame.transform.scale(self.image, (500, 200))
        self.rect = self.image.get_rect().move(*coords)

    def update(self, counter):
        self.rect.y = 20*math.sin(counter/50) + 50
        

class Start_Button(pygame.sprite.Sprite):
    def __init__(self, coords, groups):
        super().__init__(*groups)
        self.image = load_image('Start_button_letters.png')
        self.image = pygame.transform.scale(self.image, (290, 100))
        self.smaller_image = self.image
        self.larger_image = pygame.transform.scale(self.image, (310, 120))
        self.xy = coords
        self.rect = self.image.get_rect().move(*self.xy)

    def update(self, *args):
        if (self.rect.collidepoint(*pygame.mouse.get_pos())):
            self.image = self.larger_image
            self.rect = self.image.get_rect().move(self.xy[0] - 10,
                                                   self.xy[1] - 10)
        if not self.rect.collidepoint(*pygame.mouse.get_pos()):
            self.image = self.smaller_image
            self.rect = self.image.get_rect().move(self.xy[0],
                                                   self.xy[1])
        if (args and args[0].type == pygame.MOUSEBUTTONDOWN and
            self.rect.collidepoint(args[0].pos)):
            return False
        if not args:
            pass
        else:
            return True
