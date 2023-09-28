import pygame
import classes

pygame.init()

screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Game")
background_color = (40, 10, 255)
fps = 50

clock = pygame.time.Clock()

ball = classes.ball()
ball_g = pygame.sprite.GroupSingle(ball)

obstacle = classes.obstacle(1344, 0, 650)
floating_ground = classes.obstacle(5, 500, 450)
obstacle.tag = "ground"
floating_ground.tag = "ground"
obstacles = pygame.sprite.Group([obstacle, floating_ground])

running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("jump")
                ball.jump()
            if event.key == pygame.K_LEFT:
                ball.moving_left = True
                print("left")
            if event.key == pygame.K_RIGHT:
                ball.moving_right = True
                print("right")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ball.moving_left = False
                print("left")
            if event.key == pygame.K_RIGHT:
                ball.moving_right = False
                print("right")

    classes.update(screen, background_color, ball_g, obstacles)
