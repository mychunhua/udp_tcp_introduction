import socket
#1. 建立 udp socket
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#2. 準備receive端IP, PORT:xxxx(數字)
localaddr = ("", 58888) #IP一般不用寫表示本機任何一個IP
udpsocket.bind(localaddr)
#3. 接收數據
recvdata = udpsocket.recvfrom(1024) #1024接收最大字節數
#4. 顯示接收的數據
print(recvdata[0].decode("gbk")) 
#5. 關閉socket
udpsocket.close()
