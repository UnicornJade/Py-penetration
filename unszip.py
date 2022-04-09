import zipfile
from zipfile import *
from threading import Thread
import optparse

def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        # return password
        print('[+] Password = '+password+'\n')
    except:
        pass


def main():
    parser=optparse.OptionParser('usage%prog '+'-f <zipfile> -d <dictionary>')
    parser.add_option('-f',dest='zname',type='string',help='zip加密文件')
    parser.add_option('-d',dest='dname',type='string',help='字典')
    (options, args) = parser.parse_args()
    if(options.zname==None)|(options.dname==None)
        print parser.usage
        exit(0)
    else:
        zname=options.zname
        dname=options.dname

    zFile= ZipFile(zname)
    passFile=open(dname)
    for line in passFile.readlines():
        password=line.strip('\n')
        # guess=extractFile(zFile,password)
        t=Thread(target=extractFile,args=(zFile,password))
        t.start()



if __name__ == '__main__':
    main()