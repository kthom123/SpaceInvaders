import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player(x,y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keystroke check
    if event.type == pygame.KEYDOWN:
        print("A keystroke is pressed")
        if event.key == pygame.K_LEFT:
            print("Left arrow is pressed")
        if event.key == pygame.K_RIGHT:
            print("Right arrow is pressed")
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            print("Keystroke has been released")

    player(playerX,playerY)
    pygame.display.update()
