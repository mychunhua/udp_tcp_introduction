import socket

def sendmsg(udpsocket):
  senddata = input("send data:")
  destip = input("destip:")
  destport = int(input("dest port:"))
  udpsocket.sendto(senddata.encode("utf-8"),(destip,destport))  

def recvmsg(udpsocket):
  recvdata = udpsocket.recvfrom(1024)
  recvmsg = recvdata[0]
  recvaddr = recvdata[1]
  print("%s:%s" % (recvmsg.decode("gbk"), str(recvaddr)))

def main():
  #建立socket
  udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  #bind port
  udpsocket.bind(("",58888))

  while True:
    #發送
    sendmsg(udpsocket)
    #接收並且顯示
    recvmsg(udpsocket)

  udpsocket.close()
if __name__ == "__main__":
  main()
