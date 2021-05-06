import socket

def main():
    #1.連結tcp socket
    client_tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.綁定server ip與port
    #3.連結server
    client_tcpsocket.connect(("192.168.0.5", 58888))
    # 4.獲取下載的文件名稱
    dwfilename = input("請輸入檔名")
    #5.將文件名稱發送到server
    client_tcpsocket.send(dwfilename.encode("utf-8"))
    #6.傳送文件數據
    recvdata = client_tcpsocket.recv(1024)
    if recvdata:
        #7.保存數計到本地一個文件中
        with open("[new]"+dwfilename, "w") as f:
            f.write(recvdata.decode("utf-8"))

    #8.關閉tcp socket
    client_tcpsocket.close()
if __name__ == "__main__":
    main()