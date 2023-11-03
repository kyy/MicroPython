try:
    import usocket as socket
except:
    import socket

import network
import gc

gc.collect()



station = network.WLAN(network.STA_IF)

station.active(True)


station.connect('iga-umet', 'umet2020')

while not station.isconnected():
    pass

print(station.ifconfig())
