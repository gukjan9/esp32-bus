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

queryTime, stationId = bus.parse_xml(bus.get_data(config['api_key'], config['ID_9030']))
print(f"Query Time: {queryTime}, First Station ID: {stationId}")

display.display_str(0, queryTime)
