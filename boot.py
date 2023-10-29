try:
    import usocket as socket
except:
    import socket

from machine import Pin
from lib import ds18x20, onewire
import network
import gc

gc.collect()

ds_pin = Pin(13)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))


ssid = 'modem34'
password = '14312076'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print(station.ifconfig())
