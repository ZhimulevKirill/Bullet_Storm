import pygame, math
from Player_stuff import Player, YourBullet, load_image, Null_thingy
from Enemies import Bullet_Shooter_Module, Bullet_Shooter_Eye, attack
from Buttons import Start_Button, Loading_Sign, Title, Ship_Explosion
from Buttons import Level_Button, Back_Button, Dev_Level_Button
from Buttons import Restart_Button, Quit_Button


#demo
def keys_check(player):
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


def level_menu(screen, WIDTH, HEIGHT):
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    level_buttons = [Level_Button((155 + j * 215, 155 + i * 215),
                                  (all_sprites, all_sprites),
                                  (j + 1) + 3 * i) for i in range(2) for j in range(3)]
    back_button = Back_Button((20, 520), (all_sprites, all_sprites))
    dev_level_button = Dev_Level_Button((480, 520), (all_sprites, all_sprites))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
            if event.type == pygame.MOUSEBUTTONDOWN:
                #for level_button in level_buttons:
                if level_buttons[0].rect.collidepoint(event.pos):
                    return 'level_1'
                if level_buttons[1].rect.collidepoint(event.pos):
                    return 'level_2'
                if level_buttons[2].rect.collidepoint(event.pos):
                    return 'level_3'
                if level_buttons[3].rect.collidepoint(event.pos):
                    return 'level_4'
                if level_buttons[4].rect.collidepoint(event.pos):
                    return 'level_5'
                if level_buttons[5].rect.collidepoint(event.pos):
                    return 'level_6'
                if back_button.rect.collidepoint(event.pos):
                    return 'start_screen'
                if dev_level_button.rect.collidepoint(event.pos):
                    return 'dev_mode_level'
                #if flag:
                
                    #return flag
        screen.fill((0, 0, 0))
        screen.blit(load_image('Fon.png'), (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(50)

    
def explo_demo(screen, WIDTH, HEIGHT):
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    explo = Ship_Explosion((0, 0), (all_sprites, all_sprites))
    running = True
    counter = 0
    while running:
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        counter += 1
        clock.tick(50)

def victory_screen(screen, WIDTH, HEIGHT, level):
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    running = True
    counter = 0
    quit_button = Quit_Button((650, 520), (all_sprites, all_sprites))
    victory_fon = load_image('Victory_fon.png')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.rect.collidepoint(event.pos):
                    return 'level_menu'
        screen.fill((0, 0, 0))
        screen.blit(victory_fon, (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        counter += 1
        clock.tick(50)

def death_screen(screen, WIDTH, HEIGHT, groups, old_player, counter_old, level):
    #groups[0] = all_sprites
    #groups[1] = bullet_group
    #groups[2] = enemy_group
    #groups[3] = enemy_eyes_group
    #groups[4] = enemy_bullet_group 
    all_sprites = groups[0]
    bullet_group = groups[1]
    enemy_group = groups[2]
    enemy_eyes_group = groups[3]
    enemy_bullet_group = groups[4]
    hpbar_group = groups[5]
    clock = pygame.time.Clock()
    title_group = pygame.sprite.Group()
    player = Ship_Explosion((old_player.rect.x, old_player.rect.y),
                            (title_group, title_group))
    darker_screen = load_image('Darker_screen.png')
    dead_title = load_image('Dead_title.png')
    restart = Restart_Button((20, 520), (all_sprites, all_sprites), level)
    quit_button = Quit_Button((650, 520), (all_sprites, all_sprites))
    running = True
    counter = counter_old
    while running:
        if counter == 37 + counter_old:
            player.kill()
            player = Null_thingy((old_player.rect.x, old_player.rect.y),
                                 (title_group, title_group))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.rect.collidepoint(event.pos):
                    return 'level_menu'
                if restart.rect.collidepoint(event.pos):
                    return level
        screen.fill((0, 0, 0))
        title_group.draw(screen)
        enemy_group.draw(screen)
        enemy_eyes_group.draw(screen)
        enemy_group.update(counter, player)
        all_sprites.draw(screen)
        all_sprites.update()
        hpbar_group.draw(screen)
        if counter % 2 == 0:
            title_group.update()
        screen.blit(darker_screen, (0, 0))
        screen.blit(dead_title, (0, 0))
        pygame.display.flip()
        counter += 1
        clock.tick(50)
 

def start_screen(screen, WIDTH, HEIGHT):
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    title_group = pygame.sprite.Group()

    start = Start_Button((255, 400), (all_sprites, all_sprites))
    title = Title((150, 50), (title_group, title_group))

    flag = None
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag = start.update(event)
                if flag:
                    return flag
        screen.fill((0, 0, 0))
        screen.blit(load_image('Fon.png'), (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        title_group.draw(screen)
        title_group.update(counter)
        pygame.display.flip()
        counter += 1
        clock.tick(50)

def loading_screen(screen, WIDTH, HEIGHT, flag):
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    loading = Loading_Sign((WIDTH - 100, HEIGHT - 100),
                           (all_sprites, all_sprites))
    counter = 0
    while counter <= 40:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
        screen.blit(load_image('Fon.png'), (0, 0))
        all_sprites.update(counter)
        all_sprites.draw(screen)
        counter += 1
        pygame.display.flip()
        clock.tick(50)
    return flag

def dev_mode_level(screen, WIDTH, HEIGHT):
    clock = pygame.time.Clock()

    level = 'dev_mode_level'
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_eyes_group = pygame.sprite.Group()
    enemy_bullet_group = pygame.sprite.Group()
    hpbar_group = pygame.sprite.Group()

    player = Player((WIDTH//2, HEIGHT//2), (player_group, player_group))
    enemy1 = Bullet_Shooter_Module((100, 100), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   1000, 1000)
    
    running = True
    counter = 0
    flag = None
    while running:
        if player.dead:
            flag = death_screen(screen, WIDTH, HEIGHT,
                                (all_sprites, bullet_group, enemy_group,
                                enemy_eyes_group, enemy_bullet_group, hpbar_group),
                                player, counter, level)
            running = False
        elif len(enemy_group) == 0:
            flag = victory_screen(screen, WIDTH, HEIGHT, level)
            running = False
        else:
            counter += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'QUIT'
            keys_check(player)
            new_bullet = YourBullet((player.rect.centerx, player.rect.y),
                                    (all_sprites, bullet_group))
        
            screen.fill((0, 0, 0)) 
            enemy_group.draw(screen)
            enemy_eyes_group.draw(screen)
            enemy_group.update(counter, player, bullet_group)
            
            for enemy in enemy_group.sprites():   
                new_enemy_bullets = attack(enemy, player,
                                           (all_sprites, enemy_bullet_group),
                                           'circle_spread_grav_aff', counter)
            player_group.draw(screen)
            player_group.update(enemy_bullet_group)
            all_sprites.draw(screen)
            all_sprites.update()
            hpbar_group.draw(screen)
            pygame.display.flip()
            clock.tick(50)
    return flag
