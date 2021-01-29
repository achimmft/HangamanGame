import pygame
import os
import math

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
    letters.append([positionX, positionY, chr(A + pos), True])

# loading images
imgs = []
for image in range(7):
    pictures = pygame.image.load("hangman" + str(image) + ".png")
    imgs.append(pictures)

hangmanUpdate = 0
word = "DEVELOPER"
guessed = []

# setting up the global variables for colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont('arial', 20)
newFont = pygame.font.SysFont('arial', 50)
TITLE_FONT = pygame.font.SysFont('comicsans', 60)

# setting up the game loop
framePerSecond = 60
clock = pygame.time.Clock()
controller = True


def drawBoard():
    window.fill(WHITE)
    # game title
    txt = TITLE_FONT.render("Hey HANGMAN", 1, BLACK)
    window.blit(txt, (WIDTH / 2 - txt.get_width() / 2, 20))
    # displaying word on the scree
    newWord = ""
    for letter in word:
        if letter in guessed:
            newWord += letter + " "
        else:
            newWord += "_ "
    txt = newFont.render(newWord, 1, BLACK)
    window.blit(txt, (375, 250))
    # drawing button with letters
    for label in letters:
        positionX, positionY, letter, visible = label
        if visible:
            pygame.draw.circle(
                window, BLACK, (positionX, positionY), RADIUS, 2)
            txt = FONT.render(letter, 1, BLACK)
            window.blit(txt, (positionX - txt.get_width() /
                              2, positionY - txt.get_height() / 2))

    window.blit(imgs[hangmanUpdate], (150, 100))
    pygame.display.update()


def DisplayMessaage(input):
    pygame.time.delay(1000)
    window.fill(WHITE)
    txt = FONT.render(input, 1, BLACK)
    window.blit(txt, (WIDTH / 2 - txt.get_width() /
                      2, HEIGHT / 2 - txt.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)


while controller:
    clock.tick(framePerSecond)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            controller = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            for label in letters:
                positionX, positionY, letter, visible = label
                if visible:
                    distance = math.sqrt((mouseX - positionX) **
                                         2 + (mouseY - positionY) ** 2)
                    if distance < RADIUS:
                        label[3] = False
                        guessed.append(letter)
                        if letter not in word:
                            hangmanUpdate += 1

    drawBoard()

    isWon = True
    for letter in word:
        if letter not in guessed:
            isWon = False
            break

    if isWon:
        DisplayMessaage("Congratulations, You won!")
        break

    if hangmanUpdate == 6:
        DisplayMessaage("I'm sorry, You lost!")
        break
pygame.QUIT()
