import json
from tuyapy import TuyaApi
import time, tuyapy

api = TuyaApi()

hue = 0
saturation = 0

def turn_off(device):
    if not isinstance(device, list):
        return device.turn_off()
    else:
        return [i.turn_off() for i in device]


def turn_on(device):
    if not isinstance(device, list):
        return device.turn_on()
    else:
        return [i.turn_on() for i in device]


def change_color(device, r, g, b):
    # Manually adjusting for black white and gray
    h, s, v = rgb_to_hsv(r, g, b)
    if v < 5 or s < 10:
        print("Adjusting from {} to {}".format(str(v),str((210, 4 , 19))))
        h = 210
        s = 4
        v = 19
    change_color_from_hsv(device, h, s, v)


def change_color_from_rgb(device, r, g, b):
    if not isinstance(device, list):
        return device.set_color(rgb_to_hsv(r, g, b))
    else:
        return [i.set_color(rgb_to_hsv(r, g, b)) for i in device]


def change_color_from_hsv(device, h, s, v):
    if not isinstance(device, list):
        return device.set_color((h, s, v))
    else:
        return [i.set_color((h, s, v)) for i in device]


def rgb_to_hsv(r, g, b):
    # Reference: https://www.w3resource.com/python-exercises/math/python-math-exercise-77.php
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    h = 0
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100
    return h, s, v

def wake__up(Light, wait_sec = 0):
    turn_on(Light)
    print("started light wake up sequence")
    # change_color_from_hsv(Light, hue, saturation, 200)

    for i in range(1, 100, 1):
        # change_color_from_hsv(Light, hue, saturation, i)
        print(i)
        time.sleep(1)
        change_color_from_rgb(Light, i, i, i)


def init():
    with open('config.json') as config:
        data = json.load(config)
    username = data['username']
    password = data['password']
    country_code = data['country_code']
    application = data['application']
    print("Logging in for {}".format(username))
    while True:
        try:
            api.init(username, password, country_code, application)
            break
        except tuyapy.tuyaapi.TuyaAPIException as e:
            print("waiting 10 sec", e)
            for _ in range(0, 11):
                time.sleep(1)
                print('.', end='')
            
    device_ids = api.get_all_devices()
    lights = dict(sorted(dict((i.name(), i) for i in device_ids if i.obj_type == 'light').items()))
    devices = {**lights}
    devices_list = [*devices.values()]
    return devices_list[0]
    # while True:
    #     word = input(">")
    #     if word == "wake up":
    #         wake__up(devices_list)
    #     elif word == "quit":
    #         break
    #     else:
    #         print(word , " did not work")