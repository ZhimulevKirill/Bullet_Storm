import pygame, os, sys, math


STANDART_BULLET_VEL = 5


def load_image(name):
    fullname = os.path.join('C:\\Users\\1\\Desktop\\data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image

def attack(enemy, player, groups, attack_type, counter):
    out_projectiles = []
    if attack_type == 'single_regular' and counter % 15 == 0:
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.atan2(player.rect.x - enemy.rect.x,
                                                        player.rect.y - enemy.rect.y))
        out_projectiles.append(new_enemy_bullet)
    elif attack_type == 'triple_regular' and counter % 25 == 0:
        new_enemy_bullet_left = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.atan2(player.rect.x - enemy.rect.x,
                                                        player.rect.y - enemy.rect.y) - math.pi / 5)
        new_enemy_bullet_central = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.atan2(player.rect.x - enemy.rect.x,
                                                        player.rect.y - enemy.rect.y))
        new_enemy_bullet_right = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.atan2(player.rect.x - enemy.rect.x,
                                                        player.rect.y - enemy.rect.y) + math.pi / 5)
        out_projectiles.append(new_enemy_bullet_left)
        out_projectiles.append(new_enemy_bullet_central)
        out_projectiles.append(new_enemy_bullet_right)
    return out_projectiles


class Bullet_Shooter_Module(pygame.sprite.Sprite):
    def __init__(self, coords, groups):
        super().__init__(*groups)
        self.image = load_image('Bullet_Shooter_Module.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect().move(*coords)
        self.way = []
        #x = 500*sin(t) + 500
        
    def update(self, counter):
        self.rect.x = 350*math.sin(counter/70) + 375
        self.rect.y = 75*math.cos(counter/70) + 125

class EnemyBulletLinear(pygame.sprite.Sprite):
    def __init__(self, coords, groups, velocity, angle):
        super().__init__(*groups)
        self.image = load_image('enemy_bullet.png')
        self.image = pygame.transform.scale(self.image, (4, 4))
        self.rect = self.image.get_rect().move(*coords)
        self.velocity, self.angle = velocity, angle

    def update(self):
        self.rect.x += self.velocity * math.sin(self.angle)
        self.rect.y += self.velocity * math.cos(self.angle)
        if 700 < self.rect.y < - 100 or 900 < self.rect.x < - 100:
            self.kill()
