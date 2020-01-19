import pygame, os, sys, math
from levels import dev_mode_level, start_screen, loading_screen


FPS = 50
WIDTH, HEIGHT = 800, 600


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    start_screen(screen, WIDTH, HEIGHT)
    loading_screen(screen, WIDTH, HEIGHT)
    dev_mode_level(screen, WIDTH, HEIGHT)
    pygame.quit()         
