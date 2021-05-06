import time
import threading
numbercount = 0
def task1(num):
  global numbercount
  for i in range(num):
    numbercount += 1 
  print("---task1----numbercount=%d" % numbercount)

def task2(num):
  global numbercount
  for i in range(num):
    numbercount += 1
  print("---task2----numbercount=%d" % numbercount)

def main():
  ttask1 = threading.Thread(target=task1, args=(1000000,))
  ttask2 = threading.Thread(target=task2, args=(1000000,))
  ttask1.start()
  ttask2.start()

  time.sleep(3)
  print("main thread numbercount=%d" % numbercount)

if __name__ == "__main__":
  main()
