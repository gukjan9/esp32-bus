import network
import json

def connect():
    with open('config.json', 'r') as e:
        config = json.load(e)

    ssid = config['ssid']
    password = config['password']

    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass

    print('와이파이:', wlan.ifconfig())