import pygame, math

gravity = 2
max_speed = 20
speed = 1
max_speed_x = 1
friction = 0.5
image = pygame.transform.smoothscale(pygame.image.load("images/bg.jpg"), (1280, 720))


def update(screen:pygame.surface, bg_color, ball_g:pygame.sprite.GroupSingle, obstacles:pygame.sprite.Group):
    screen.blit(image, (0, 0))
    obstacles.update()
    ball_g.update(obstacles)
    obstacles.draw(screen)
    ball_g.draw(screen)
    # pygame.draw.rect(screen, (255, 255, 255), ball_g.sprite.rect)
    pygame.display.flip()

class ball(pygame.sprite.Sprite):
    def __init__(self, size = 50):
        print("Player is being created...")
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.surface.Surface([size, size])
        # self.image.fill((255, 255, 255))
        # pygame.draw.circle(self.image, (0, 0, 255), (size/2, size/2), size/2)
        # self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.smoothscale(pygame.image.load("images/png/Default/ball_red_large.png"), (size, size))
        self.rect = pygame.rect.Rect(100, 100, size, size)
        self.vel = pygame.Vector2()
        self.on_ground = False
        self.jumping = False
        self.moving_left = False
        self.moving_right = False
    
    def update(self, obstacles):
        collider = pygame.sprite.spritecollideany(self, obstacles)
        if  collider != None and collider.rect.x < self.rect.x:
            self.on_ground = True
        if not self.on_ground:
            self.vel.y += gravity
            self.vel.y = min(self.vel.y, max_speed)
            self.jumping = False
        else:
            if not self.jumping:
                self.vel.y = 0
            if collider == None:
                self.on_ground = False
        if self.moving_left == self.moving_right:
            dir = 0 
        dir = 0
        if self.moving_right:
            dir = 1
        elif self.moving_left:
            dir = -1
        else:
            dir = 0
        # print(self.moving_left, self.moving_right)
        self.move(dir)
        self.rect.y += self.vel.y
        self.rect.x += self.vel.x
        # self.rect.x = min(self.vel.x, 1280)
        # self.rect.x = max(self.vel.x, 0)
    def jump(self):
        if self.on_ground:
            print("jumping")
            self.jumping = True
            self.vel.y = -25
    def move(self, dirc):
        if dirc != 0:
            self.vel.x += speed * dirc
        else:
            if self.vel.x > 0.3:
                self.vel.x -= friction
            elif self.vel.x < 0.3:
                self.vel.x += friction
            else:
                self.vel.x = 0
        if self.rect.x > 1285:
            self.rect.x = 10
            self.vel.x = 0
        
        if self.rect.x < -5:
            self.rect.x = 1270
            self.vel.x = 0

class obstacle(pygame.sprite.Sprite):
    def __init__(self, no, loc_x, loc_y):
        print("obstacle is being created...")
        size_x = no * 64
        self.image = pygame.surface.Surface((size_x, 64))
        self.image.set_colorkey((0, 0, 0))
        block = pygame.image.load("images/PNG/Default/block_square.png")
        for i in range(0, 64%size_x):
            self.image.blit(block, (i * 64, 0))
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.rect.Rect(loc_x, loc_y, size_x, 64)
