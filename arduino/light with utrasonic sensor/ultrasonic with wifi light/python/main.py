import serial
from tuyapy import TuyaApi
import json

api = TuyaApi()
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

def init():
    with open('C:/Users/Aavaa/Documents/Projects/arduino/light with utrasonic sensor/ultrasonic with wifi light/python/config.json') as config:
        data = json.load(config)
    username = data['username']
    password = data['password']
    country_code = data['country_code']
    application = data['application']
    print("Logging in for {}".format(username))
    api.init(username, password, country_code, application)
    device_ids = api.get_all_devices()
    lights = dict(sorted(dict((i.name(), i) for i in device_ids if i.obj_type == 'light').items()))
    devices = {**lights}
    devices_list = [*devices.values()]
    return devices_list[0]

light = init()

turn_off(light)

arduino = serial.Serial(port="COM5", baudrate=9600)
while True:
    data = arduino.read()
    if data == b'1':
        turn_on(light)
        break
