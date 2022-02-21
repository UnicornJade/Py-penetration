from scapy.all import *
from scapy.utils import PcapWriter

def packetHandler(pkt):
    src=pkt[IP].src
    srcPort=pkt[IP].dst

    #pktdump.write(pkt)

#pktdump=PcapWriter('test1.pcap',append=True,sync=True)
sniff(filter='tcp and port 80',prn=packetHandler,iface='eth0',offline="test1.pcap")

# packets=rdpcap('test1.pcap')


