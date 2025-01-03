import futaba_8md06inkm
from machine import Pin, freq, SPI
import time, json, framebuf
import wifi, bus

with open('config.json', 'r') as e:
        config = json.load(e)

wifi.connect(config['ssid'], config['password'])
            
freq(240000000)

hspi = SPI(1, baudrate=5000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))
en = Pin(4, Pin.OUT)
rst = Pin(5, Pin.OUT)
cs = Pin(26, Pin.OUT)
display = futaba_8md06inkm.VFD(hspi, rst, cs, en)

def where_is_bus(stationSeq):
    if stationSeq < 0:
        return 'None'
    
    if stationSeq == 0:
        return ' Arr'
    
    else:
        if(stationSeq >= 10): return ' ' + str(stationSeq) + 's'
        else: return '  ' + str(stationSeq) + 's'

def display_route(route_name, route):
    queryTime, stationSeq = bus.parse_xml(bus.get_data(config['api_key'], config[f'ID_{route_name}']))
    print(f"Query Time: {queryTime}, Station Seq: {stationSeq}")

    queryTime = queryTime[11:19]
    now = where_is_bus(stationSeq)
    print(now)

    display.fill(0)
    display.display_str(0, queryTime)
    time.sleep(2)
    display.fill(0)
    display.display_str(0, route_name)
    display.display_str(4, str(now))
    time.sleep(3)

while True:
    display_route('9030', R9030)
    time.sleep(10)
    display_route('7625', R7625)
    time.sleep(10)
