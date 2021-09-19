import pygame
from pygame.math import Vector2
import pygame
from core import cell_number, cell_size, screen

class Fruit:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x, self.pos.y, cell_size, cell_size)
        pygame.draw.rect(screen, (126,166,113), fruit_rect)