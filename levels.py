import pygame, math
from Player_stuff import Player, YourBullet, load_image
from Enemies import Bullet_Shooter_Module, Bullet_Shooter_Eye, attack
from Buttons import Start_Button, Loading_Sign, Title


#demo
def start_screen(screen, WIDTH, HEIGHT):
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    title_group = pygame.sprite.Group()

    start = Start_Button((255, 400), (all_sprites, all_sprites))
    title = Title((150, 50), (title_group, title_group))

    running = True
    counter = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #pass
                running = all_sprites.update(event)
        screen.fill((0, 0, 0))
        screen.blit(load_image('Fon.png'), (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        title_group.draw(screen)
        title_group.update(counter)
        pygame.display.flip()
        counter += 1
        clock.tick(50)

def loading_screen(screen, WIDTH, HEIGHT):
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    for i in range(0, HEIGHT, 100):
        loading = Loading_Sign((WIDTH - i - 100, i),
                               (all_sprites, all_sprites))
    counter = 0
    while counter <= 100:
        screen.blit(load_image('Fon.png'), (0, 0))
        all_sprites.update(counter)
        all_sprites.draw(screen)
        counter += 1
        pygame.display.flip()
        clock.tick(50)
    

def dev_mode_level(screen, WIDTH, HEIGHT):
    clock = pygame.time.Clock()

    
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_eyes_group = pygame.sprite.Group()
    enemy_bullet_group = pygame.sprite.Group()

    player = Player((WIDTH//2, HEIGHT//2), (all_sprites, player_group))
    #enemy1 = Spawn_Bullet_Shooter((100, 100), player, (enemy_group, enemy_group), (enemy_eyes_group, enemy_eyes_group))
    enemy1 = Bullet_Shooter_Module((100, 100), player,
                                   (enemy_eyes_group, enemy_eyes_group),
                                   (enemy_group, enemy_group))
    
    running = True
    counter = 0
    while running:
        counter += 1
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
        #if counter % 2 == 0:
        new_bullet = YourBullet((player.rect.centerx, player.rect.y),
                                (all_sprites, bullet_group))
        
        screen.fill((0, 0, 0)) 
        enemy_group.draw(screen)
        enemy_eyes_group.draw(screen)
        enemy_group.update(counter, player)
            
        for enemy in enemy_group.sprites():   
            new_enemy_bullets = attack(enemy, player,
                                       (all_sprites, enemy_bullet_group),
                                       'circle_spread_grav_aff', counter)
        #enemy_bullet_group.draw(screen)
        #enemy_bullet_group.update(counter)
        #print(enemy_bullet_group.sprites())
        all_sprites.draw(screen)
        all_sprites.update()
        
        #enemy1.update(counter)
        
        #print(self.rect.x, self.rect.y)
        pygame.display.flip()
        #if counter % 50 == 0:
        #    print(counter//50)
        clock.tick(50)
    return
