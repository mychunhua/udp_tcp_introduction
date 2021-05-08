import socket
def sendmsg(udpsocket):
    #連結server端IP與Port
    destip = input("請輸入IP: ")
    destport = int(input("請輸入PORT: "))
    #傳送數據
    senddata = input("請輸入傳送資料: ")
    udpsocket.sendto(senddata.encode("utf-8"), (destip, destport))

def recvmsg(udpsocket):
    #接收數據
    recvdata = udpsocket.recvfrom(1024)
    recvmsg = recvdata[0]
    recvaddr = recvdata[1]
    #顯示接收數據
    print("%s:%s" % (recvmsg.decode("utf-8"), str(recvaddr)))

def main():
    #建立udp socket
    udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #綁定Port
    udpsocket.bind(("", 58888))

    while True:
        # 傳送數據
        sendmsg(udpsocket)
        # 接收數據
        recvmsg(udpsocket)

    #關閉udp socket
    udpsocket.close()

if __name__ == "__main__":
    main()