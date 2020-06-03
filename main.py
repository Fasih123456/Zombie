import pygame
import random
import math

from pygame import mixer

pygame.init()

#Title
pygame.display.set_caption("Zombie Wars")



# create the screen of 800x600
screen = pygame.display.set_mode((800, 600))

#background
Background = pygame.image.load('background.jpg')

#Player
playerlevel = 1
playerhealth = 600 * playerlevel
playerdamage = 25 * playerlevel
playerstamina = 25 * playerlevel
playerexp = 400 * playerlevel
playerdefense = 12 * playerlevel
playerimage = pygame.image.load('svendeath.gif')
playerdeathimage = [pygame.image.load("Death/Capture.png"),pygame.image.load("Death/Capture1.png"),pygame.image.load("Death/Capture2.png"),pygame.image.load("Death/Capture3.png"),pygame.image.load("Death/Capture4.png"),pygame.image.load("Death/Capture5.png"),pygame.image.load("Death/Capture6.png"),pygame.image.load("Death/Capture7.png"),pygame.image.load("Death/Capture8.png"),pygame.image.load("Death/Capture9.png"),pygame.image.load("Death/Capture10.png")]

#Enemy
enemysmallhealth = 400
enemysmalldamage = 15
enemysmalldefense = 30
enemysmallgold = 15
enemysmallimage = pygame.image.load('small zombie.png')

enemybighealth = 1100
enemybigdamage = 40
enemybigdefense = 5
enemybiggold = 55
enemybigimage = pygame.image.load('large_zombie.png')

# Main Menu
main_menu_font = pygame.font.Font("freesansbold.ttf", 32)


def mainmenu():
    heading = main_menu_font.render("Welcome to Zombie War", True, (255, 255, 255))
    screen.blit(heading, (210, 10))

    playbutton = main_menu_font.render("Play", True, (255, 0, 0))
    screen.blit(playbutton, (340, 125))


# Main Menu
isDoneMenu = True
isDone = True
while isDoneMenu:
    screen.fill((0, 0, 0))


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
    screen.blit(Background,(0,0))

    screen.blit(enemysmallimage, (300, 400))
    screen.blit(enemybigimage, (200, 400))


    #Pressing keys does stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
       # if event.type == pygame.K_RIGHT


    pygame.display.update()
