import threading
import time
numbercount = 0
def task1(n):
    global numbercount
    for i in range(n):
        numbercount += 1
    print("___task1___%d" % numbercount)

def task2(n):
    global numbercount
    for i in range(n):
        numbercount += 1
    print("___task1___%d" % numbercount)

def main():
    t1 = threading.Thread(target=task1, args=(100,))
    t2 = threading.Thread(target=task2, args=(50,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("main threading numbercount=%d" % numbercount)

if __name__ == "__main__":
    main()