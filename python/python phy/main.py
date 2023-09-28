import pygame, classes
pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
screen = pygame.display.set_mode([1280, 720])
Fps = 60

phy_object_group = pygame.sprite.Group()
obj1 = classes.Phy_obj(50, 1, (255, 0, 0), pygame.Rect(250, 250, 0, 0))

obj2 = classes.Phy_obj(50, 1, (255, 0, 0), pygame.Rect(500, 500, 0, 0))
phy_object_group.add(obj1)
phy_object_group.add(obj2)

# Run until the user asks to quit
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    phy_object_group.update(phy_object_group.sprites())

    screen.fill((255, 255, 255))
    phy_object_group.draw(screen)

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()