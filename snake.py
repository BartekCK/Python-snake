from pygame.math import Vector2
import pygame
import core

class Snake:
    def __init__(self) -> None:
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self) -> None:
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * core.cell_size), int(block.y * core.cell_size), core.cell_size, core.cell_size)
            pygame.draw.rect(core.screen,(183, 191, 122), block_rect)
            
    def move(self):
        body = self.body[:-1]
        body.insert(0, body[0] + self.direction)
        self.body = body[:]