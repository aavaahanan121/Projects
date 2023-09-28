import pygame
import classes

pygame.init()
pygame.display.init()
clock = pygame.time.Clock()

height, width = 1280, 720
fps = 60
screen = pygame.display.set_mode([height, width])

running = True

ball = classes.ball()
ball_group = pygame.sprite.Group(ball)
ground = classes.obstacle((165,42,42), 0, 650, 1280, 100)
obstacles = pygame.sprite.Group(ground)

while running:
    classes.update(screen, ball_group, obstacles)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
