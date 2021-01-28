import pygame
import os

# setting up display
pygame.init()
WIDTH = 800
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
for pos in rang(26):
    positionX = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (pos % 13))
    positiony = starty + ((pos // 13) * (GAP + RADIUS * 2))
    letters.append([positionX, positiony])

# loading images
imgs = []
for image in range(7):
    pictures = pygame.image.load("hangman" + str(image) + ".png")
    imgs.append(pictures)

hangmanUpdate = 5

# colors
WHITE = (255, 255, 255)
# setting up the game loop
framePerSecond = 60
clock = pygame.time.Clock()
controller = True

while controller:
    clock.tick(framePerSecond)

    window.fill(WHITE)
    window.blit(imgs[hangmanUpdate], (150, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            controller = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            print(position)
pygame.QUIT()
