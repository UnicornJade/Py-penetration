from scapy.all import *
from whois import whois
import socket
from random import randint

def main():
    ip_id = randint(1,65535)
    icmp_id = randint(1,65535)
    icmp_seq = randint(1,65535)
    packet = IP(dst="192.168.183.128",ttl=64,id=ip_id)/ICMP(id=icmp_id,seq=icmp_seq)/b'rootkit'
    result = sr1(packet,timeout=1,verbose=False)
    if result:
        for rcv in result:
            scan_ip = rcv[IP].src
            print(scan_ip+' is alive~~')
    else:
        print('The target ip is dead !!!')


    pass

if __name__ == '__main__':
    main()

