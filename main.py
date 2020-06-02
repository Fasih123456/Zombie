import pygame
import random
import math

from pygame import mixer

pygame.init()

# create the screen of 800x600
screen = pygame.display.set_mode((800,600))

# Main Menu
main_menu_font = pygame.font.Font("freesansbold.ttf", 32)


def mainmenu():
    heading = main_menu_font.render("Welcome to war games", True, (255, 255, 255))
    screen.blit(heading, (300, 250))


# Main program
mainmenu()
isDone = True
while isDone:
    mainmenu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
