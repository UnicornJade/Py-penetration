from scapy.all import *
from whois import whois
import socket
from random import randint
import time

####判断主机是否存活(端口扫描结果可信度不高)
def main():
    ip = ""

    ans, uans = sr(IP(dst=ip) / UDP(dport=80))

    for snd, rcv in ans:
        print(rcv.sprintf("%IP.src% is up"))

if __name__ == '__main__':
    main()
