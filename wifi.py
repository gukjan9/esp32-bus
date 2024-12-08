import network

def connect(ssid, pw):
    ssid = ssid
    password = pw

    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass

    print('와이파이:', wlan.ifconfig())
