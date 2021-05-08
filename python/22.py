import socket


def main():
    #1.建立tcp socket
    server_tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.綁定IP與Port
    server_tcpsocket.bind(("", 58888))
    #3.監聽socket
    server_tcpsocket.listen(128)
    while True:
        #4.等待接收客戶端accept
        client_tcpsocket, clientaddr = server_tcpsocket.accept()
        #5.讀server端檔案，傳送資料給客戶端
        recvdata = client_tcpsocket.recv(1024)
        filecontent = None
        try:
            f = open("./"+recvdata.decode("utf-8"), "r")
            filecontent = f.read()
        except:
            print("file not found")
        if filecontent:
            client_tcpsocket.send(filecontent.encode("utf-8"))
        #6.關閉tcp socket
        client_tcpsocket.close()
    server_tcpsocket.close()

if __name__ == "__main__":
    main()