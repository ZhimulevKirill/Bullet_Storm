import pygame, os, sys, math
from levels import dev_mode_level, start_screen, loading_screen, explo_demo, death_screen
from levels import level_menu


FPS = 50
WIDTH, HEIGHT = 800, 600


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    flag = 'start_screen'
    running = True
    while running:
        if flag != 'QUIT':
            #flag = loading_screen(screen, WIDTH, HEIGHT, flag)
            if flag == 'start_screen':
                flag = start_screen(screen, WIDTH, HEIGHT)
            elif flag == 'level_menu':
                flag = level_menu(screen, WIDTH, HEIGHT)
            elif flag == 'dev_mode_level':
                flag = dev_mode_level(screen, WIDTH, HEIGHT)
            elif flag == 'level_1':
                print('1')
                flag = 'level_menu'
            elif flag == 'level_2':
                print('2')
                flag = 'level_menu'
            elif flag == 'level_3':
                print('3')
                flag = 'level_menu'
            elif flag == 'level_4':
                print('4')
                flag = 'level_menu'
            elif flag == 'level_5':
                print('5')
                flag = 'level_menu'
            elif flag == 'level_6':
                print('6')
                flag = 'level_menu'
        else:
            running = False
    pygame.quit()         
