from scapy.all import *
from whois import whois
import socket
from random import randint
import time

####判断主机是否存活(端口扫描结果可信度不高)
def main():
    ip = ""
    #dport=randint(1,65535)

    packet=IP(dst=ip)/TCP(flags="A",dport=dport)
    response=sr1(packet,timeout=1.0,verbose=0)
    if response:
        #RST
        if int(response[TCP].flags)==4:
            time.sleep(0.5)
            print(ip+"is up~~")
        else:
            print(ip+" is down!!!!")

if __name__ == '__main__':
    main()
