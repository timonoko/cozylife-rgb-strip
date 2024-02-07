#! /usr/bin/python3
import custom_components.cozylife.tcp_client as tcp_client
import time
import colorsys
import sys

a=tcp_client.tcp_client('192.168.1.154')

print(a.query())
"""
for x in range(24):
    for y in range(10):
        a.control({'4':y*100,'5':x*10,'6':1000})
        time.sleep(0.1)
"""
def rgb(r,g,b):
    a.query()
    h,s,v=colorsys.rgb_to_hsv(r/256,g/256,b/256)
    b={'4':int(v*1000),'5':int(h*360),'6':int(s*1000)}
    a.control(b)
    print(a.query())
    return (h,s,v)

def hex2(s): return(eval("0x"+s))
def hexa(s):
    rgb(hex2(s[0:2]),hex2(s[2:4]),hex2(s[4:6]))
    print(hex2(s[0:2]),hex2(s[2:4]),hex2(s[4:6]))

def testi():
    while True:
        hexa('ff0000')
        time.sleep(1)
        hexa('ffff00')
        time.sleep(1)
        hexa('00ff00')
        time.sleep(1)
        hexa('0000ff')
        time.sleep(1)
        hexa('ffffff')
        time.sleep(1)

def sumua(): hexa('ffa040')
def hamara(): hexa('402038')



eval(sys.argv[1]+"()")



