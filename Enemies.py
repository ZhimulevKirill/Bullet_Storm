import pygame, os, sys, math, random
import shapely
from shapely.geometry.point import Point
from shapely.geometry import Polygon


STANDART_BULLET_VEL = 5
STANDART_BULLET_AXEL = 0.1
ASSAULT_BULLET_OFFSET = 7
RAY_BULLET_OFFSET = 2
EYE_OFFSET = 3


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image

def single_regular_homing(enemy, player, groups, counter):
    new_enemy_bullet = EnemyBulletLinear((enemy.rect.x + 15, enemy.rect.y + 15),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.atan2(player.rect.x + 30 - (enemy.rect.x + 15),
                                                        player.rect.y + 40 - (enemy.rect.y + 15)))
    return [new_enemy_bullet]

def triple_regular_homing(enemy, player, groups, counter):
    new_enemy_bullet_left = EnemyBulletLinear((enemy.rect.x + 15, enemy.rect.y + 15),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.atan2(player.rect.x + 30 - (enemy.rect.x + 15),
                                                        player.rect.y + 40 - (enemy.rect.y + 15)) - math.pi / 5)
    new_enemy_bullet_central = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                                 groups,
                                                 STANDART_BULLET_VEL,
                                                 math.atan2(player.rect.x + 30 - (enemy.rect.x + 15),
                                                            player.rect.y + 40 - (enemy.rect.y + 15)))
    new_enemy_bullet_right = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                                 groups,
                                                 STANDART_BULLET_VEL,
                                                 math.atan2(player.rect.x + 30 - (enemy.rect.x + 15),
                                                            player.rect.y + 40 - (enemy.rect.y + 15)) + math.pi / 5)
    return [new_enemy_bullet_left, new_enemy_bullet_central, new_enemy_bullet_right]

def triple_regular(enemy, player, groups, counter):
    new_enemy_bullet_left = EnemyBulletLinear((enemy.rect.x + 15, enemy.rect.y + 15),
                                             groups,
                                             STANDART_BULLET_VEL,
                                              - math.pi / 5)
    new_enemy_bullet_central = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                                 groups,
                                                 STANDART_BULLET_VEL,
                                                 0)
    new_enemy_bullet_right = EnemyBulletLinear((enemy.rect.centerx, enemy.rect.centery),
                                                 groups,
                                                 STANDART_BULLET_VEL,
                                                 math.pi / 5)
    return [new_enemy_bullet_left, new_enemy_bullet_central, new_enemy_bullet_right]

def circle_regular(enemy, player, groups, counter):
    new_enemy_bullet = EnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             0)
    return [new_enemy_bullet]

def circle_regular_grav_aff(enemy, player, groups, counter):
    new_enemy_bullet = GravityEnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.pi)
    return [new_enemy_bullet]

