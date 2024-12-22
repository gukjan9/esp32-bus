import futaba_8md06inkm
from machine import Pin, freq, SPI
import time, json, framebuf
import wifi, bus

R9030 = ['229001697', '229001669', '229001668', '229001666', '229000886', '229000885', '229000852', '229000851',
         '229000850', '229000849', '229000826', '229000557', '229001803', '229001394', '229001659', '229001545',
         '229000937', '229001553', '229001552']

R7625 = ['229000940', '229000515', '229000664', '229002348', '229001582', '229001583', '229001497', '229001552']

departure = '229001552'

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
        return ' ' + stationSeq + 's'

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