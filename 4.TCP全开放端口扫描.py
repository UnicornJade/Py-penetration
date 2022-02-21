from scapy.all import *
from whois import whois
import socket
from random import randint
import time


def main():
    ip = ""
    port=445
    #发送SYN
    packet=IP(dst=ip)/TCP(sport=12345,dport=port,flags="S")
    resp=sr1(packet,timeout=20)
    if(str(type(resp))=="<type 'NoneType'>"):
        print("port %s is closed"%(port))
    elif(resp.haslayer(TCP)):
        #0x12返回SYN+ACK同意继续链接
        if(resp.getlayer(TCP).flags==0x12):
            send_rst=sr(IP(dst=ip)/TCP(sport=12345,dport=port,flags="AR"),timeout=20)
            print("port %s is up~~"%(port))
        #0x14是RST+ACK，表明目标端口是关闭的
        elif(resp.getlayer(TCP).flags==0x14):
            print("port %s is down!!!!"%(port))

if __name__ == '__main__':
    main()
