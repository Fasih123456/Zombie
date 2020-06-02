import pygame
import random
import math

from pygame import mixer

pygame.init()

#Title
pygame.display.set_caption("Zombie Wars")


# create the screen of 800x600
screen = pygame.display.set_mode((800, 600))

# Main Menu
main_menu_font = pygame.font.Font("freesansbold.ttf", 32)


def mainmenu():
    heading = main_menu_font.render("Welcome to Zombie War", True, (255, 255, 255))
    screen.blit(heading, (210, 10))

    play = main_menu_font.render("Play", True, (255, 0, 0))
    screen.blit(play, (340, 125))

def button (msg,x,y,w,h,i,a):
    mouse = pygame.mouse.get_pos()

# Main Menu
isDoneMenu = True
isDone = True
while isDoneMenu:
    screen.fill((0, 0, 0))

    print("Running")

    # buttons
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 325 + 100 > mouse[0] > 325 and 125 + 50 > mouse[1] > 125:
        pygame.draw.rect(screen, (0, 255, 0), (325, 115, 100, 50))
        if click[0] == 1:
            isDoneMenu = False
    else:
        pygame.draw.rect(screen, (0, 200, 0), (325, 115, 100, 50))

    mainmenu()

    # Pressing keys does stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDoneMenu = False
            isDone = False

    pygame.display.update()

#Main Program
while isDone:
    screen.fill((0, 0, 0))
    print("running2")



    #Pressing keys does stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False

    pygame.display.update()
