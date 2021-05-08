import socket

def main():
    #建立tcp socket
    client_tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #連結server
    serverip = input("server IP: ")
    serverport = int(input("server Port: "))
    client_tcpsocket.connect((serverip, serverport))
    while True:
        #發送數據
        senddata = input("請輸入傳送數據: ")
        client_tcpsocket.send(senddata.encode("utf-8"))
    #關閉tcp socket
    client_tcpsocket.close()

if __name__ == "__main__":
    main()