# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

hero_image = pygame.image.load("C:/kooliProjekt/Untitled.png")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 0, 0))

    hero_x = 500
    hero_y = 300

    # blit the hero image onto the screen
    screen.blit(hero_image, (hero_x, hero_y ))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()