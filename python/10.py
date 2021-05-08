import socket

def main():
    #建立tcp socket
    server_tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #綁定IP與Port
    server_tcpsocket.bind(("", 58888))
    print("bind...")
    #監聽listen socket
    server_tcpsocket.listen(128)
    print("listen...")
    while True:
        #等待客戶連結accept
        client_tcpsocket, client_tcpaddr = server_tcpsocket.accept()
        print("客戶%s連結..." % str(client_tcpaddr))
        recvdata = client_tcpsocket.recv(1024)
        print(recvdata.decode("utf-8"))
        client_tcpsocket.send("hello".encode("utf-8"))
        #關閉tcp socket
        client_tcpsocket.close()
    server_tcpsocket.close()

if __name__ == "__main__":
    main()