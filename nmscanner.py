import nmap
import optparse

def nmapScan(tgtHost,tgtPort):
    nmscan=nmap.PortScanner()
    nmscan.scan(tgtHost,tgtPort)
    state=nmscan[tgtHost]['tcp'][int(tgtPort)]['state']
    print('[+] '+tgtHost+' tcp/'+tgtPort+' '+state)



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
    for tgtPort in tgtPorts:
        nmapScan(tgtHost,tgtPort)


if __name__ == '__main__':
    main()