import socket
import threading

def recvmsg(udpsocket):
    while True:
        #接收數據
        recvdata = udpsocket.recvfrom(1024)
        recvmsg = recvdata[0]
        recvaddr = recvdata[1]
        #顯示接收數據
        print("%s:%s" % (recvmsg.decode("utf-8"), str(recvaddr)))

def main():
    #建立udp socket
    udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #綁定IP與Port
    udpsocket.bind(("", 58888))
    t1 = threading.Thread(target=recvmsg, args=(udpsocket,))
    t1.start()

if __name__ == "__main__":
    main()