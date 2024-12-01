import framebuf, futaba_8md06inkm, time
from machine import Pin, freq, SPI

freq(240000000)

hspi = SPI(1, baudrate=5000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))

en = Pin(4, Pin.OUT)
rst = Pin(5, Pin.OUT)
cs = Pin(26, Pin.OUT)

display = futaba_8md06inkm.VFD(hspi, rst, cs, en)

display.text('Hello', 0, 0)
display.show()