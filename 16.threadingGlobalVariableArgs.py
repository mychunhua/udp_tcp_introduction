import time
import threading

def task1(num):
  print("---task1----numbercount=%d" % num)

def task2(num):
  print("---task2----numbercount=%d" % num)

def main():
  ttask1 = threading.Thread(target=task1, args=(100,))
  ttask2 = threading.Thread(target=task2, args=(50,))
  ttask1.start()
  time.sleep(1)
  ttask2.start()
  time.sleep(1)
  #print("main thread numbercount=%d" % numbercount)

if __name__ == "__main__":
  main()
