import pygame, os, sys, math
from Player_stuff import Player, YourBullet
from Enemies import Bullet_Shooter_Module, attack


FPS = 50
WIDTH, HEIGHT = 800, 600


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    enemy_bullet_group = pygame.sprite.Group()

    player = Player((WIDTH//2, HEIGHT//2), (all_sprites, player_group))
    enemy1 = Bullet_Shooter_Module((100, 100), (enemy_group, enemy_group))
    
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
        enemy_group.update(counter)
        
        for enemy in enemy_group.sprites():   
            new_enemy_bullets = attack(enemy, player,
                                       (all_sprites, enemy_bullet_group),
                                       'triple_regular', counter)
        #print(enemy_bullet_group.sprites())
        all_sprites.draw(screen)
        all_sprites.update()
        
        #enemy1.update(counter)
        
        #print(self.rect.x, self.rect.y)
        pygame.display.flip()
        #if counter % 50 == 0:
        #    print(counter//50)
        clock.tick(50)
    pygame.quit()         
