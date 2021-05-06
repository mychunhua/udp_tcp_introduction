import socket
import threading

def recvmsg(udpsocket):
  while True:
    recvdata = udpsocket.recvfrom(1024)
    print(recvdata)

def sendmsg(udpsocket, destip, destport):
  while True:
    senddata = input("send data: ")
    udpsocket.sendto(senddata.encode("utf-8"),(destip, destport))

def main():
  #建立socket
  udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  #綁定本地訊息
  udpsocket.bind(("", 58888))

  destip = input("dest ip: ")
  destport = int(input("dest port: "))

  #收發數據
  t_recv = threading.Thread(target=recvmsg, args=(udpsocket,))
  t_send = threading.Thread(target=sendmsg, args=(udpsocket, destip, destport))
  t_recv.start()
  t_send.start()

if __name__ == "__main__":
  main()
