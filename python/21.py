import socket


def main():
    #1.建立tcp socket
    client_tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.連結伺服器
    client_tcpsocket.connect(("192.168.0.5", 58888))
    #3.傳送接收數據(檔案名稱/下載檔案)
    filename = input("請輸入下載檔案名稱: ")
    client_tcpsocket.send(filename.encode("utf-8"))
    recvdata = client_tcpsocket.recv(1024)
    if recvdata:
        with open("./[new]"+filename, "w") as f:
            f.write(recvdata.decode("utf-8"))
    #4.關閉tcp socket
    client_tcpsocket.close()

if __name__ == "__main__":
    main()
