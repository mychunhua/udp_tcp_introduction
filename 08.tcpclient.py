import socket

def main():
  #create socket
  tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  #連結server
  serverip = input("server ip:")
  serverport = int(input("server port:"))
  tcpsocket.connect((serverip, serverport))

  #收發訊息
  senddata = input("send data:")
  tcpsocket.send(senddata.encode("utf-8"))

  #關閉服務
  tcpsocket.close()

if __name__ == "__main__":
  main()
