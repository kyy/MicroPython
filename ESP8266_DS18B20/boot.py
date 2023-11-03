import network
import gc


WFSSID = 'iga-umet'
WFKEY = 'umet2020'

gc.collect()

station = network.WLAN(network.STA_IF)  # noqa

def wf_con():

    if not station.isconnected():
        print(f'\n\nconnecting to network {WFSSID}')
        station.active(True)
        station.connect(WFSSID, WFKEY)
        while not station.isconnected():
            pass
    print('\nnetwork config:', station.ifconfig())


wf_con()
