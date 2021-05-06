import socket

def service_client(client_tcpsocket):
  #1.接收瀏覽器發送的請求 GET / HTTP/1.1
  request = client_tcpsocket.recv(1024)
  print(request.decode("utf-8"))

  #2.返回http數據給瀏覽器
  #header
  response = "HTTP/1.1 200 OK\r\n"
  response += "\r\n"
  #body
  # response += "hello world!"
  f = open("./html/index.html", "r")
  htmlcontent = f.read()
  f.close()
  client_tcpsocket.send(response.encode("utf-8"))
  client_tcpsocket.send(htmlcontent.encode("utf-8"))
  client_tcpsocket.close()

def main():
  #1.建立tcp socker
  server_tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #2.綁定
  server_tcpsocket.bind(("", 58888))
  #3.監聽
  server_tcpsocket.listen(128)
  while True:
    #4.等待客戶accept連結
    client_tcpsocket, clientaddre = server_tcpsocket.accept()
    #5.為客戶服務
    service_client(client_tcpsocket)
  server_tcpsocket.close()

if __name__ == "__main__":
  main()
