import pygame, sys
from core import cell_number, cell_size, screen, clock, FPS
from fruit import Fruit
from snake import Snake

pygame.init()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

fruit = Fruit()
snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move()    

        screen.fill((175, 215, 70))

        fruit.draw_fruit()
        snake.draw_snake()

        pygame.display.update()
        clock.tick(FPS)