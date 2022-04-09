import optparse
from socket import *
from threading import *
import time
import nmap
from scapy.all import *

screenLock=Semaphore(value=1)
def connScan(tgtHost,tgtPort):
    try:
        # connSkt=socket(AF_INET,SOCK_STREAM)
        # connSkt.connect((tgtHost,tgtPort))
        # connSkt.send('Refer'.encode())
        # results=connSkt.recv(1024)
        # time.sleep(10)
        # screenLock.ac
        # print('[+] %d/tcp open'%tgtPort)
        # print('[+] '+str(results))
        # connSkt.close()
####tcp半开放扫描
        # 发送SYN
        packet = IP(dst=tgtHost) / TCP(sport=12345, dport=tgtPort, flags="S")
        resp = sr1(packet, timeout=20)
        screenLock.acquire()
        if (str(type(resp)) == "<type 'NoneType'>"):
            print("[-] port %s is closed" % (tgtPort))
        elif (resp.haslayer(TCP)):
            # 0x12返回SYN+ACK同意继续链接
            if (resp.getlayer(TCP).flags == 0x12):
                """直接发送RST包终止请求"""
                send_rst = sr(IP(dst=tgtHost) / TCP(sport=12345, dport=tgtPort, flags="R"), timeout=20)
                print("[+] %d/tcp open" % (tgtPort))
            # 0x14是RST+ACK，表明目标端口是关闭的
            elif (resp.getlayer(TCP).flags == 0x14):
                print("[-] %d/tcp closed" % (tgtPort))
    except:
        screenLock.acquire()
        print('[-] %d/tcp closed'%tgtPort)
    finally:
        screenLock.release()

def portScan(tgtHost,tgtPorts):
    #确认IP
    try:
        tgtIP=gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s':　Unknown host"%tgtHost)
        return
    try:
        tgtName=gethostbyaddr(tgtIP)
        print('[+] Scan Results For: '+tgtName[0])
    except:
        print('[+] Scan Results For: '+tgtIP)
    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        # connScan(tgtHost,int(tgtPort))
        t=Thread(target=connScan,args=(tgtHost,int(tgtPort)))
        t.start()

def main():

    parser=optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H',dest='tgtHost',type='string',help='目标主机名或ip')
    parser.add_option('-p',dest='tgtPort',type='string',help='目标端口')
    (options, args) = parser.parse_args()
    tgtHost=options.tgtHost
    tgtPorts=options.tgtPort.split(',')
    if(tgtHost==None)|(tgtPorts[0]==None):
        print("[-] 请输入目标host和port[s]")
        exit(0)
    portScan(tgtHost,tgtPorts)


if __name__ == '__main__':
    main()