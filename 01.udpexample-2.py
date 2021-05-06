import socket

def main():
  #1. 建立 tcp socket
  udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  #2. 準備receive端的IP(192.168.0.x) PORT:xxxx(數字)
  #destaddr = ("192.168.0.5", 8888)
  destip = input("dest ip: ")
  port = int(input("port:"))

  #3. 鍵盤獲得資料
  senddata = input("input data: ")

  #4. 發送數據
  udpsocket.sendto(senddata.encode("utf-8"), (destip, port))

  #5. 關閉socket
  udpsocket.close()

if __name__ == "__main__":
  main()
