import socket
import threading
from pynput.keyboard import Key, Listener
num=0
#create
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#get ip & port
destip = input("ip:")
destport = int(input("port:"))

def on_press(key):
  global udpsocket
  global destip
  global destport
  global num

  if key == Key.ctrl:
      num += 1
      udpsocket.sendto(str(num).encode("utf-8"),(destip,destport))

with Listener(on_press=on_press) as listener:
  listener.join()  
