import socket

def sendfiletoclient(clientsocket):
    #1.接收客戶端文件名稱
    filename = clientsocket.recv(1024).decode("utf-8")
    filecontent =None
    #2.打開文件讀取數據
    try:
        f = open(filename, "r")
        filecontent = f.read()
    except:
        print("No file %s" % filename)
    #3發送文件數據
    if filecontent:
        clientsocket.send(filecontent.encode("utf-8"))


def main():
  #建立socket
  tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  #綁定ip&port
  tcpsocket.bind(("", 58888))

  #監聽socket
  tcpsocket.listen(128)

  while True:
      #接受accept等待客戶連結
      clientsocket, clientaddr = tcpsocket.accept()
      print(clientaddr)
      #傳送檔案給客戶端
      sendfiletoclient(clientsocket)
      clientsocket.close()
  tcpsocket.close()

if __name__ == "__main__":
  main()

