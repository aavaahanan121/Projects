import pygame

ball_r = 25
ball_colour = (255, 0, 0)

gravity = 1.0

class ball(pygame.sprite.Sprite):
    def __init__(self, Screen : pygame.surface.Surface, center = (300, 300)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ball_r * 2, ball_r * 2])
        pygame.draw.circle(self.image, ball_colour, (ball_r, ball_r), ball_r)
        self.rect = pygame.Rect(300, 300, 50, 50)
        self.rect.center = center
        self.image.set_colorkey((0, 0, 0))
        self.velocity = pygame.Vector2(0, 0)
        self.screen = Screen
    
    def update(self, ground : pygame.sprite.Sprite):
        if self.rect.bottom >= ground.rect.top and abs(self.velocity.y) > 3:
            self.velocity.y = -self.velocity.y / 1.4
            self.rect.bottom = ground.rect.top
        elif self.rect.bottom >= ground.rect.top:
            self.rect.bottom = ground.rect.top
            self.velocity.y = 0
        self.velocity.y += gravity
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        print( self.velocity.y , " --- ", abs(self.velocity.y))
        if not self.is_on_screen:
            self.kill()
    
    @property
    def is_on_screen(self):
        if self.screen.get_height() < self.rect.top or self.rect.bottom < 0 or 0 > self.rect.right or self.rect.left > self.screen.get_width():
            return False
        else:
            return True
        
class ground(pygame.sprite.Sprite):
    def __init__(self, display : pygame.surface.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((display.get_width(), 40))
        self.image.fill((0, 0, 255))
        self.rect = pygame.Rect((0, display.get_height() - self.image.get_height(), self.image.get_width(), self.image.get_height()))