def circle_spread_grav_aff(enemy, player, groups, counter):
    out_projectiles = []
    for i in range(1, 5):
        new_enemy_bullet = GravityEnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                                    groups,
                                                    STANDART_BULLET_VEL,
                                                    math.pi*(i/6))
        out_projectiles.append(new_enemy_bullet)
        new_enemy_bullet = GravityEnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                                    groups,
                                                    STANDART_BULLET_VEL,
                                                    math.pi*(-i/6))
        out_projectiles.append(new_enemy_bullet)
    new_enemy_bullet = GravityEnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                                groups,
                                                STANDART_BULLET_VEL,
                                                0)
    out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def tripleshift_regular(enemy, player, groups, counter, shift):
    theta = math.pi / 3
    out_projectiles = []
    for i in range(1, 4):
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.x + 15, enemy.rect.y + 15),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.pi*(i/9) + shift)
        out_projectiles.append(new_enemy_bullet)
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.x + 15, enemy.rect.y + 15),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.pi*(-i/9) + shift)
        out_projectiles.append(new_enemy_bullet)
    new_enemy_bullet = EnemyBulletLinear((enemy.rect.x + 15, enemy.rect.y + 15),
                                         groups,
                                         STANDART_BULLET_VEL,
                                         0 + shift)
    out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def random_regular(enemy, player, groups, counter):
    out_projectiles = []
    for i in range(5):
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.x + 15, enemy.rect.y + 15),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.pi*(random.randint(-5, 5) / 12))
        out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def spread_regular(enemy, player, groups, counter):
    out_projectiles = []
    for i in range(-10, 11, 4):
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.x + 15, enemy.rect.y + 15),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.pi*(i / 25))
        out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def spread_regular_homing(enemy, player, groups, counter):
    out_projectiles = []
    player_angle = math.atan2(player.rect.x + 30 - (enemy.rect.x + 15),
                              player.rect.y + 40 - (enemy.rect.y + 15))
    for i in range(-10, 11):
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.x + 15, enemy.rect.y + 15),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.pi*(i / 25) + player_angle)
        out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def spread_regular_grav_aff(enemy, player, groups, counter):
    out_projectiles = []
    for i in range(-10, 11, 3):
        new_enemy_bullet = EnemyBulletGravity((enemy.rect.x + 15, enemy.rect.y + 15),
                                              groups,
                                              STANDART_BULLET_VEL,
                                              math.pi*(i / 25))
        out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def spread_regular_grav_aff_homing(enemy, player, groups, counter):
    out_projectiles = []
    player_angle = math.atan2(player.rect.x + 30 - (enemy.rect.x + 15),
                              player.rect.y + 40 - (enemy.rect.y + 15))
    for i in range(-5, 6):
        new_enemy_bullet = EnemyBulletGravity((enemy.rect.x + 15, enemy.rect.y + 15),
                                              groups,
                                              STANDART_BULLET_VEL,
                                              math.pi*(i / 25) + player_angle)
        out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def assault_regular_homing(enemy, player, groups, counter):
    out_projectiles = []
    player_angle = math.atan2(player.rect.x + 30 - (enemy.rect.x + 15),
                              player.rect.y + 40 - (enemy.rect.y + 15))
    for i in range(0, 5):
        new_enemy_bullet = EnemyBulletLinear((enemy.rect.x + 15 + i * ASSAULT_BULLET_OFFSET * math.sin(player_angle),
                                               enemy.rect.y + 15 + i * ASSAULT_BULLET_OFFSET * math.cos(player_angle)),
                                              groups,
                                              STANDART_BULLET_VEL,
                                              player_angle)
        out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def circle_spread(enemy, player, groups, counter):
    out_projectiles = []
    for i in range(1, 5):
        new_enemy_bullet = EnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                                    groups,
                                                    STANDART_BULLET_VEL,
                                                    math.pi*(i/6))
        out_projectiles.append(new_enemy_bullet)
        new_enemy_bullet = EnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                                    groups,
                                                    STANDART_BULLET_VEL,
                                                    math.pi*(-i/6))
        out_projectiles.append(new_enemy_bullet)
    new_enemy_bullet = EnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                                groups,
                                                STANDART_BULLET_VEL,
                                                0)
    out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def circular_circle(enemy, player, groups, counter):
    new_enemy_bullet = EnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                         groups, STANDART_BULLET_VEL,
                                         (counter % 40) * math.pi / 20)
    return [new_enemy_bullet]

def rapid_circle_homing(enemy, player, groups, counter):
    new_enemy_bullet = EnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                             groups,
                                             STANDART_BULLET_VEL,
                                             math.atan2(player.rect.x + 30 - (enemy.rect.x + 15),
                                                        player.rect.y + 40 - (enemy.rect.y + 15)))
    return [new_enemy_bullet]

def circle_spread_fist(enemy, player, groups, counter):
    out_projectiles = []
    player_angle = math.atan2(player.rect.x + 30 - (enemy.rect.x + 15),
                              player.rect.y + 40 - (enemy.rect.y + 15))
    for i in range(1, 5):
        new_enemy_bullet = EnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                                    groups,
                                                    STANDART_BULLET_VEL,
                                                    math.pi*(i/24) + player_angle)
        out_projectiles.append(new_enemy_bullet)
        new_enemy_bullet = EnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                                    groups,
                                                    STANDART_BULLET_VEL,
                                                    math.pi*(-i/24) + player_angle)
        out_projectiles.append(new_enemy_bullet)
    new_enemy_bullet = EnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                                groups,
                                                STANDART_BULLET_VEL,
                                                player_angle)
    out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def handswap_circle_left(enemy, player, groups, counter):
    out_projectiles = []
    angle = - math.pi / 4
    new_enemy_bullet = EnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                            groups,
                                            STANDART_BULLET_VEL,
                                            angle + (counter % 56) * math.pi / 8)
    out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def handswap_circle_right(enemy, player, groups, counter):
    out_projectiles = []
    angle = 5 * math.pi / 4
    new_enemy_bullet = EnemyBulletCircle((enemy.rect.x + 15, enemy.rect.y + 15),
                                            groups,
                                            STANDART_BULLET_VEL,
                                            angle + (counter % 56) % 9 * math.pi / 8)
    out_projectiles.append(new_enemy_bullet)
    return out_projectiles

