import threading
import time

def task1():
    for i in range(6):
        print("___task1___%d" % i)
        time.sleep(1)

def task2():
    for i in range(6):
        print("___task2___%d" % i)
        time.sleep(1)

def main():
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
    while True:
        length = len(threading.enumerate())
        if length <= 1:
            break
        print("len = %d" % length)
        time.sleep(1)
    print("main threading...")

if __name__ == "__main__":
    main()