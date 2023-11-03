import gc
import socket
import time
from lib.ds18x20 import DS18X20
from lib.onewire import OneWire
from machine import Pin


d6 = Pin(12, Pin.IN, Pin.PULL_UP)
d7 = OneWire(Pin(13))
d8 = Pin(15, Pin.OUT)

ds = DS18X20(d7)

roms = ds.scan()


def read_ds_sensor():
    rom = roms[0]
    ds.convert_temp()
    time.sleep_ms(800)
    ds.resolution(rom, 12)
    temp_far = ds.read_temp(rom)
    temp_cels = (temp_far - 32) * 5/9

    return round(temp_cels, 2)


def web_page():
    try:
        temp = read_ds_sensor()
    except:
        temp = None
    html = """<!DOCTYPE HTML><html>
    <head>
    
  <style> html { font-family: Arial; display: inline-block; margin: 0px auto; text-align: center; }
    h2 { font-size: 3.0rem; } p { font-size: 3.0rem; } .units { font-size: 1.2rem; } 
    .ds-labels{ font-size: 1.5rem; vertical-align:middle; padding-bottom: 15px; }
  </style>
  
  </head><body>
  
  <h2>ESP with DS18B20</h2>
  
  <p><i style="color:#059e8a;"></i> 
    <span class="ds-labels">Temperature</span>
    <span id="temperature">""" + str(temp) + """</span>
  </p>"""
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    s: socket
    conn, addr = s.accept()
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn.settimeout(3.0)
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
