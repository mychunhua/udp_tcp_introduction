import multiprocessing
import time

def task1():
    for i in range(60):
        print("___task1___")
        time.sleep(1)

def task2():
    for i in range(60):
        print("___task2___")
        time.sleep(1)

def main():
    # task1()
    # task2()
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)
    p1.start()
    p2.start()

if __name__ == "__main__":
    main()