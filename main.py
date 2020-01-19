import pygame, os, sys, math
from levels import dev_mode_level


FPS = 50
WIDTH, HEIGHT = 800, 600


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    dev_mode_level(screen, WIDTH, HEIGHT)
    pygame.quit()         
