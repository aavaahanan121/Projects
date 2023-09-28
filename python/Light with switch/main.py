import datetime
import time
import functions, pygame, Classes, tuyapy
from pynput import keyboard

light = functions.init()

on = False

# def click(key):
#     global on
#     print(key)
#     print(type(key))
#     if key == Key.space and not on:
#         functions.turn_on(light)
#         print("turn on")
#         on = True
#     elif key == Key.space and on:
#         print("turn off")
#         functions.turn_off(light)
#         on = False
#     elif key.char == ("r") and keyboard.:
#         print("red")
#         functions.change_color_from_rgb(light, 255, 0, 0)
#         color = 1
#     elif key.char == ("g"):
#         print("green")
#         functions.change_color_from_rgb(light, 0, 255, 0)
#         color = 1
#     elif key.char == ("b"):
#         print("blue")
#         functions.change_color_from_rgb(light, 0, 0, 255)
#         color = 1
#     elif key.char == "w":
#         print("white")
#         functions.change_color_from_rgb(light, 255, 255, 255)
#     elif key == Key.delete:
#         return False

def turn_red():
    print("red")
    functions.change_color_from_rgb(light, 255, 0, 0)

def turn_green():
    print("green")
    functions.change_color_from_rgb(light, 0, 255, 0)

def turn_blue():
    print("blue")
    functions.change_color_from_rgb(light, 0, 0, 255)

def turn_white():
    print("white")
    functions.change_color_from_rgb(light, 255, 255, 255)


def turn_on_off():
   global on
   print("on/off")
   if not on:
       functions.turn_on(light)
       print("turn on")
       on = True
   elif on:
       print("turn off")
       functions.turn_off(light)
       on = False

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Light switch")
clock = pygame.time.Clock()

button = Classes.button(100, 50, 200, 200, (255, 10, 0), color1=(170, 0, 0), text = "On/Off", function=turn_on_off)

buttons = pygame.sprite.Group(button)

running = True
while running:
    clock.tick(60)

    buttons.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed(3))

    screen.fill((255, 255, 255))
    buttons.draw(screen)
    pygame.display.flip()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            print("bye")
            running = False
    