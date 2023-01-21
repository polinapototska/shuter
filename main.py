import pygame
pygame.init()

FPS = 40
WIN_WIDTH = 700
WIN_WEIGHT = 500

window = pygame.display.set_mode((WIN_WIDTH, WIN_WEIGHT))
clock = pygame.time.Clock()

play = True
game = True
while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    clock.tick(FPS)
    pygame.display.update()