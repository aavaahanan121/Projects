import pygame, math

class Phy_obj(pygame.sprite.Sprite):
    count = 0
    def __init__(self, r:float,mass:float, color, rect:pygame.Rect):
        print("Object Created")
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((r*2, r*2))
        self.image.set_colorkey((0,0,0))
        pygame.draw.circle(self.image, color, (r, r), r)
        self.mass = mass
        self.rect = pygame.Rect(rect.x, rect.y, r, r)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)
        self.vector = pygame.math.Vector2(self.rect.x, self.rect.y)
        Phy_obj.count += 1
        self.id = Phy_obj.count
        print("Object Ready")
    
    def update(self, Objects: list):
        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
        self.vector = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        if len(Objects) == 2:
            if Objects[0].id != self.id:
                object2 = Objects[0]
            else:
                object2 = Objects[1]
            # self.velocity += pygame.math.Vector2(self.mass * object2.mass / math.sqrt(pygame.math.Vector2.distance_to(self.vector, object2.vector)))
            # self.velocity.rotate(self.velocity.angle_to(object2.vector))
            self.acceleration.x += self.mass * object2.mass / (self.vector.x - object2.vector.x) 
            self.acceleration.y += self.mass * object2.mass / (self.vector.y - object2.vector.y) 

            print(self.velocity, self.id, self.count)

