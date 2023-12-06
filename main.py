import pygame
import constants

#initialise pygame
pygame.init()

#create clock
clock = pygame.time.Clock()

#create gamewindow
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Totally accurate tower")

#load images
enemy_image = pygame.image.load('assets/images/enemies/enemy_1.png')

#game loop
run = True
while run:
    clock.tick(constants.FPS)

    #event handler
    for event in pygame.event.get():
        #quit program
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
