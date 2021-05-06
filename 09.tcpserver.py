import socket

def main():
  #建立socket
  tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  #綁定ip&port
  tcpsocket.bind(("", 58888))

  #監聽socket
  tcpsocket.listen(128)

  #接受accept等待客戶連結
  clientsocket, clientaddr = tcpsocket.accept()
  print(clientaddr)

  #收客戶端資料
  recvdata = clientsocket.recv(1024)
  print(recvdata)

  clientsocket.send("hello".encode("utf-8"))
  clientsocket.close()
  tcpsocket.close()

if __name__ == "__main__":
  main()

