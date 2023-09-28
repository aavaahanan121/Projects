import pygame

# preferences

background_color = (0, 25, 255)
gravity = 1
max_speed = 30


def update(screen: pygame.surface.Surface, ball_g, obs_g):
    screen.fill(background_color)
    obs_g.update()
    ball_g.update(obs_g)
    obs_g.draw(screen)
    ball_g.draw(screen)
    pygame.display.flip()


class ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((50, 50))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, (0, 255, 0), (25, 25), 25)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.rect.Rect(50, 50, self.width, self.height)
        self.velocity = vector(0, 0)
        

    def update(self, obs_g):
        self.rect.x += self.velocity.x_vel
        self.rect.y += self.velocity.y_vel
        self.velocity.y_vel = min(self.velocity.y_vel, max_speed)
        if not self.on_floor(obs_g):
            self.velocity.y_vel += gravity
        else:
            self.velocity.y_vel = 0
        
    def on_floor(self, obs_g):
        if pygame.sprite.spritecollideany(self, obs_g) != None:
            print("on floor")
            return True
        else:
            return False

class vector:
    def __init__(self, x_vel: float, y_vel: float):
        self.x_vel = x_vel
        self.y_vel = y_vel


class obstacle(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((1280, 50))
        self.image.fill(color)
        self.rect = pygame.Rect(x, y, width, height)
        self.width = width
        self.height = height


if __name__ == "__main__":
    import sys
    import os
    os.system('"' + sys.executable + '" ' + os.getcwd() + "/main.py")
