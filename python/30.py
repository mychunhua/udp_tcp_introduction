import multiprocessing
import re
import socket


def serviceclient(client_tcpsocket):
    # 接收瀏覽器發送的請求GET /HTTP/1.1
    recvdata = client_tcpsocket.recv(1024).decode("utf-8")
    recvdataarr = recvdata.splitlines()
    print(recvdataarr)

    # 返回http數據給瀏覽器
    # header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # body
    # response += "hello"
    #GET /index.html HTTP/1.1
    result = re.match(r"[^/]+/([^ ]*)", recvdataarr[0])
    if result:
        filename = result.group(1)
        print(filename)
        try:
            f = open("./"+filename, "r")
            htmcontent = f.read()
            client_tcpsocket.send(response.encode("utf-8"))
            client_tcpsocket.send(htmcontent.encode("utf-8"))
        except:
            response = "HTTP/1.1 404 NOT FOUND\r\n"
            response += "\r\n"
            response += "no page"
            client_tcpsocket.send(response.encode("utf-8"))
    client_tcpsocket.close()


def main():
    #1.建立tcp socket
    server_tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #2.綁定
    server_tcpsocket.bind(("192.168.0.5", 58888))
    #3.監聽socket
    server_tcpsocket.listen(128)
    while True:
        # 4.等待接收客戶端accept
        client_tcpsocket, clientaddr = server_tcpsocket.accept()
        #5.將數據回傳客戶端
        p = multiprocessing.Process(target=serviceclient, args=(client_tcpsocket,))
        p.start()
        client_tcpsocket.close() #這裡是關閉主程序

    #6關閉socket
    server_tcpsocket.close()
if __name__ == "__main__":
    main()
