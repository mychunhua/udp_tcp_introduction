import socket
from pynput.keyboard import Key, Listener

#建立udp socket
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#設定IP與PORT
destip = input("IP: ")
destport = int(input("PORT: "))
num = 0
def on_press(key):
    global udpsocket, destip, destport, num
    if key == Key.ctrl:
        num += 1
        udpsocket.sendto(str(num).encode("utf-8"), (destip, destport))

with Listener(on_press=on_press) as listener:
    listener.join()
