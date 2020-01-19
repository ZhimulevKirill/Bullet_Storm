import pygame, os, sys, math, random


STANDART_BULLET_VEL = 5
STANDART_BULLET_AXEL = 0.1
ASSAULT_BULLET_OFFSET = 7
RAY_BULLET_OFFSET = 2
EYE_OFFSET = 3


def load_image(name):
    fullname = os.path.join('C:\\Users\\1\\Desktop\\data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image

def single_regular_homing(enemy, player, groups, counter):
    new_enemy_bullet = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.atan2(player.rect.centerx - enemy.rect.centerx,
                                                        player.rect.centery - enemy.rect.centery))
    return [new_enemy_bullet]

def triple_regular_homing(enemy, player, groups, counter):
    new_enemy_bullet_left = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.atan2(player.rect.centerx - enemy.rect.centerx,
                                                        player.rect.centery - enemy.rect.centery) - math.pi / 5)
    new_enemy_bullet_central = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                                 groups,
                                                 STANDART_BULLET_VEL,
                                                 math.atan2(player.rect.centerx - enemy.rect.centerx,
                                                            player.rect.centery - enemy.rect.centery))
    new_enemy_bullet_right = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                                 groups,
                                                 STANDART_BULLET_VEL,
                                                 math.atan2(player.rect.centerx - enemy.rect.centerx,
                                                            player.rect.centery - enemy.rect.centery) + math.pi / 5)
    return [new_enemy_bullet_left, new_enemy_bullet_central, new_enemy_bullet_right]

def circle_regular(enemy, player, groups, counter):
    new_enemy_bullet = EnemyBulletCircle((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             0)
    return [new_enemy_bullet]

def circle_regular_grav_aff(enemy, player, groups, counter):
    new_enemy_bullet = GravityEnemyBulletCircle((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.pi)
    return [new_enemy_bullet]

def circle_spread_grav_aff(enemy, player, groups, counter):
    out_projectiles = []
    for i in range(1, 5):
        new_enemy_bullet = GravityEnemyBulletCircle((enemy.rect.centerx, enemy.rect.centery),
                                                    groups,
                                                    STANDART_BULLET_VEL,
                                                    math.pi*(i/6))
        out_projectiles.append(new_enemy_bullet)
        new_enemy_bullet = GravityEnemyBulletCircle((enemy.rect.centerx, enemy.rect.centery),
                                                    groups,
                                                    STANDART_BULLET_VEL,
                                                    math.pi*(-i/6))
        out_projectiles.append(new_enemy_bullet)
    new_enemy_bullet = GravityEnemyBulletCircle((enemy.rect.centerx, enemy.rect.centery),
                                                groups,
                                                STANDART_BULLET_VEL,
                                                0)
    out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def tripleshift_regular(enemy, player, groups, counter, shift):
    theta = math.pi / 3
    out_projectiles = []
    for i in range(1, 4):
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.pi*(i/9) + shift)
        out_projectiles.append(new_enemy_bullet)
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.pi*(-i/9) + shift)
        out_projectiles.append(new_enemy_bullet)
    new_enemy_bullet = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                         groups,
                                         STANDART_BULLET_VEL,
                                         0 + shift)
    out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def random_regular(enemy, player, groups, counter):
    out_projectiles = []
    for i in range(5):
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.pi*(random.randint(-5, 5) / 12))
        out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def spread_regular(enemy, player, groups, counter):
    out_projectiles = []
    for i in range(-10, 11):
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.pi*(i / 25))
        out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def spread_regular_homing(enemy, player, groups, counter):
    out_projectiles = []
    player_angle = math.atan2(player.rect.x - enemy.rect.x,
                              player.rect.y - enemy.rect.y)
    for i in range(-10, 11):
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.pi*(i / 25) + player_angle)
        out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def spread_regular_grav_aff(enemy, player, groups, counter):
    out_projectiles = []
    for i in range(-10, 11):
        new_enemy_bullet = EnemyBulletGravity((enemy.rect.centerx, enemy.rect.centery),
                                              groups,
                                              STANDART_BULLET_VEL,
                                              math.pi*(i / 25))
        out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def spread_regular_grav_aff_homing(enemy, player, groups, counter):
    out_projectiles = []
    player_angle = math.atan2(player.rect.x - enemy.rect.x,
                              player.rect.y - enemy.rect.y)
    for i in range(-5, 6):
        new_enemy_bullet = EnemyBulletGravity((enemy.rect.centerx, enemy.rect.centery),
                                              groups,
                                              STANDART_BULLET_VEL,
                                              math.pi*(i / 25) + player_angle)
        out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def assault_regular_homing(enemy, player, groups, counter):
    out_projectiles = []
    player_angle = math.atan2(player.rect.centerx - enemy.rect.centerx,
                              player.rect.centery - enemy.rect.centery)
    for i in range(0, 8):
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.centerx + i * ASSAULT_BULLET_OFFSET * math.sin(player_angle),
                                               enemy.rect.centery + i * ASSAULT_BULLET_OFFSET * math.cos(player_angle)),
                                              groups,
                                              STANDART_BULLET_VEL,
                                              player_angle)
        out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def attack(enemy, player, groups, attack_type, counter):
    out_projectiles = []
    if attack_type == 'single_regular_homing' and counter % 15 == 0:
        out_projectiles.extend(single_regular_homing(enemy, player, groups, counter))

    elif attack_type == 'triple_regular_homing' and counter % 25 == 0:
        out_projectiles.extend(triple_regular_homing(enemy, player, groups, counter))
        
    elif attack_type == 'circle_regular' and counter % 25 == 0:    
        out_projectiles.extend(circle_regular(enemy, player, groups, counter))

    elif attack_type == 'circle_regular_grav_aff' and counter % 25 == 0:    
        out_projectiles.extend(circle_regular_grav_aff(enemy, player, groups, counter))

    elif attack_type == 'circle_spread_grav_aff' and counter % 25 == 0:
        out_projectiles.extend(circle_spread_grav_aff(enemy, player, groups, counter))

    elif attack_type == 'tripleshift_regular' and counter % 30 <= 4 and counter % 30 % 2 == 0:
        out_projectiles.extend(tripleshift_regular(enemy, player, groups, counter, 0))

    elif attack_type == 'tripleshift_regular_shifted' and counter % 30 <= 4 and counter % 30 % 2 == 0:
        out_projectiles.extend(tripleshift_regular(enemy, player, groups, counter, counter % 30 / 25))

    elif attack_type == 'random_regular' and counter % 8 == 0:
        out_projectiles.extend(random_regular(enemy, player, groups, counter))

    elif attack_type == 'spread_regular' and counter % 20 == 0:
        out_projectiles.extend(spread_regular(enemy, player, groups, counter))

    elif attack_type == 'spread_regular_homing' and counter % 25 == 0:
        out_projectiles.extend(spread_regular_homing(enemy, player, groups, counter))

    elif attack_type == 'spread_regular_grav_aff' and counter % 25 == 0:
        out_projectiles.extend(spread_regular_grav_aff(enemy, player, groups, counter))

    elif attack_type == 'spread_regular_grav_aff_homing' and counter % 25 == 0:
        out_projectiles.extend(spread_regular_grav_aff_homing(enemy, player, groups, counter))

    elif attack_type == 'assault_regular_homing' and counter % 20 == 0:
        out_projectiles.extend(assault_regular_homing(enemy, player, groups, counter))
        
    return out_projectiles


