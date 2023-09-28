import pygame, classes

pygame.init()
Clock = pygame.time.Clock()

Screen_wigth, Screen_height = 1080, 720
Fps = 60
Display = pygame.display.set_mode((Screen_wigth, Screen_height))
pygame.display.set_caption("Ball sim")

running = True
Background_colour = (255, 255, 255)

ball = classes.ball(Display)
balls = pygame.sprite.Group(ball)

ground = classes.ground(Display)
ground_g = pygame.sprite.GroupSingle(ground)

mouse = False

def update():
    Display.fill(Background_colour)
    balls.update(ground)
    balls.draw(Display)
    ground_g.draw(Display)
    pygame.display.flip()

while running:
    Clock.tick(Fps)
    update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = False
    if mouse:
        ball = classes.ball(Display, pygame.mouse.get_pos())
        balls.add(ball)
