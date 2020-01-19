import pygame, math
from Player_stuff import Player, YourBullet, load_image, Null_thingy
from Enemies import Bullet_Shooter_Module, Bullet_Shooter_Eye, attack
from Enemies import Destroyer
from Buttons import Start_Button, Loading_Sign, Title, Ship_Explosion
from Buttons import Level_Button, Back_Button, Dev_Level_Button
from Buttons import Restart_Button, Quit_Button
from program_levels import program_level_1, breakdown_level_1, breakdown_level_2
from program_levels import program_level_2_1, program_level_2_2
from program_levels import program_level_3_1, program_level_3_2, program_level_3_3
from program_levels import program_level_4, breakdown_level_4
from program_levels import program_level_5


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

def death_screen(screen, WIDTH, HEIGHT, groups, old_player,
                 counter_old, level, destroyer):
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
    destroyer_group = groups[6]
    clock = pygame.time.Clock()
    title_group = pygame.sprite.Group()
    player = Ship_Explosion((old_player.rect.x, old_player.rect.y),
                            (title_group, title_group))
    demo_destroyer = destroyer
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
        destroyer_group.draw(screen)
        enemy_group.draw(screen)
        enemy_eyes_group.draw(screen)
        destroyer_group.update(counter)
        enemy_group.update(player, demo_destroyer.xy)
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
    destroyer_group = pygame.sprite.Group()

    player = Player((WIDTH//2, HEIGHT//2), (player_group, player_group))
    #enemy1 = Bullet_Shooter_Module((100, 100), player,
    #                               (enemy_eyes_group, enemy_eyes_group),
    #                               (enemy_group, enemy_group),
    #                               hpbar_group,
    #                               1000, 1000)
    demo_destroyer = Destroyer((400, -200), (destroyer_group, destroyer_group),
                               [(141, 88)], [], 'Level_1_destroyer.png',
                               program_level_1)
    enemy1 = Bullet_Shooter_Module((100, 100), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   1000, 1000, demo_destroyer.joints[0])
    
    running = True
    counter = 0
    flag = None
    while running:
        if player.dead:
            flag = death_screen(screen, WIDTH, HEIGHT,
                                (all_sprites, bullet_group, enemy_group,
                                 enemy_eyes_group, enemy_bullet_group,
                                 hpbar_group, destroyer_group),
                                player, counter, level, demo_destroyer)
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
            #new_bullet = YourBullet((player.rect.centerx, player.rect.y),
            #                        (all_sprites, bullet_group))
            player.attack((all_sprites, bullet_group), counter)
        
            screen.fill((0, 0, 0))
            destroyer_group.draw(screen)
            enemy_group.draw(screen)
            enemy_eyes_group.draw(screen)
            
            destroyer_group.update(counter)
            enemy_group.update(player, demo_destroyer.xy, bullet_group)
            
            for enemy in enemy_group.sprites():   
                new_enemy_bullets = attack(enemy, player,
                                           (all_sprites, enemy_bullet_group),
                                           'handswap_circle_left', counter)
            player_group.draw(screen)
            player_group.update(enemy_bullet_group)
            all_sprites.draw(screen)
            all_sprites.update()
            hpbar_group.draw(screen)
            pygame.display.flip()
            clock.tick(50)
    return flag








def level_1(screen, WIDTH, HEIGHT):
    clock = pygame.time.Clock()
    level = 'level_1'
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_eyes_group = pygame.sprite.Group()
    enemy_bullet_group = pygame.sprite.Group()
    hpbar_group = pygame.sprite.Group()
    destroyer_group = pygame.sprite.Group()
    player = Player((WIDTH//2, HEIGHT//2), (player_group, player_group))
    demo_destroyer = Destroyer((400, -200), (destroyer_group, destroyer_group),
                               [(141, 88)], [], 'Level_1_destroyer.png',
                               program_level_1)
    enemy1 = Bullet_Shooter_Module((100, 100), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   1000, 1000, demo_destroyer.joints[0])
    running = True
    counter = 0
    attack_counter = 0
    flag = None
    attack_switch = 0
    while running:
        if player.dead:
            flag = death_screen_level_1(screen, WIDTH, HEIGHT,
                                        (all_sprites, bullet_group, enemy_group,
                                         enemy_eyes_group, enemy_bullet_group,
                                         hpbar_group, destroyer_group),
                                        player, counter, level, demo_destroyer)
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
            #player.attack((all_sprites, bullet_group), counter)
            screen.fill((0, 0, 0))
            destroyer_group.draw(screen)
            enemy_group.draw(screen)
            enemy_eyes_group.draw(screen)
            destroyer_group.update(counter)
            enemy_group.update(player, demo_destroyer.xy, bullet_group)
            if counter > breakdown_level_1:
                player.attack((all_sprites, bullet_group), counter)
                if attack_switch <= 3 and attack_counter % 20 == 0:
                    for enemy in enemy_group.sprites():   
                        new_enemy_bullets = attack(enemy, player,
                                                   (all_sprites, enemy_bullet_group),
                                                   'circle_spread', attack_counter)
                elif 4 <= attack_switch <= 6 and attack_counter % 20 == 0:
                    for enemy in enemy_group.sprites():   
                        new_enemy_bullets = attack(enemy, player,
                                                   (all_sprites, enemy_bullet_group),
                                                   'triple_regular_homing', attack_counter)
                attack_counter += 1
            attack_switch = (attack_switch + 1) % 7
            player_group.draw(screen)
            player_group.update(enemy_bullet_group)
            all_sprites.draw(screen)
            all_sprites.update()
            hpbar_group.draw(screen)
            pygame.display.flip()
            clock.tick(50)
    return flag

def death_screen_level_1(screen, WIDTH, HEIGHT, groups, old_player,
                 counter_old, level, destroyer):
    all_sprites = groups[0]
    bullet_group = groups[1]
    enemy_group = groups[2]
    enemy_eyes_group = groups[3]
    enemy_bullet_group = groups[4]
    hpbar_group = groups[5]
    destroyer_group = groups[6]
    clock = pygame.time.Clock()
    title_group = pygame.sprite.Group()
    player = Ship_Explosion((old_player.rect.x, old_player.rect.y),
                            (title_group, title_group))
    demo_destroyer = destroyer
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
        destroyer_group.draw(screen)
        enemy_group.draw(screen)
        enemy_eyes_group.draw(screen)
        destroyer_group.update(counter)
        enemy_group.update(player, demo_destroyer.xy)
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


def level_2(screen, WIDTH, HEIGHT):
    clock = pygame.time.Clock()
    level = 'level_2'
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_eyes_group = pygame.sprite.Group()
    enemy_bullet_group = pygame.sprite.Group()
    hpbar_group = pygame.sprite.Group()
    destroyer_group = pygame.sprite.Group()
    player = Player((WIDTH//2, HEIGHT//2), (player_group, player_group))
    first_destroyer = Destroyer((400, -200), (destroyer_group, destroyer_group),
                                [(141, 88)], [], 'Level_1_destroyer.png',
                                program_level_2_1)
    second_destroyer = Destroyer((400, -200), (destroyer_group, destroyer_group),
                                 [(141, 88)], [], 'Level_1_destroyer.png',
                                 program_level_2_2)
    enemy1 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   300, 300, first_destroyer.joints[0])
    enemy2 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   300, 300, second_destroyer.joints[0])
    enemy_group_array = [enemy1, enemy2]
    running = True
    counter = 0
    attack_counter = 0
    flag = None
    attack_switch = 0
    while running:
        if player.dead:
            flag = death_screen_level_2(screen, WIDTH, HEIGHT,
                                        (all_sprites, bullet_group, enemy_group,
                                         enemy_eyes_group, enemy_bullet_group,
                                         hpbar_group, destroyer_group),
                                        player, counter, level, first_destroyer, second_destroyer,
                                        enemy_group_array)
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
            screen.fill((0, 0, 0))
            destroyer_group.draw(screen)
            enemy_group.draw(screen)
            enemy_eyes_group.draw(screen)
            destroyer_group.update(counter)
            #enemy_group.update(player, demo_destroyer.xy, bullet_group)
            enemy1.update(player, first_destroyer.xy, bullet_group)
            enemy2.update(player, second_destroyer.xy, bullet_group)
            if enemy1.hp <= 0:
                first_destroyer.kill()
            if enemy2.hp <= 0:
                second_destroyer.kill()
            if counter > breakdown_level_2:
                player.attack((all_sprites, bullet_group), counter)
                if attack_counter % 40 == 0 and enemy1.hp > 0:
                    new_enemy_bulles_1 = attack(enemy1, player,
                                                (all_sprites, enemy_bullet_group),
                                                'circle_spread', attack_counter)
                if attack_counter % 20 == 0 and enemy2.hp > 0:
                    new_enemy_bullets_2 = attack(enemy2, player,
                                                (all_sprites, enemy_bullet_group),
                                                'random_regular', attack_counter)
                
                #if attack_switch <= 3 and attack_counter % 20 == 0:
                #    new_enemy_bullets = attack(enemy, player,
                #                                (all_sprites, enemy_bullet_group),
                #                                'circle_spread', attack_counter)
                #elif 4 <= attack_switch <= 6 and attack_counter % 20 == 0:
                #    new_enemy_bullets = attack(enemy, player,
                #                                (all_sprites, enemy_bullet_group),
                #                                'triple_regular_homing', attack_counter)
                attack_counter += 1
            attack_switch = (attack_switch + 1) % 7
            player_group.draw(screen)
            player_group.update(enemy_bullet_group)
            all_sprites.draw(screen)
            all_sprites.update()
            hpbar_group.draw(screen)
            pygame.display.flip()
            clock.tick(50)
    return flag


def death_screen_level_2(screen, WIDTH, HEIGHT, groups, old_player,
                 counter_old, level, destroyer_1, destroyer_2, old_enemy_group_array):
    all_sprites = groups[0]
    bullet_group = groups[1]
    enemy_group = groups[2]
    enemy_eyes_group = groups[3]
    enemy_bullet_group = groups[4]
    hpbar_group = groups[5]
    destroyer_group = groups[6]
    clock = pygame.time.Clock()
    title_group = pygame.sprite.Group()
    player = Ship_Explosion((old_player.rect.x, old_player.rect.y),
                            (title_group, title_group))
    first_destroyer = destroyer_1
    second_destroyer = destroyer_2
    enemy1 = old_enemy_group_array[0]
    enemy2 = old_enemy_group_array[1]
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
        destroyer_group.draw(screen)
        enemy_group.draw(screen)
        enemy_eyes_group.draw(screen)
        destroyer_group.update(counter)
        #enemy_group.update(player, demo_destroyer.xy)
        enemy1.update(player, first_destroyer.xy, bullet_group)
        enemy2.update(player, second_destroyer.xy, bullet_group)
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

def level_3(screen, WIDTH, HEIGHT):
    clock = pygame.time.Clock()
    level = 'level_3'
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_eyes_group = pygame.sprite.Group()
    enemy_bullet_group = pygame.sprite.Group()
    hpbar_group = pygame.sprite.Group()
    destroyer_group = pygame.sprite.Group()
    player = Player((WIDTH//2, HEIGHT//2), (player_group, player_group))
    first_destroyer = Destroyer((400, -200), (destroyer_group, destroyer_group),
                                [(62, 111), (229, 111)], [], 'Level_m_destroyer.png',
                                program_level_3_1)
    second_destroyer = Destroyer((400, -200), (destroyer_group, destroyer_group),
                                 [(141, 88)], [], 'Level_1_destroyer.png',
                                 program_level_3_2)
    third_destroyer = Destroyer((400, -200), (destroyer_group, destroyer_group),
                                 [(141, 88)], [], 'Level_1_destroyer.png',
                                 program_level_3_3)
                                
    enemy1 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   900, 900, first_destroyer.joints[0])
    enemy2 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   900, 900, first_destroyer.joints[1])
    enemy3 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   300, 300, second_destroyer.joints[0])
    enemy4 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   300, 300, third_destroyer.joints[0])
    enemy_group_array = [enemy1, enemy2, enemy3, enemy4]
    running = True
    counter = 0
    attack_counter = 0
    flag = None
    attack_switch = 0
    while running:
        if player.dead:
            flag = death_screen_level_3(screen, WIDTH, HEIGHT,
                                        (all_sprites, bullet_group, enemy_group,
                                         enemy_eyes_group, enemy_bullet_group,
                                         hpbar_group, destroyer_group),
                                        player, counter, level,
                                        first_destroyer, second_destroyer,
                                        third_destroyer, enemy_group_array)
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
            screen.fill((0, 0, 0))
            destroyer_group.draw(screen)
            enemy_group.draw(screen)
            enemy_eyes_group.draw(screen)
            destroyer_group.update(counter)
            #enemy_group.update(player, demo_destroyer.xy, bullet_group)
            enemy1.update(player, first_destroyer.xy, bullet_group)
            enemy2.update(player, first_destroyer.xy, bullet_group)
            enemy3.update(player, second_destroyer.xy, bullet_group)
            enemy4.update(player, third_destroyer.xy, bullet_group)
            #print(first_destroyer.xy, counter)
            if enemy1.hp <= 0 and enemy2.hp <= 0:
                first_destroyer.kill()
            if enemy3.hp <= 0:
                second_destroyer.kill()
            if enemy4.hp <= 0:
                third_destroyer.kill()
            if counter > breakdown_level_2:
                player.attack((all_sprites, bullet_group), counter)
                if attack_counter % 5 == 0 and enemy1.hp > 0:
                    new_enemy_bulles_1 = attack(enemy1, player,
                                                (all_sprites, enemy_bullet_group),
                                                'circular_circle', attack_counter)
                if attack_counter % 5 == 0 and enemy2.hp > 0:
                    new_enemy_bullets_2 = attack(enemy2, player,
                                                (all_sprites, enemy_bullet_group),
                                                'circular_circle', attack_counter)
                if attack_counter % 20 == 0 and enemy3.hp > 0:
                    new_enemy_bullets_3 = attack(enemy3, player,
                                                (all_sprites, enemy_bullet_group),
                                                'single_regular_homing', attack_counter)
                if attack_counter % 20 == 0 and enemy4.hp > 0:
                    new_enemy_bullets_4 = attack(enemy4, player,
                                                (all_sprites, enemy_bullet_group),
                                                'single_regular_homing', attack_counter)
                
                #if attack_switch <= 3 and attack_counter % 20 == 0:
                #    new_enemy_bullets = attack(enemy, player,
                #                                (all_sprites, enemy_bullet_group),
                #                                'circle_spread', attack_counter)
                #elif 4 <= attack_switch <= 6 and attack_counter % 20 == 0:
                #    new_enemy_bullets = attack(enemy, player,
                #                                (all_sprites, enemy_bullet_group),
                #                                'triple_regular_homing', attack_counter)
                attack_counter += 1
            attack_switch = (attack_switch + 1) % 7
            player_group.draw(screen)
            player_group.update(enemy_bullet_group)
            all_sprites.draw(screen)
            all_sprites.update()
            hpbar_group.draw(screen)
            pygame.display.flip()
            clock.tick(50)
    return flag


def death_screen_level_3(screen, WIDTH, HEIGHT, groups, old_player,
                         counter_old, level,
                         destroyer_1, destroyer_2, destroyer_3,
                         old_enemy_group_array):
    all_sprites = groups[0]
    bullet_group = groups[1]
    enemy_group = groups[2]
    enemy_eyes_group = groups[3]
    enemy_bullet_group = groups[4]
    hpbar_group = groups[5]
    destroyer_group = groups[6]
    clock = pygame.time.Clock()
    title_group = pygame.sprite.Group()
    player = Ship_Explosion((old_player.rect.x, old_player.rect.y),
                            (title_group, title_group))
    first_destroyer = destroyer_1
    second_destroyer = destroyer_2
    third_destroyer = destroyer_3
    enemy1 = old_enemy_group_array[0]
    enemy2 = old_enemy_group_array[1]
    enemy3 = old_enemy_group_array[2]
    enemy4 = old_enemy_group_array[3]
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
        destroyer_group.draw(screen)
        enemy_group.draw(screen)
        enemy_eyes_group.draw(screen)
        destroyer_group.update(counter)
        #enemy_group.update(player, demo_destroyer.xy)
        #print(first_destroyer.xy, counter)
        enemy1.update(player, first_destroyer.xy, bullet_group)
        enemy2.update(player, first_destroyer.xy, bullet_group)
        enemy3.update(player, second_destroyer.xy, bullet_group)
        enemy4.update(player, third_destroyer.xy, bullet_group)
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

def level_4(screen, WIDTH, HEIGHT):
    clock = pygame.time.Clock()
    level = 'level_4'
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_eyes_group = pygame.sprite.Group()
    enemy_bullet_group = pygame.sprite.Group()
    hpbar_group = pygame.sprite.Group()
    destroyer_group = pygame.sprite.Group()
    player = Player((WIDTH//2, HEIGHT//2), (player_group, player_group))
    first_destroyer = Destroyer((400, -200), (destroyer_group, destroyer_group),
                                [(62, 121), (145, 93), (229, 121)], [], 'Level_x_destroyer.png',
                                program_level_4)
              
    enemy1 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   900, 900, first_destroyer.joints[0])
    enemy2 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   900, 900, first_destroyer.joints[1])
    enemy3 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   900, 900, first_destroyer.joints[2])
    enemy_group_array = [enemy1, enemy2, enemy3]
    running = True
    counter = 0
    attack_counter = 0
    flag = None
    attack_switch = 0
    while running:
        if player.dead:
            flag = death_screen_level_4(screen, WIDTH, HEIGHT,
                                        (all_sprites, bullet_group, enemy_group,
                                         enemy_eyes_group, enemy_bullet_group,
                                         hpbar_group, destroyer_group),
                                        player, counter, level,
                                        first_destroyer, enemy_group_array)
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
            screen.fill((0, 0, 0))
            destroyer_group.draw(screen)
            enemy_group.draw(screen)
            enemy_eyes_group.draw(screen)
            destroyer_group.update(counter)
            enemy1.update(player, first_destroyer.xy, bullet_group)
            enemy2.update(player, first_destroyer.xy, bullet_group)
            enemy3.update(player, first_destroyer.xy, bullet_group)
            if enemy1.hp <= 0 and enemy2.hp <= 0 and enemy3.hp <= 0:
                first_destroyer.kill()
            if counter > breakdown_level_4:
                player.attack((all_sprites, bullet_group), counter)
                if attack_counter % 3 == 0 and enemy1.hp > 0:
                    new_enemy_bulles_1 = attack(enemy1, player,
                                                (all_sprites, enemy_bullet_group),
                                                'circular_circle_fast', attack_counter)
                if attack_counter % 3 == 0 and enemy3.hp > 0:
                    new_enemy_bullets_3 = attack(enemy3, player,
                                                (all_sprites, enemy_bullet_group),
                                                'circular_circle_fast', attack_counter)
                if attack_counter % 15 == 0 and enemy2.hp > 0:
                    new_enemy_bullets_2 = attack(enemy2, player,
                                                (all_sprites, enemy_bullet_group),
                                                'random_regular', attack_counter)
                attack_counter += 1
            attack_switch = (attack_switch + 1) % 7
            player_group.draw(screen)
            player_group.update(enemy_bullet_group)
            all_sprites.draw(screen)
            all_sprites.update()
            hpbar_group.draw(screen)
            pygame.display.flip()
            clock.tick(50)
    return flag


def death_screen_level_4(screen, WIDTH, HEIGHT, groups, old_player,
                         counter_old, level,
                         destroyer_1, old_enemy_group_array):
    all_sprites = groups[0]
    bullet_group = groups[1]
    enemy_group = groups[2]
    enemy_eyes_group = groups[3]
    enemy_bullet_group = groups[4]
    hpbar_group = groups[5]
    destroyer_group = groups[6]
    clock = pygame.time.Clock()
    title_group = pygame.sprite.Group()
    player = Ship_Explosion((old_player.rect.x, old_player.rect.y),
                            (title_group, title_group))
    first_destroyer = destroyer_1
    enemy1 = old_enemy_group_array[0]
    enemy2 = old_enemy_group_array[1]
    enemy3 = old_enemy_group_array[2]
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
        destroyer_group.draw(screen)
        enemy_group.draw(screen)
        enemy_eyes_group.draw(screen)
        destroyer_group.update(counter)
        enemy1.update(player, first_destroyer.xy, bullet_group)
        enemy2.update(player, first_destroyer.xy, bullet_group)
        enemy3.update(player, first_destroyer.xy, bullet_group)
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

def level_5(screen, WIDTH, HEIGHT):
    clock = pygame.time.Clock()
    level = 'level_5'
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_eyes_group = pygame.sprite.Group()
    enemy_bullet_group = pygame.sprite.Group()
    hpbar_group = pygame.sprite.Group()
    destroyer_group = pygame.sprite.Group()
    player = Player((WIDTH//2, HEIGHT//2), (player_group, player_group))
    first_destroyer = Destroyer((400, -200), (destroyer_group, destroyer_group),
                                [(62, 121), (127, 85),
                                 (145, 60), (163, 85), (229, 121)],
                                [], 'Level_y_destroyer.png',
                                program_level_5)
              
    enemy1 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   900, 900, first_destroyer.joints[0])
    enemy2 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   900, 900, first_destroyer.joints[1])
    enemy3 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   900, 900, first_destroyer.joints[2])
    enemy4 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   900, 900, first_destroyer.joints[3])
    enemy5 = Bullet_Shooter_Module((-50, -50), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group),
                                   hpbar_group,
                                   900, 900, first_destroyer.joints[4])
    enemy_group_array = [enemy1, enemy2, enemy3, enemy4, enemy5]
    running = True
    counter = 0
    attack_counter = 0
    flag = None
    attack_switch = 0
    while running:
        if player.dead:
            flag = death_screen_level_5(screen, WIDTH, HEIGHT,
                                        (all_sprites, bullet_group, enemy_group,
                                         enemy_eyes_group, enemy_bullet_group,
                                         hpbar_group, destroyer_group),
                                        player, counter, level,
                                        first_destroyer, enemy_group_array)
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
            screen.fill((0, 0, 0))
            destroyer_group.draw(screen)
            enemy_group.draw(screen)
            enemy_eyes_group.draw(screen)
            destroyer_group.update(counter)
            enemy1.update(player, first_destroyer.xy, bullet_group)
            enemy2.update(player, first_destroyer.xy, bullet_group)
            enemy3.update(player, first_destroyer.xy, bullet_group)
            enemy4.update(player, first_destroyer.xy, bullet_group)
            enemy5.update(player, first_destroyer.xy, bullet_group)
            if (enemy1.hp <= 0 and enemy2.hp <= 0 and
                enemy3.hp <= 0 and enemy4.hp <= 0 and enemy5.hp <= 0):
                first_destroyer.kill()
            if counter > breakdown_level_2:
                player.attack((all_sprites, bullet_group), counter)
                if attack_counter % 56 <= 8 and enemy1.hp > 0:
                    new_enemy_bulles_1 = attack(enemy1, player,
                                                (all_sprites, enemy_bullet_group),
                                                'handswap_circle_left', attack_counter)
                if attack_counter % 20 == 10 and enemy2.hp > 0:
                    new_enemy_bullets_2 = attack(enemy2, player,
                                                (all_sprites, enemy_bullet_group),
                                                'spread_regular_grav_aff', 0)
                if attack_counter % 15 == 0 and enemy3.hp > 0:
                    new_enemy_bullets_3 = attack(enemy3, player,
                                                (all_sprites, enemy_bullet_group),
                                                'triple_regular_homing', attack_counter)
                if attack_counter % 20 == 0 and enemy4.hp > 0:
                    new_enemy_bullets_4 = attack(enemy4, player,
                                                (all_sprites, enemy_bullet_group),
                                                'spread_regular_grav_aff', attack_counter)
                if 28 <= attack_counter % 56 <= 36 and enemy5.hp > 0:
                    new_enemy_bullets_5 = attack(enemy5, player,
                                                 (all_sprites, enemy_bullet_group),
                                                 'handswap_circle_right', attack_counter)
                attack_counter += 1
            attack_switch = (attack_switch + 1) % 7
            player_group.draw(screen)
            player_group.update(enemy_bullet_group)
            all_sprites.draw(screen)
            all_sprites.update()
            hpbar_group.draw(screen)
            pygame.display.flip()
            clock.tick(50)
    return flag


