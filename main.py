# Example file showing a basic pygame "game loop"
import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1910, 1070))
clock = pygame.time.Clock()
running = True

hero_image = pygame.image.load("C:/kooliProjekt/Untitled.png")

hero_x = 1800
hero_y = 1000
acceleration = 1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        acceleration += 150
    if keys[pygame.K_RIGHT]:
        hero_x += 1
    if keys[pygame.K_LEFT]:
        hero_x -= 1


    if event.type == pygame.KEYUP:
        if acceleration < 1:
            acceleration = 1
        elif event.key == pygame.K_UP and acceleration != 1:
            acceleration = acceleration / 1.1

    movement = math.log(acceleration, 4)
    hero_y -= movement

    if hero_y < -100:
        hero_y = 1200

    if hero_y > 1200:
        hero_y = -100

    if hero_x < -100:
        hero_x = 2000

    if hero_x > 2000:
        hero_x = -100


    # blit the hero image onto the screen
    screen.blit(hero_image, (hero_x, hero_y))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()