import socket

def main():
    #建立udp socket
    udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #連結server端IP與Port
    # destaddr = ("192.168.0.5", 58888)
    destip = input("請輸入IP: ")
    destport = int(input("請輸入PORT: "))
    while True:
        #傳送數據
        senddata = input("請輸入傳送資料: ")
        if senddata == "exit":
            break
        udpsocket.sendto(senddata.encode("utf-8"), (destip, destport))
    #關閉udp socket
    udpsocket.close()

if __name__ == "__main__":
    main()