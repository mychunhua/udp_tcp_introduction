import time
import threading

def task1():
  for i in range(6):
    print("---task1----")
    time.sleep(1)

def task2():
  for i in range(6):
    print("---task2----")
    time.sleep(1)

def main():
  ttask1 = threading.Thread(target=task1)
  ttask2 = threading.Thread(target=task2)
  ttask1.start()
  ttask2.start()

if __name__ == "__main__":
  main()
