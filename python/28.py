import socket


def serviceclient(client_tcpsocket):
    # 接收瀏覽器發送的請求GET /HTTP/1.1
    recvdata = client_tcpsocket.recv(1024).decode("utf-8")
    print(recvdata)
    # 返回http數據給瀏覽器
    # header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # body
    # response += "hello"
    f = open("./index.html", "r")
    htmcontent = f.read()

    client_tcpsocket.send(response.encode("utf-8"))
    client_tcpsocket.send(htmcontent.encode("utf-8"))


def main():
    # 建立tcp socket
    server_tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 綁定ip與port
    server_tcpsocket.bind(("", 58889))
    # 監聽socket
    server_tcpsocket.listen(128)
    # 等待接收客戶連線accept
    client_tcpsocket, clientaddr = server_tcpsocket.accept()
    # 為客戶服務
    serviceclient(client_tcpsocket)


if __name__ == "__main__":
    main()