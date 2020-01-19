import pygame, os, math


BULLET_VEL = 20


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


class Ship_Explosion(pygame.sprite.Sprite):
    def __init__(self, coords, groups):
        super().__init__(*groups)
        self.frames = []
        self.sheet = load_image('Explosion_animation.png')
        self.cut_sheet()
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(*coords)

    def cut_sheet(self, columns=16, rows=1):
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


class Quit_Button(pygame.sprite.Sprite):
    def __init__(self, coords, groups):
        super().__init__(*groups)
        self.xy = coords
        self.image = load_image('Quit_Button.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.larger_image = pygame.transform.scale(self.image, (150, 80))
        self.smaller_image = pygame.transform.scale(self.image, (130, 60))
        self.rect = self.image.get_rect().move(*coords)

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
            #print('level_' + str(self.level))
            return 'level_menu'
        if not args:
            pass
        else:
            return None


class Restart_Button(pygame.sprite.Sprite):
    def __init__(self, coords, groups, level):
        super().__init__(*groups)
        self.xy = coords
        self.level = level
        self.image = load_image('Restart_Button.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.larger_image = pygame.transform.scale(self.image, (220, 80))
        self.smaller_image = pygame.transform.scale(self.image, (200, 60))
        self.rect = self.image.get_rect().move(*coords)

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
            #print('level_' + str(self.level))
            return self.level
        if not args:
            pass
        else:
            return None


class Dev_Level_Button(pygame.sprite.Sprite):
    def __init__(self, coords, groups):
        super().__init__(*groups)
        self.xy = coords
        self.image = load_image('Dev_level.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.larger_image = pygame.transform.scale(self.image, (80, 80))
        self.smaller_image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect().move(*coords)

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
            #print('level_' + str(self.level))
            return 'dev_mode_level'
        if not args:
            pass
        else:
            return None


class Back_Button(pygame.sprite.Sprite):
    def __init__(self, coords, groups):
        super().__init__(*groups)
        self.image = load_image('Back_button.png')
        self.xy = coords
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.larger_image = pygame.transform.scale(self.image, (80, 80))
        self.smaller_image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect().move(*coords)

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
            return 'level_' + str(self.level)
        if not args:
            pass
        else:
            return None

class Level_Button(pygame.sprite.Sprite):
    def __init__(self, coords, groups, level):
        super().__init__(*groups)
        self.level = level
        #print(level)
        self.xy = coords
        self.image = load_image('Level_' + str(level) + '_icon.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.larger_image = pygame.transform.scale(self.image, (80, 80))
        self.smaller_image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect().move(*coords)

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
            #print('level_' + str(self.level))
            return 'level_' + str(self.level)
        if not args:
            pass
        else:
            return None


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
            #return 'dev_mode_level'
            return 'level_menu'
        if not args:
            pass
        else:
            return None