def attack(enemy, player, groups, attack_type, counter):
    out_projectiles = []
    if attack_type == 'single_regular_homing' and counter % 20 == 0:
        out_projectiles.extend(single_regular_homing(enemy, player, groups, counter))

    elif attack_type == 'triple_regular_homing' and counter % 20 == 0:
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

    elif attack_type == 'random_regular' and counter % 5 == 0:
        out_projectiles.extend(random_regular(enemy, player, groups, counter))

    elif attack_type == 'spread_regular' and counter % 20 == 0:
        out_projectiles.extend(spread_regular(enemy, player, groups, counter))

    elif attack_type == 'spread_regular_homing' and counter % 25 == 0:
        out_projectiles.extend(spread_regular_homing(enemy, player, groups, counter))

    elif attack_type == 'spread_regular_grav_aff' and counter % 20 == 0:
        out_projectiles.extend(spread_regular_grav_aff(enemy, player, groups, counter))

    elif attack_type == 'spread_regular_grav_aff_homing' and counter % 25 == 0:
        out_projectiles.extend(spread_regular_grav_aff_homing(enemy, player, groups, counter))

    elif attack_type == 'assault_regular_homing' and counter % 5 == 0:
        out_projectiles.extend(assault_regular_homing(enemy, player, groups, counter))
        
    elif attack_type == 'circle_spread' and counter % 20 == 0:
        out_projectiles.extend(circle_spread(enemy, player, groups, counter))

    elif attack_type == 'circular_circle' and counter % 5 == 0:
        out_projectiles.extend(circular_circle(enemy, player, groups, counter))

    elif attack_type == 'circular_circle_fast' and counter % 3 == 0:
        out_projectiles.extend(circular_circle(enemy, player, groups, counter))

    elif attack_type == 'rapid_circle_homing' and counter % 8 == 0:
        out_projectiles.extend(rapid_circle_homing(enemy, player, groups, counter))
        #out_projectiles.extend(single_regular_homing(enemy, player, groups, counter))

    elif attack_type == 'circle_spread_fist' and counter % 20 == 0:
        out_projectiles.extend(circle_spread_fist(enemy, player, groups, counter))

    elif attack_type == 'handswap_circle_left' and counter % 56 <= 8:
        out_projectiles.extend(handswap_circle_left(enemy, player, groups, counter))

    elif attack_type == 'handswap_circle_right' and 28 <=  counter % 56 <= 36:
        out_projectiles.extend(handswap_circle_right(enemy, player, groups, counter))

    elif attack_type == 'triple_regular' and counter % 5 == 0:
        out_projectiles.extend(triple_regular(enemy, player, groups, counter))
        
    return out_projectiles


class Destroyer(pygame.sprite.Sprite):
    #
    def __init__(self, coords, groups, joints, module_types, image, program):
        super().__init__(*groups)
        self.image = load_image(image)
        self.image = pygame.transform.scale(self.image, (300, 150))
        self.wh = [300, 150]
        self.xy = coords
        self.rect = self.image.get_rect().move(coords[0],
                                               coords[1])
        self.joints = joints
        self.program = program
        self.program_length = sum([command[0][1] - command[0][0] + 1 for command in self.program])

    def update(self, counter):
        #command = [(counter_bottom, counter_top), function_x, function_y]
        #function = def function(counter): ...
        for command in self.program:
            if command[0][0] <= counter % self.program_length <= command[0][1]:
                function_x = command[1]
                function_y = command[2]
                self.rect.x = function_x(counter)
                self.rect.y = function_y(counter)
                self.xy = (self.rect.x, self.rect.y)


