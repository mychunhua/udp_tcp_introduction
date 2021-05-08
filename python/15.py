import threading
import time
numbercount = 100
def task1():
    global numbercount
    numbercount += 1
    print("___task1___%d" % numbercount)

def task2():
    print("___task1___%d" % numbercount)

def main():
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("main threading numbercount=%d" % numbercount)

if __name__ == "__main__":
    main()