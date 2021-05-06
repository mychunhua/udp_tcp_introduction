import time
import threading

numbercount = 100
def task1():
  global numbercount  
  numbercount = numbercount + 1
  print("---task1----numbercount=%d" % numbercount)

def task2():
  print("---task2----numbercount=%d" % numbercount)

def main():
  ttask1 = threading.Thread(target=task1)
  ttask2 = threading.Thread(target=task2)
  ttask1.start()
  time.sleep(1)
  ttask2.start()
  time.sleep(1)
  print("main thread numbercount=%d" % numbercount)

if __name__ == "__main__":
  main()