class HPBar(pygame.sprite.Sprite):
    def __init__(self, coords, groups, hp, max_health):
        super().__init__(*groups)
        self.bar = load_image('HP_bar.png')
        self.max_health = max_health
        self.bar_filling = load_image('HP_itself.png')
        self.bar_filling = pygame.transform.scale(self.bar_filling, (int(46*(hp/self.max_health)), 6))
        self.image = self.bar.copy()
        self.image.blit(self.bar_filling, (2, 2))
        self.rect = self.image.get_rect().move(*coords)

    def update(self, entity):
        if entity.hp > 0:
        #self.bar_filling = pygame.transform.scale(self.bar_filling, (int(46*(entity.hp/self.max_health)), 6))
            self.image = self.bar.copy()
            self.image.blit(pygame.transform.scale(self.bar_filling, (int(46*(entity.hp/self.max_health)), 6)), (2, 2))
            #print(entity.hp)
            self.rect.x = entity.rect.x
            self.rect.y = entity.rect.y + 50


class Bullet_Shooter_Module(pygame.sprite.Sprite):
    #position on destroyer is a tuple of coords on the destroyer's surface
    def __init__(self, coords, player, groups_eye, groups, hpbar_group,
                 hp, max_hp, position_on_destroyer):
        super().__init__(*groups)
        self.image = load_image('Bullet_Shooter_Module.png')
        #self.image = pygame.Surface((50, 50))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect().move(*coords)
        self.eye = Bullet_Shooter_Eye(self, player, groups_eye)
        self.hp_bar = HPBar((self.rect.x, self.rect.y + 50),
                            (hpbar_group, hpbar_group),
                            hp, max_hp)
        self.hp = hp
        self.hitbox = Point(coords[0] + 25, coords[1] + 25).buffer(25.0)
        self.way = []
        self.joint_coords = position_on_destroyer
        #x = 500*sin(t) + 500
        
    #def update(self, counter, player, *bullet_group):
        #self.rect.x = 350*math.sin(counter/200) + 375
        #self.rect.y = 75*math.cos(counter/200) + 125
    def update(self, player, coords, *bullet_group):
        #coords - destroyer's coords
        if self.hp > 0:
            self.rect.x = coords[0] + self.joint_coords[0] - 25
            self.rect.y = coords[1] + self.joint_coords[1] - 25
            #print(self.rect.x, self.rect.y)
            self.hitbox = Point(*self.rect.center).buffer(25.0)
            self.eye.update(player, self)
            self.hp_bar.update(self)
            self.hitbox = Point(self.rect.x + 25, self.rect.y + 25).buffer(25.0)
            if bullet_group:
                for bullet in bullet_group[0]:
                    if bullet.hitbox.intersects(self.hitbox):
                        self.hp -= bullet.damage
                        bullet.kill()
        if self.hp <= 0:
            self.eye.kill()
            self.kill()
            self.hp_bar.kill()


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
        self.hitbox = Point(coords[0] + 15, coords[1] + 15).buffer(15.0)

    def update(self):
        self.rect.x += self.velocity * math.sin(self.angle)
        self.rect.y += self.velocity * math.cos(self.angle)
        self.hitbox = Point(*self.rect.center).buffer(15.0)
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
        self.hitbox = Point(*self.rect.center).buffer(15.0)
        if self.rect.y > 700 or self.rect.y < -100 or self.rect.x > 900 or self.rect.x < -100:
            self.kill()
            

class EnemyBulletLinear(pygame.sprite.Sprite):
    def __init__(self, coords, groups, velocity, angle):
        super().__init__(*groups)
        self.image = load_image('enemy_bullet.png')
        self.image = pygame.transform.scale(self.image, (4, 4))
        self.rect = self.image.get_rect().move(*coords)
        self.velocity, self.angle = velocity, angle
        self.hitbox = Point(coords[0] + 2, coords[1] + 2).buffer(2.0)

    def update(self):
        self.rect.x += self.velocity * math.sin(self.angle)
        self.rect.y += self.velocity * math.cos(self.angle)
        self.hitbox = Point(*self.rect.center).buffer(2.0)
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
        self.hitbox = Point(*self.rect.center).buffer(2.0)
        if self.rect.y > 700 or self.rect.y < -100 or self.rect.x > 900 or self.rect.x < -100:
            self.kill()
