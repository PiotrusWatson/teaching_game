import pygame, sys

pygame.init()

size = width, height = 1280, 720

screen = pygame.display.set_mode(size)
black = 0, 0, 0

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
