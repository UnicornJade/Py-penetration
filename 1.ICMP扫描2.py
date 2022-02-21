from scapy.all import *
from whois import whois
import socket
from random import randint

def main():
    #重要的都在ans
    ans, uans = sr(IP(dst="") / ICMP())
    #snd是发送的数据，rcv是接收的数据
    for snd,rcv in ans:
        print(rcv.sprintf("%IP.src% is alive now"))
    pass

if __name__ == '__main__':
    main()
