import re
import socket

def serviceback(client_tcpsocket):
    request = client_tcpsocket.recv(1024).decode("utf-8")
    requestarr = request.splitlines()
    print(requestarr)
    result = re.match(r"[^/]+/([^ ]*)", requestarr[0])
    # print("===============")
    # print(result.group(1))
    if result:
        print("===============")
        print(result.group(1))
        filename = result.group(1)
        # 回傳header給client
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        # body
        # response += "hello world!"
        try:
            f = open("./"+filename, "r")
            htmlcontent = f.read()
            f.close()
            client_tcpsocket.send(response.encode("utf-8"))
            client_tcpsocket.send(htmlcontent.encode("utf-8"))

        except:
            response = "HTTP/1.1 404 NOT FOUND!\r\n"
            response += "\r\n"
            response += "no page"
            client_tcpsocket.send(response.encode("utf-8"))
        client_tcpsocket.close()



def main():
    #1.建立tcp socket
    server_tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.綁定
    server_tcpsocket.bind(("192.168.0.5", 58889))
    #3.監聽socket
    server_tcpsocket.listen(128)

    while True:
        # 4.等待接收客戶端accept
        client_tcpsocket, clientaddr = server_tcpsocket.accept()
        #5.將數據回傳客戶端
        serviceback(client_tcpsocket)
        # client_tcpsocket.close()

    #6關閉socket
    server_tcpsocket.close()
if __name__ == "__main__":
    main()