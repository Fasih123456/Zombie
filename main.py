import pygame
import random
import math
import time

from pygame import mixer

# Animation Stuff
win = pygame.display.set_mode((500, 480))
deathcount = 0
standingcount = 0

pygame.init()

# Title
pygame.display.set_caption("Zombie Wars")

# create the screen of 800x600
screen = pygame.display.set_mode((800, 600))

# background
Background = pygame.image.load('background.jpg')

# Player
playerlevel = 1
playerhealth = 600 * playerlevel
playerdamage = 25 * playerlevel
playerstamina = 25 * playerlevel
playerexp = 400 * playerlevel
playerdefense = 12 * playerlevel
playerimage = pygame.image.load('svendeath.gif')
playerdeathimage = [pygame.image.load("Death/sven-thole-knight-death-0.png"),
                    pygame.image.load("Death/sven-thole-knight-death-1.png"),
                    pygame.image.load("Death/sven-thole-knight-death-2.png"),
                    pygame.image.load("Death/sven-thole-knight-death-3.png"),
                    pygame.image.load("Death/sven-thole-knight-death-4.png"),
                    pygame.image.load("Death/sven-thole-knight-death-5.png"),
                    pygame.image.load("Death/sven-thole-knight-death-6.png"),
                    pygame.image.load("Death/sven-thole-knight-death-7.png"),
                    pygame.image.load("Death/sven-thole-knight-death-8.png"),
                    pygame.image.load("Death/sven-thole-knight-death-9.png")]
playerstandingimage = [pygame.image.load("Idle/sven-thole-knight-idle-0.png"),
                       pygame.image.load("Idle/sven-thole-knight-idle-1.png"),
                       pygame.image.load("Idle/sven-thole-knight-idle-2.png"),
                       pygame.image.load("Idle/sven-thole-knight-idle-3.png"),
                       pygame.image.load("Idle/sven-thole-knight-idle-4.png"),
                       pygame.image.load("Idle/sven-thole-knight-idle-5.png"),
                       pygame.image.load("Idle/sven-thole-knight-idle-6.png"),
                       pygame.image.load("Idle/sven-thole-knight-idle-7.png")]

width_of_player = 64
height_of_player = 64

# Enemy
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

# Main Program
while isDone:

    # Pressing keys does stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False

    keys = pygame.key.get_pressed()

    if playerhealth <= 0:
        dead = True
    else:
        dead = False

    screen.fill((0, 0, 0))
    screen.blit(Background, (0, 0))

    deathcount
    standingcount

    if deathcount + 1 >= 30:
        walkcount = 0

    if standingcount + 1 >= 21:
        standingcount = 0

    if dead:
        win.blit(playerdeathimage[deathcount // 3], (100, 375))
        time.sleep(0.03)
        deathcount += 1
    else:
        win.blit(playerstandingimage[standingcount // 3], (100, 375))
        time.sleep(0.05)
        standingcount += 1

    win.blit(enemysmallimage, (400, 450))
    screen.blit(enemybigimage, (300, 425))

    pygame.display.update()
