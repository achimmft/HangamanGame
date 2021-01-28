import pygame
import os

# setting up display
pygame.init()
WIDTH = 800
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Welcome To Hangman!")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 375
A = 65
for pos in range(26):
    positionX = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (pos % 13))
    positionY = starty + ((pos // 13) * (GAP + RADIUS * 2))
    letters.append([positionX, positionY, chr(A + pos)])

# loading images
imgs = []
for image in range(7):
    pictures = pygame.image.load("hangman" + str(image) + ".png")
    imgs.append(pictures)

hangmanUpdate = 0

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont('ar')

# setting up the game loop
framePerSecond = 60
clock = pygame.time.Clock()
controller = True


def drawBoard():
    window.fill(WHITE)

    # drawing button with letters
    for label in letters:
        positionX, positionY, letter = label
        pygame.draw.circle(window, BLACK, (positionX, positionY), RADIUS, 2)

    window.blit(imgs[hangmanUpdate], (150, 100))
    pygame.display.update()


while controller:
    clock.tick(framePerSecond)

    drawBoard()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            controller = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            print(position)
pygame.QUIT()
