import pygame

cell_number = 20
cell_size = 40

FPS = 60

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
