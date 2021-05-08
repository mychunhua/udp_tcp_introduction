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
    t1 = threading.Thread(target=task1, args=(1000000,))
    t2 = threading.Thread(target=task2, args=(500000,))
    t1.start()
    t2.start()
    print("main threading numbercount=%d" % numbercount)

if __name__ == "__main__":
    main()