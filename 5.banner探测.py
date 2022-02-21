from scapy.all import *
from whois import whois
import socket
from random import randint
import time


def main():
    ip = ""
    port=80

    s=socket.socket()
    s.connect((ip,port))
    s.send("nihao".encode())

    #1024表示，最多每次接受1024字节
    banner=s.recv(1024)
    s.close()
    print("banner is {}".format(banner))


if __name__ == '__main__':
    main()
