import time
import threading

def task1():
  for i in range(6):
    print("---task1----%d" % i)
    time.sleep(1)

def task2():
  for i in range(12):
    print("---task2----%d" % i)
    time.sleep(1)

def main():
  ttask1 = threading.Thread(target=task1)
  ttask2 = threading.Thread(target=task2)
  ttask1.start()
  #time.sleep(1)
  ttask2.start()

  while True:
    length = len(threading.enumerate())
    print("threading numbers: %d" % length)
    #剩下主Threading則跳出
    if length <= 1:
       break
    time.sleep(1)
  print("main threading....")
if __name__ == "__main__":
  main()
