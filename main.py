import pygame, sys

pygame.init()

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(60)