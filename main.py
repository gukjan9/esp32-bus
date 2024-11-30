import framebuf, futaba_8md06inkm, time
from machine import Pin, freq, SPI

freq(240000000)

hspi = SPI(1, baudrate=5000000, polarity=0, phase=0)

en = Pin(24, Pin.OUT)
rst = Pin(23, Pin.OUT)
cs = Pin(8, Pin.OUT)

display = futaba_8md06inkm.VFD(hspi, rst, cs, en)

display.clear()
display.text("Hello, VFD!", 0, 0)
display.show()

time.sleep(5)

display.clear()
display.show()