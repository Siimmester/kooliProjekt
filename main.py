# Example file showing a basic pygame "game loop"
import pygame
import math
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1910, 1070))
clock = pygame.time.Clock()
running = True

hero_image = pygame.image.load("C:\kooliProjekt/Untitled.png")
asteroid_image = pygame.image.load("C:\kooliProjekt/Untitled.png")

hero_x = 1800
hero_y = 1000
acceleration = 1
time_helddown = 0
rotation = 0
var1 = 1
var2 = 0

asteroids = []
asteroid_speed_range = (1, 3)

for _ in range(10):
    x = random.randint(0, 1910)
    y = random.randint(0, 1070)
    speed = random.uniform(*asteroid_speed_range)
    angle = random.uniform(0, 360)
    asteroids.append({
        "x": x,
        "y": y,
        "speed": speed,
        "angle": angle
    })

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
        if time_helddown < 1:
            time_helddown += 0.01
        acceleration += 300 * time_helddown

    if keys[pygame.K_RIGHT]:
        if rotation >= 360:
            rotation -= 360
        elif rotation <= 0:
            rotation += 360
        rotation -= 1

    if keys[pygame.K_LEFT]:
        if rotation <= 0:
            rotation += 360
        elif rotation >= 360:
            rotation -= 360
        rotation += 1

    if time_helddown > 0:
        time_helddown -= 0.01
    if acceleration < 1:
        acceleration = 1
    elif not keys[pygame.K_UP] and acceleration != 1:
        acceleration = acceleration / 1.03

    movement = math.log(acceleration, 4)
    
    # Ei ole oluline kuidas see töötab,
    # ainult, et see kuidagi töötab. Amen
    # Corinthians 13:4-5

    if 90 >= rotation >= 0:
        if rotation != 0:
            var1 = rotation / 90
        else:
            var1 = 0
        var2 = movement * var1

        var3 = movement - var2
        hero_y -= var3
        hero_x -= var2

    if 180 >= rotation > 90:
        rotation1 = rotation - 90
        var1 = rotation1 / 90
        var2 = movement * var1
        var3 = movement - var2

        hero_y += var2
        hero_x -= var3

    if 270 >= rotation > 180:
        rotation1 = rotation - 180
        var1 = rotation1 / 90
        var2 = movement * var1
        var3 = movement - var2

        hero_y += var3
        hero_x += var2

    if 360 >= rotation > 270:
        rotation1 = rotation - 270
        var1 = rotation1 / 90
        var2 = movement * var1
        var3 = movement - var2

        hero_y -= var2
        hero_x += var3

    if hero_y < -100:
        hero_y = 1200

    if hero_y > 1200:
        hero_y = -100

    if hero_x < -100:
        hero_x = 2000

    if hero_x > 2000:
        hero_x = -100

    for asteroid in asteroids:
        rad_angle = math.radians(asteroid["angle"])
        delta_x = asteroid["speed"] * math.cos(rad_angle)
        delta_y = asteroid["speed"] * math.sin(rad_angle)
        asteroid["x"] += delta_x
        asteroid["y"] += delta_y

        if asteroid["x"] > 1910:
            asteroid["x"] = 0
        elif asteroid["x"] < 0:
            asteroid["x"] = 1910
        if asteroid["y"] > 1070:
            asteroid["y"] = 0
        elif asteroid["y"] < 0:
            asteroid["y"] = 1070

        asteroid_rect = asteroid_image.get_rect()
        asteroid_rect.center = (asteroid["x"], asteroid["y"])
        screen.blit(asteroid_image, asteroid_rect)
    
    # blit the hero image onto the screen
    screen.blit(hero_image, (hero_x, hero_y))
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60) # limits FPS to 60

pygame.quit()