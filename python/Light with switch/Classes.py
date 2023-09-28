import pygame

pygame.font.init()
font = pygame.font.Font("font/SourceCodePro-Regular.ttf", 24)


def reder_text(text: str, screen: pygame.Surface = None, color=(0, 0, 0), loc=(0, 0), blit: bool = False):
    image = font.render(text, True, color)
    if blit:
        screen.blit(image, loc)
    else:
        return image


class button(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color, text_color=(1, 1, 1), color1: tuple = (100, 100, 100), color2=(50, 50, 50), text="", border=7, function=None, args=None):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.rect.Rect(pos_x, pos_y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.set_colorkey((0, 0, 0))
        self.draw_rect = pygame.Rect(0, 0, width, height)
        pygame.draw.rect(self.image, color, self.draw_rect,
                         border_radius=border)
        self.color = color
        self.color1 = color1
        self.color2 = color2
        self.border = border
        self.function = function
        self.functionargs = args
        self.clicked = False
        self.text_img = reder_text(text, self.image, text_color, (0, 0))
        self.text_loc = (self.rect.width/2 - self.text_img.get_rect().centerx,
                         self.rect.height/2 - self.text_img.get_rect().centery)

    def update(self, mouse_pos, is_pressing):
        if self.rect.collidepoint(mouse_pos) and is_pressing[0]:
            if not self.clicked:
                self.image.fill((0, 0, 0))
                pygame.draw.rect(self.image, self.color2,
                                 self.draw_rect, border_radius=self.border)
                self.image.blit(self.text_img, self.text_loc)
                self.clicked = True
                self.click()
        elif self.rect.collidepoint(mouse_pos):
            self.image.fill((0, 0, 0))
            pygame.draw.rect(self.image, self.color1,
                             self.draw_rect, border_radius=self.border)
            self.image.blit(self.text_img, self.text_loc)
            self.clicked = False
        else:
            self.image.fill((0, 0, 0))
            pygame.draw.rect(self.image, self.color,
                             self.draw_rect, border_radius=self.border)
            self.image.blit(self.text_img, self.text_loc)
            self.clicked = False

    def click(self):
        if self.function != None and self.functionargs != None:
            self.function(self.functionargs)
        elif self.function != None:
            self.function()

    def connect_click(self, function):
        self.function = function
