import network
#import socket
import wifideets
from time import sleep
import urequests

network.hostname('SonosBattDisp')

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(wifideets.ssid, wifideets.password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip


try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()


try:
    battery_json = urequests.get("http://" + hostAndPort + "public/battery_data.json" )
except Exception as exc:
    print(exc)
    print('------ error sleepy time------')
    deepsleep(60000)

   
#fetch file
#check if file has timestamp
#check if timestamp is greater than last time stamp
    #if it is, refresh display
    #if skip
#sleep





