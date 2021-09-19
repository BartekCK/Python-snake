import pygame, sys
from core import cell_number, cell_size, screen, clock, FPS
from fruit import Fruit

pygame.init()


fruit = Fruit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill((175, 215, 70))
        fruit.draw_fruit()
        pygame.display.update()
        clock.tick(FPS)