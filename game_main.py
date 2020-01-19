import pygame, os, sys


pygame.init()
FPS = 50
WIDTH, HEIGHT = 300, 300
STEP = 5
BULLET_VELOCITY = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def load_image(name):
    fullname = os.path.join('C:\\Users\\1\\Desktop\\data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image

class Player(pygame.sprite.Sprite):
    
    def __init__(self, coords):
        super().__init__(player_group, all_sprites)
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
    def __init__(self, coords):
        super().__init__(bullet_group, all_sprites)
        self.image = load_image('bullet.png')
        self.image = pygame.transform.scale(self.image, (2, 4))
        self.rect = self.image.get_rect().move(*coords)

    def update(self):
        self.rect.y -= BULLET_VELOCITY

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
player = Player((0, 0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    move_keys = [keys[pygame.K_LEFT], keys[pygame.K_RIGHT],
                 keys[pygame.K_DOWN], keys[pygame.K_UP]]
    for i in range(4):
        if move_keys[i]:
            if i == 0:
                player.go_left()
            elif i == 1:
                player.go_right()
            elif i == 2:
                player.go_down()
            elif i == 3:
                player.go_up()
    new_bullet = YourBullet((player.rect.centerx, player.rect.y))
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()         