class Bullet_Shooter_Module(pygame.sprite.Sprite):
    def __init__(self, coords, player, groups_eye, groups):
        super().__init__(*groups)
        self.image = load_image('Bullet_Shooter_Module.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect().move(*coords)
        self.eye = Bullet_Shooter_Eye(self, player, groups_eye)
        self.way = []
        #x = 500*sin(t) + 500
        
    def update(self, counter, player):
        self.rect.x = 350*math.sin(counter/200) + 375
        self.rect.y = 75*math.cos(counter/200) + 125
        self.eye.update(player, self)


class Bullet_Shooter_Eye(pygame.sprite.Sprite):
    def __init__(self, bullet_shooter, player, groups):
        super().__init__(*groups)
        self.image = load_image('Bullet_Shooter_Eye.png')
        self.image = pygame.transform.scale(self.image, (8, 8))
        player_angle = math.atan2(player.rect.centerx - bullet_shooter.rect.centerx,
                                  player.rect.centery - bullet_shooter.rect.centery)
        self.rect = self.image.get_rect().move(bullet_shooter.rect.centerx + EYE_OFFSET * math.sin(player_angle),
                                               bullet_shooter.rect.centery + EYE_OFFSET * math.cos(player_angle))

    def update(self, player, bullet_shooter):
        player_angle = math.atan2(player.rect.centerx - bullet_shooter.rect.centerx,
                                  player.rect.centery - bullet_shooter.rect.centery)
        self.rect.centerx = bullet_shooter.rect.centerx + EYE_OFFSET * math.sin(player_angle)
        self.rect.centery = bullet_shooter.rect.centery + EYE_OFFSET * math.cos(player_angle)

        
class EnemyBulletCircle(pygame.sprite.Sprite):
    def __init__(self, coords, groups, velocity, angle):
        super().__init__(*groups)
        self.image = load_image('Circle_Bullet.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect().move(*coords)
        self.velocity, self.angle = velocity, angle   

    def update(self):
        self.rect.x += self.velocity * math.sin(self.angle)
        self.rect.y += self.velocity * math.cos(self.angle)
        if self.rect.y > 700 or self.rect.y < -100 or self.rect.x > 900 or self.rect.x < -100:
            self.kill()


class GravityEnemyBulletCircle(EnemyBulletCircle):
    def update(self):
        vel_x = self.velocity * math.sin(self.angle)
        vel_y = self.velocity * math.cos(self.angle)
        self.rect.x += vel_x
        self.rect.y += vel_y
        vel_y += STANDART_BULLET_AXEL
        self.velocity = (vel_x ** 2 + vel_y ** 2) ** 0.5
        self.angle = math.atan2(vel_x, vel_y)
        if self.rect.y > 700 or self.rect.y < -100 or self.rect.x > 900 or self.rect.x < -100:
            self.kill()
            

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
        if self.rect.y > 700 or self.rect.y < -100 or self.rect.x > 900 or self.rect.x < -100:
            self.kill()


class EnemyBulletGravity(EnemyBulletLinear):
    def update(self):
        vel_x = self.velocity * math.sin(self.angle)
        vel_y = self.velocity * math.cos(self.angle)
        self.rect.x += vel_x
        self.rect.y += vel_y
        vel_y += STANDART_BULLET_AXEL
        self.velocity = (vel_x ** 2 + vel_y ** 2) ** 0.5
        self.angle = math.atan2(vel_x, vel_y)
        if self.rect.y > 700 or self.rect.y < -100 or self.rect.x > 900 or self.rect.x < -100:
            self.kill()
