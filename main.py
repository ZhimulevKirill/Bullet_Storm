import pygame, os, sys
from Player_stuff import Player, YourBullet


FPS = 50
WIDTH, HEIGHT = 800, 600









if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()

    player = Player((WIDTH//2, HEIGHT//2), (all_sprites, player_group))
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
        new_bullet = YourBullet((player.rect.centerx, player.rect.y),
                                (all_sprites, bullet_group))
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()         
