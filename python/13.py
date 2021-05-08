import threading
import time

def task1():
    for i in range(6):
        print("___task1___")
        time.sleep(1)

def task2():
    for i in range(6):
        print("___task2___")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()