def death_screen_level_5(screen, WIDTH, HEIGHT, groups, old_player,
                         counter_old, level,
                         destroyer_1, old_enemy_group_array):
    all_sprites = groups[0]
    bullet_group = groups[1]
    enemy_group = groups[2]
    enemy_eyes_group = groups[3]
    enemy_bullet_group = groups[4]
    hpbar_group = groups[5]
    destroyer_group = groups[6]
    clock = pygame.time.Clock()
    title_group = pygame.sprite.Group()
    player = Ship_Explosion((old_player.rect.x, old_player.rect.y),
                            (title_group, title_group))
    first_destroyer = destroyer_1
    enemy1 = old_enemy_group_array[0]
    enemy2 = old_enemy_group_array[1]
    enemy3 = old_enemy_group_array[2]
    enemy4 = old_enemy_group_array[3]
    enemy5 = old_enemy_group_array[4]
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
        destroyer_group.draw(screen)
        enemy_group.draw(screen)
        enemy_eyes_group.draw(screen)
        destroyer_group.update(counter)
        enemy1.update(player, first_destroyer.xy, bullet_group)
        enemy2.update(player, first_destroyer.xy, bullet_group)
        enemy3.update(player, first_destroyer.xy, bullet_group)
        enemy4.update(player, first_destroyer.xy, bullet_group)
        enemy5.update(player, first_destroyer.xy, bullet_group)
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
