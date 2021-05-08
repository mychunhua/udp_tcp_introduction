import socket
import threading

def recvmsg(udpsocket):
    while True:
        recvdata = udpsocket.recvfrom(1024)
        print(recvdata)

def sendmsg(udpsocket, destip, destport):
    while True:
        senddata = input("send data: ")
        udpsocket.sendto(senddata.encode("utf-8"), (destip, destport))

def main():
    #建立udp socket
    udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #綁定IP與Port
    udpsocket.bind(("", 58888))
    #傳送數據
    # sendmsg(udpsocket, "192.168.0.5", 58888)
    # recvmsg(udpsocket)
    t1 = threading.Thread(target=sendmsg, args=(udpsocket, "192.168.0.5", 58888, ))
    t2 = threading.Thread(target=recvmsg, args=(udpsocket,))
    t1.start()
    t2.start()
    #關閉udp socket
if __name__ == "__main__":
  main()
